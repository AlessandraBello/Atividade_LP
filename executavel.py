import Alessandra 

#exercicio 1

array1 = Alessandra.gerar_ndarray(0,100,10)
array2 = Alessandra.gerar_ndarray(0,100,10)

array3 = Alessandra.somar(array1, array2)

#exercicio 2 
array3 = Alessandra.redimensionar_array (array3, 2,5)

array3 = Alessandra.converter_float(array3)

array3 = Alessandra.transpostas(array3)

#exercicio3

array4 = Alessandra.gerar_ndarray(0,100,10)

array4 = Alessandra.redimensionar_array (array4, 5, 2)

array4 = Alessandra.multiplicar(array3, array4)

#execicio 4
exercicio4 = Alessandra.ex_4(0,10,6)
print (array1)
print (array2)
print (array3)
print (array4)
print (exercicio4)
