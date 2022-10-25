#Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
num_veces = 0
for n in frase:
   if n == letra:
       num_veces = num_veces + 1
print("El numero de veces es ", num_veces)
