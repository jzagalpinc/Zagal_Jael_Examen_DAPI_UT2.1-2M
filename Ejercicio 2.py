# Pide al usuario su nombre completo en formato Nombre Apellido y almacénalo en una variable. Muestra solo el primer nombre extrayendo la parte antes del espacio

print("\nNombre principal")
nombre_completo = input("Ingrese su nombre completo: ")
nombre = nombre_completo.split()[0]
print("Nombre:", nombre)

# Pide al usuario un número entero y muestra si es un número primo o no.

print("\nTe digo si un número es primo")
print("\nNúmero primo")
num = int(input("Ingrese un número entero: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "no es un número primo")
            break


# Solicita al usuario una palabra y una vocal, y luego reemplaza todas las apariciones de esa vocal en la palabra con su versión en mayúcula. Muestra el resultado.
print("\nReemplazador de vocal por mayúscula")
palabra = input("Ingrese una palabra: ")
vocal = input("Ingrese una vocal: ")
nueva_palabra = palabra.replace(vocal.lower(), vocal.upper())
print("Nueva palabra:", nueva_palabra)

