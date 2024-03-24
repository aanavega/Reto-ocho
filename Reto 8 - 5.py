# Leer un numero de potencia para dos
n = int(input("Ingrese numero de potencia: "))

# Definir el rango en el que se evaluara 2 elevado a la potencia dada
for i in range(1, n+1):
    i = 2**n
print("La potencia de 2 elevado a " +str(n) + " es: " + str(i))