import numpy as np
import numpy.random as npr

def gerar_ndarray (inicio_intervalo, final_intervalo, n_elementos):
    ndarray = npr.randint(inicio_intervalo, final_intervalo, n_elementos)
    
    return ndarray