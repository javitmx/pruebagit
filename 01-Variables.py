# nombre = "Alberto"

# primera forma pero no es optimo de concatenar variables
# concatenacion = "hola " + nombre + " como estas." 
#print(concatenacion)

#CamelCase es una forma de escribir las variables, y se basa en colocar mayusculas en las iniciales de la palabra.
OtroNombre = "Hector"
#Snake_case es otra forma de escribir variables pero de manera o forma de serpiente es decir con guiones bajos para separar o identificar las palabras
Otro_Nombre =  "Javi"


nombre =  False #sea lo que colocamos siempre lo convierte en manera de string

#segunda forma pero mas optima de concatenar variables utilizando el operador ternario
concatenacion = f"hola  {nombre}  como estas." 
print(concatenacion)

#Operadores de pertenencia (in / not in)
print("luca" in concatenacion)#manera de buscar dentro de una variable
print("luca" not in concatenacion)
 