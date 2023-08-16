import numpy as np
import numpy.random as npr

#exercicio 1
def gerar_ndarray (inicio_intervalo, final_intervalo, n_elementos):
    ndarray = npr.randint(inicio_intervalo, final_intervalo, n_elementos)
    
    return ndarray

#exercicio 2
def redimensionar_array(ndarray):
    ndarray.shape = (2,5)
    
    return ndarray
    
def converter_float(ndarray):
    ndarray = ndarray.astype("float")
    
    return ndarray

def transpostas(ndarray):
    np.transpose(ndarray)
    
    return ndarray
    
