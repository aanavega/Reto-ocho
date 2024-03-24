# Leer un numero natural
n = int(input("Ingrese un numero natural: "))

# Definimos el rango para el numero natural
factorial : int = 1
for i in range(1, n+1):
  factorial *= i
print("El factorial del numeroo " + str(n) + " es " + str(factorial))