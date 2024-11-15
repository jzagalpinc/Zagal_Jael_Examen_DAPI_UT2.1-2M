# Define una función "area_cuadrado(lado)" que calcule el area de un cuadrado con uno de sus lado. Después, el usuario ingresa la longitud de un lado y el programa devuelve el área del  cuadrado respecto longitud ingresada por el usuario.

def area_cuadrado(lado):
    return lado**2

print("\nCalculo área de un cuadrado")
lado = float(input("Ingrese el lado del cuadrado: "))
area = area_cuadrado(lado)
print(f"El área del cuadrado es: {area}")
    
# Define una función mayor_de_tres(a, b, c) que reciba tres números y devuelva el mayor de ellos. Después, en el programa principal, el usuario ingresa tres números, llama a la función y el programa muestra el número mayor.

def mayor_de_tres(a, b, c):
    return max(a, b, c)

print("\nCalculo del mayor de tres numeros")
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
mayor = mayor_de_tres(a, b, c)
print("El número mayor es:", mayor)
    