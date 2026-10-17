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
