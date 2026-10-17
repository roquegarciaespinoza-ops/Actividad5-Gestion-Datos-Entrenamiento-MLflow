"""Preparación reproducible UC3M-LP. Prototipo: no validado integralmente en CI."""
import argparse, hashlib, io, json, zipfile
from collections import Counter
from pathlib import Path, PurePosixPath
import numpy as np
from PIL import Image
from sklearn.model_selection import GroupShuffleSplit

EXCLUIDAS = {"I", "U", "O"}
def sha256(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""): h.update(block)
    return h.hexdigest()

def construir(zip_path, destino):
    destino=Path(destino); destino.mkdir(parents=True,exist_ok=True)
    filas=[]; issues=Counter()
    with zipfile.ZipFile(zip_path) as z:
        names=set(z.namelist())
        anotaciones=sorted(n for n in names if n.lower().endswith(".json"))
        for jp in anotaciones:
            try:
                dato=json.loads(z.read(jp).decode("utf-8-sig"))
                jpg=str(PurePosixPath(jp).with_suffix(".jpg"))
                if jpg not in names: issues["imagen_faltante"]+=1; continue
                if str(PurePosixPath(jp).parent / str(dato.get("imagePath",""))) != jpg:
                    issues["imagePath_distinto"]+=1
                with Image.open(io.BytesIO(z.read(jpg))) as src:
                    w,h=src.size; image=src.convert("L")
                if (w,h)!=(int(dato["imageWidth"]),int(dato["imageHeight"])):
                    issues["dimensiones_incorrectas"]+=1; continue
                for i,plate in enumerate(dato.get("lps",[])):
                    plate_id=str(plate.get("lp_id","")).strip().upper()
                    # IDs vacíos se agrupan por matrícula para evitar un grupo universal.
                    group=plate_id or f"{jp}:matricula:{i}"
                    for j,c in enumerate(plate.get("characters",[])):
                        label=str(c.get("char_id",""))
                        if label in EXCLUIDAS or not label.isalnum(): continue
                        try:
                            (x1,y1),(x2,y2)=c["bbox_coord"]
                            if not (0<=x1<x2<=w and 0<=y1<y2<=h): raise ValueError()
                            crop=image.crop((x1,y1,x2,y2)).resize((32,32))
                            vector=np.asarray(crop,dtype=np.float32).reshape(-1)/255.0
                            filas.append((vector,label,group,jp,i,j))
                        except (ValueError,TypeError,KeyError): issues["bbox_invalido"]+=1
            except Exception:
                issues["archivo_no_procesable"]+=1
    if not filas: raise RuntimeError("No se extrajeron caracteres")
    X=np.stack([r[0] for r in filas])
    y=np.asarray([r[1] for r in filas]); groups=np.asarray([r[2] for r in filas])
    splitter=GroupShuffleSplit(n_splits=1,test_size=.2,random_state=42)
    train,test=next(splitter.split(X,y,groups))
    if set(groups[train]) & set(groups[test]): raise RuntimeError("Fuga entre grupos")
    clases=set(np.unique(y))
    if set(y[train])!=clases or set(y[test])!=clases:
        raise RuntimeError("Partición sin cobertura total de clases: revisar estrategia antes de entrenar")
    salidas={}
    for name,ix in [("train",train),("test",test)]:
        p=destino/f"caracteres_{name}_v1.npz"
        np.savez_compressed(p,X=X[ix],y=y[ix],grupos=groups[ix])
        salidas[name]={"ruta":str(p),"registros":len(ix),"sha256":sha256(p)}
    manifest={"origen":"UC3M-LP","version":"experimental-v1","semilla":42,
              "observaciones":len(y),"clases":sorted(clases),"excluidas":sorted(EXCLUIDAS),
              "hallazgos":dict(issues),"archivos":salidas,
              "limitaciones":"IDs parcialmente ocultos: grupos no equivalen a vehículos independientes; no publicar NPZ"}
    (destino/"manifiesto.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding="utf8")
    print(json.dumps(manifest,indent=2,ensure_ascii=False))
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--zip",required=True);p.add_argument("--out",default="datos/datos_limp")
    a=p.parse_args();construir(a.zip,a.out)
