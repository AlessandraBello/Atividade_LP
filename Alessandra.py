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

#exercicio 4
def ex_4(inicio_intervalo, final_intervalo, n_elementos):
    array5 = npr.randint(inicio_intervalo, final_intervalo, n_elementos)
    array6 = npr.randint(inicio_intervalo, final_intervalo, n_elementos)
    print(array5)
    print(array6)
    
    lista_de_elementos = []
    for elemento1 in array5:
        for elemento2 in array6:
            if elemento1 == elemento2 and elemento1 not in lista_de_elementos:
                lista_de_elementos.append(elemento1)
    print(lista_de_elementos)
                
    lista_de_indices1 =[]
    lista_de_indices2 =[]
    for indice1 in range(array5.size):
        for indice2 in range(array6.size):
            if array5[indice1] == array6[indice2]:
                lista_de_indices1.append(indice1)
                lista_de_indices2.append(indice2)
    print(lista_de_indices1, lista_de_indices2)  

    elementos_unicos =[]
    for elemento in array5:
        if elemento not in lista_de_elementos:
            elementos_unicos.append(elemento)
    print(elementos_unicos)

    return (array5, array6)
