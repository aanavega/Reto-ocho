# Definir ambas variables, un numero natural y un numero real
n = int(input("Ingrese un número natural: "))
x = float(input("Ingrese un real: "))

# Definir la operacion a aplicar con ambas variables
potencia = 1

# Definir el rango de la operacion
for _ in range(n):
  potencia *= x
print("El numero real " + str(x) + " elevado al numero natural " + str(n) + " es: " + str(potencia))
