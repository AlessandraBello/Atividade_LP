import numpy as np
import numpy.random as npr

#exercicio 1
def gerar_ndarray (inicio_intervalo, final_intervalo, n_elementos):
    ndarray = npr.randint(inicio_intervalo, final_intervalo, n_elementos)
    
    return ndarray
def somar (array_1, array_2):
    novo_array = array_1+array_2

    return novo_array
    
#exercicio 2
def redimensionar_array(ndarray,  n_linhas, n_colunas):
    ndarray.shape = ( n_linhas, n_colunas)
    
    return ndarray
    
def converter_float(ndarray):
    ndarray = ndarray.astype("float")
    
    return ndarray

def transpostas(ndarray):
    ndarray = np.transpose(ndarray)
    
    return ndarray

#exercicio 3
def multiplicar (ndarray_1, ndarray_2):
    multiplicado = ndarray_1* ndarray_2

    return multiplicado
