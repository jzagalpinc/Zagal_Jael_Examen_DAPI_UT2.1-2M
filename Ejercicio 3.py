# Pide al usuario que introduzca un número entero positivo. Si el número es par, muestra el mensaje "[número] es par"; si es impar, muestra "[número] es impar"

print("\nCalculo par o impar")
n = int(input("Introduce un número entero positivo: "))
if n % 2 == 0:
    print(f"{n} es par")
else:
    print(f"{n} es impar")
    

#Solicita al usuario un número entero y genera una lista con todos los múltiplos de 3 hasta el número dado (inclusive). Muestra la lista.

print("\nLista de los múltiplos de 3")
n = int(input("Introduce un número entero: "))
if n % 3 == 0:
    multiplos_de_3 = [i for i in range(1, n+1) if i % 3 == 0]
    print(multiplos_de_3)
else:
    print("El número no tiene multiplos de 3.")





