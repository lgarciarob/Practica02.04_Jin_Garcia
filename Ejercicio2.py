#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
n = float(input("Introduce dividendo:\n"))
m = float(input("Introduce divisor:\n"))
if 0 == m:
    print("error")
else:
    print(n / m)