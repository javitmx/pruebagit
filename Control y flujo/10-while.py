#                                """BUCLE WHILE"""
Lenguajes = ["python", "ruby", "php", "java","C++","swift"] #siempre se inicia desde indice 0 hasta el final de la lista

i = 1
while i <= 9:
    print(i)
    i = i + 1
 
i = 1
while i <= 9:
    print(i, * "Anonymous ")
    i = i + 1
 
#y asi accedemos a cada uno de los elemntos de un listado.
i = 0
while i < len(Lenguajes):
    print((Lenguajes)[i])
    i = i + 1
 
 