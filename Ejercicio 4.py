# Crea un programa que almacene en una lista los nombre de tres países que te gustaría visitar. Pide cada país al usuario. Muestra cada país en pantalla en el formato " Me gustaría visitar [país]" reemplazando [país] con cada nombre en la lista.

print("Mensaje de países")
países = []
for i in range(3):
    país = input(f"Ingrese el nombre del país {i+1}: ")
    países.append(país)  
    
for país in países:
    print(f"Me gustaría visitar {país}")    

#Pide al usuario que ingrese una lista de números separados por comas y conviértelos en una lista de enteros. Muestra el número más alto y el número más bajo de la lista.
print("\nLista de números")
numeros_str = input("Ingrese una lista de números separados por comas: ")
numeros_str = numeros_str.split(",")
numeros = []
for numero_str in numeros_str:
    numero = int(numero_str)
    numeros.append(numero)
    
número_más_alto = max(numeros)
número_más_bajo = min(numeros)
print(f"El número más alto es {número_más_alto}")
print(f"El número más bajo es {número_más_bajo}")


