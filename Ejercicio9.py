numero = int(input("Introduzca un numero entero: "))
for piramide in range(1, numero+1, 2):
   for numero_fila in range(piramide, 0, -2):
       print(numero_fila, end= " ")
   print("")
