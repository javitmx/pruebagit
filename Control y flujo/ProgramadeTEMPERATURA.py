# Hacemos un mensaje concatenado
Mensaje ="""ESTO ES UN CORNVERSOR DE TEMPERATURA: 
Usted puede convertir de grados farenheit a grados celsius y a la inversa, Farenheit(N) o Celsius(C)
"""
print(Mensaje)


# capturamos los datos
D = input("elija su opcion: ")

# Hacemos las validaciones:

# Operaciones de la Conversión de farenheit a Celcius
# F = 32 - n /1.8
if D == "N":
    n = input("Ingresa el numero: ")
    F = float((32 - n.isdigit()) / 1.8)
    print(f"la Conversion es: {F}")

elif D == "n":
    n = input("Ingresa el numero: ")
    F = (32 + n.isdigit() /1.8)
    print(f"la Conversion es: {F}")

# Operaciones de la Conversión de Celcius a farenheit
# C = n * 1.8 + 32

elif D == "C":
    n = input("Ingresa el numero: ")
    C = float(n.isdigit() * 1.8 + 32)
    print(f"la Conversion es: {C}")

elif D == "c":
    n = input("Ingresa el numero: ")
    C = float(n.isdigit()* 1.8 + 32)
    print(f"la Conversion es: {C} grados farenheit")

else:
    print("¡Opcion Invalida!: ")


