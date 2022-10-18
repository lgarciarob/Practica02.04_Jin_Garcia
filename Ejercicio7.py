#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
num = int(input("Introduce un número entero:\n"))
for triangulo in range(num):
    print("*" * (triangulo + 1))