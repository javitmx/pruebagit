#Mensaje explicativo del programa
mensaje = """Este es un programa de Temperatura:
este programa toma los valores de Farenheit y los convierte a Celsius y viseversa,\ncualquiere convertir? Farenheit(N) o Celsius(C).
"""
print(mensaje)

#Recolectamos los datos del usuario
Escala = input("Digite su opcion: ").upper()
Temperatura = float(input("Digite los grados: "))

#Hacemos las operaciones devidas
if Escala == "N":
    operacion = (Temperatura - 32) / 1.8
    print(operacion)

elif Escala == "C":
    operacionC = Temperatura * 1.8 + 32
    print(operacionC)

else:
    print("¡Opcion Invalida!")
