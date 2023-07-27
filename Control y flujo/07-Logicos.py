#todo lo que escribimos en python termina en una pagina web
#Esta es la validacion mas sencilla que se puede hacer preguntamos si es mayor a 18 
edad = 22 
print(edad > 18 and edad < 30) # en este caso primero ejecuta el primer bloque hasta 18 para ver si es true y luego el de 30 y si el primero es true sigue ejecutando el codigo y si todos son tru pues manda true pero si uno solo es false no sigue ejecutando el codigo, para el operador logico and se ejecuta de izquierda a derecha y solo basta que uno sea falso para que se deje de ejecutar el codigo que esta a la derecha. 
print(edad > 18 or edad < 30)#este operador logico pregunta si el de la izquierda y derecha evalua en true entonces el resultado final es true.
print(not True)#el operador logico de not niega todo el codigo que esta a la derecha

