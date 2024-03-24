from math import exp

# Definir funcion para calcular la aproximacion de la funcion exponencial alrededor de 0
def aproximacionexpo(x, n):

# Primero se calculo el valor de 1 (primer termino de la serie de Maclaurin)
  aproximacion = 1.0

# Definir un bucle que inicia en 1 y calcula el siguiente termino de la serie
  for i in range(1, n + 1):

# Sumar el valor del bucle a la aproximacion
    aproximacion += (x**i) / factorial(i)
  return aproximacion

# Definir funcion para calcular el factorial de un numero
def factorial(n):

  if n == 0:
    return 1
  else:
    return n*factorial(n-1)

# Definir variables (un valor real x y la cantidad de terminos de la serie n)
x = 2.5
n = 3

aproximacion = aproximacionexpo(x, n)
valorreal = exp(x)
diferenciavalores = abs(valorreal - aproximacion)

print(" La aproximación para " + str(x) + " con " + str(n) + " terminos es: " + str(aproximacion))
print("El valor real es: " + str(valorreal))
print("La diferencia entre el valor real y la aproximacion es: " + str(diferenciavalores))

# Determinar el valor de n para un minimo error
errormaximo = 0.001
n = 1
while abs(exp(x) - aproximacionexpo(x, n)) / abs(exp(x)) > errormaximo:
  n += 1

print("El valor mínimo de n para un minimo error del 0.001 es: " + str(n))
