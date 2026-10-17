"""Entrenamiento agrupado con MLflow. Requiere dataset preparado y auditar grupos."""
import argparse, json, time
from pathlib import Path
import numpy as np
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import StratifiedGroupKFold,GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

def cargar(path):
    with np.load(path,allow_pickle=False) as a:
        return a["X"],a["y"],a["grupos"]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--data-dir",default="datos/datos_limp")
    p.add_argument("--output",default="resultados")
    a=p.parse_args();src=Path(a.data_dir);out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
    train=list(src.glob("caracteres_train_*.npz"));test=list(src.glob("caracteres_test_*.npz"))
    if len(train)!=1 or len(test)!=1: raise RuntimeError("Se requiere un archivo train y test versionados")
    X,y,g=cargar(train[0]);Xt,yt,gt=cargar(test[0])
    if set(g)&set(gt):raise RuntimeError("Grupos compartidos: detener")
    classes=set(y)
    folds=list(StratifiedGroupKFold(n_splits=3,shuffle=True,random_state=42).split(X,y,groups=g))
    for tr,va in folds:
        if set(g[tr])&set(g[va]) or set(y[tr])!=classes or set(y[va])!=classes:
            raise RuntimeError("Validación de folds fallida")
    tracking=out/"mlflow";tracking.mkdir(exist_ok=True)
    mlflow.set_tracking_uri("sqlite:///"+str((tracking/"mlflow.db").resolve()))
    mlflow.set_experiment("Actividad5_Clasificacion_Caracteres")
    specs=[
        ("LinearSVC",make_pipeline(StandardScaler(),LinearSVC(dual=False,max_iter=3000,random_state=42)),{"linearsvc__C":[.1,1.0]}),
        ("RandomForest",RandomForestClassifier(random_state=42,n_jobs=1),{"n_estimators":[80,120],"max_depth":[15,25]})
    ]
    rows=[]
    for name,model,grid in specs:
        t0=time.perf_counter()
        search=GridSearchCV(model,grid,scoring="f1_macro",cv=folds,n_jobs=1,refit=True,error_score="raise",return_train_score=True)
        search.fit(X,y)
        duration=time.perf_counter()-t0
        pred=search.predict(Xt)
        metrics={"accuracy":accuracy_score(yt,pred),
                 "precision_macro":precision_score(yt,pred,average="macro",zero_division=0),
                 "recall_macro":recall_score(yt,pred,average="macro",zero_division=0),
                 "f1_macro":f1_score(yt,pred,average="macro",zero_division=0),
                 "f1_macro_cv":search.best_score_,"grid_seconds":duration}
        csv=out/f"grid_{name}.csv"
        pd.DataFrame(search.cv_results_).to_csv(csv,index=False)
        with mlflow.start_run(run_name=name+"_GridSearch"):
            mlflow.set_tags({"dataset":"UC3M-LP","alcance":"clasificacion_caracteres","ia_responsable":"no_uso_operativo"})
            mlflow.log_params({"modelo":name,"semilla":42,"cv_folds":3,**search.best_params_})
            mlflow.log_metrics(metrics);mlflow.log_artifact(str(csv))
            mlflow.sklearn.log_model(search.best_estimator_,name="modelo",serialization_format="cloudpickle")
        rows.append({"modelo":name,**metrics,"parametros":str(search.best_params_)})
    pd.DataFrame(rows).to_csv(out/"comparacion.csv",index=False)
    print(pd.DataFrame(rows).to_string(index=False))
    print("ADVERTENCIA: no equivale a reconocimiento completo ni aprobación operativa.")
if __name__=="__main__":main()
