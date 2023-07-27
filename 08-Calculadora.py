#Declaramos las variables
n1 = input("Ingresa el primer numero: ")
n2 = input("Ingresa el segundo numero: ")#

#le damos el valor en que queremos que se devuelvan los resultados en este caso entero -> integer
n1 = int(n1)
n2 = int(n2)

#hacemos las operaciones que queremos
suma = n1 + n2
resta = n1 - n2
multiplicación = n1 * n2
division = n1 / n2

#hacemos un mensaje concatenandolos con las operaciones de esta manera nos mostrara los resultados
Mensaje = f"""\nEL RESULTADO DE LAS OPERACIONES SON: 5
\nEl Resultado de la suma es {suma}
\nEl resultado de la resta es {resta}
\nEl resultado de la Multiplicación es {multiplicación}
\nEl resultado de la división es {division}
"""
print(Mensaje)
