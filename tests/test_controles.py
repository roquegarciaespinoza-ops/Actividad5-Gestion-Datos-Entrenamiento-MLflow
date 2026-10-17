"""Pruebas de controles básicos sin necesidad de descargar imágenes."""
import numpy as np
from sklearn.model_selection import StratifiedGroupKFold

def test_ausencia_solapamiento():
    grupos=np.repeat(np.arange(18),2)
    y=np.tile(["0","1"],18)
    x=np.zeros((len(y),1))
    cv=StratifiedGroupKFold(n_splits=3,shuffle=True,random_state=42)
    for tr,va in cv.split(x,y,grupos):
        assert set(grupos[tr]).isdisjoint(set(grupos[va]))

def test_no_duplicar_muestras():
    x=np.arange(30).reshape(10,3)
    assert len({tuple(z) for z in x})==10

def test_tipos_numericos_validos():
    x=np.array([[0.0,0.5,1.0]],dtype=np.float32)
    assert np.isfinite(x).all()
    assert 0<=x.min()<=x.max()<=1

def test_preparacion_zip_sintetico(tmp_path):
    """Prueba de integración de datos_prep sin fotografías personales."""
    import io
    import json
    import zipfile
    import sys
    from pathlib import Path
    from PIL import Image

    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "fuentes"))
    from datos_prep import construir

    archivo = tmp_path / "ejemplo.zip"
    with zipfile.ZipFile(archivo, "w") as z:
        for i in range(24):
            name = f"UC3M-LP/train/{i:05d}"
            image = Image.new("RGB", (24, 12), (i * 9 % 255, 60, 90))
            buf = io.BytesIO()
            image.save(buf, format="JPEG")
            z.writestr(name + ".jpg", buf.getvalue())
            anotacion = {
                "imageWidth": 24, "imageHeight": 12,
                "imagePath": f"{i+1:05d}.jpg",
                "lps": [{
                    "lp_id": f"grupo-{i:05d}",
                    "characters": [
                        {"char_id": "0", "bbox_coord": [[0, 0], [8, 12]]},
                        {"char_id": "1", "bbox_coord": [[8, 0], [16, 12]]},
                        {"char_id": "2", "bbox_coord": [[16, 0], [24, 12]]}
                    ]
                }]
            }
            z.writestr(name + ".json", json.dumps(anotacion))
    destino = tmp_path / "limpios"
    construir(archivo, destino)
    with np.load(destino / "caracteres_train_v1.npz", allow_pickle=False) as tr:
        xtr, ytr, gtr = tr["X"], tr["y"], tr["grupos"]
    with np.load(destino / "caracteres_test_v1.npz", allow_pickle=False) as te:
        xte, yte, gte = te["X"], te["y"], te["grupos"]
    assert len(xtr) + len(xte) == 72
    assert xtr.shape[1] == xte.shape[1] == 1024
    assert set(gtr).isdisjoint(set(gte))
    assert set(ytr) == set(yte) == {"0", "1", "2"}
    assert (destino / "manifiesto.json").is_file()
