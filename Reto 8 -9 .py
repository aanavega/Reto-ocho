from math import sin

# Definir funcion para calcular la aproximacion de la funcion seno alrededor de 0
def aproximacionseno(x, n):

# Se inicia en 0 (primer termino de la serie de Maclaurin)
    aproximacion = 0.0

# Definir un bucle que inicia en 0 y calcula el siguiente termino de la serie
    for i in range(0, n + 1):

# Si la variable i es par, se le suma la aproximacion al resultado
        if i%2==0:
            aproximacion += (x**(2*i + 1))/ factorial(2*i+1)
# Si la variable i es impar, se le resta la aproximacion al resultado
        else:
            aproximacion -= (x**(2*i + 1))/ factorial(2*i+1)
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

aproximacion = aproximacionseno(x, n)
valorreal = sin(x)
diferenciavalores = abs(valorreal - aproximacion)

print("La aproximación para " + str(x) + " con " + str(n) + " terminos es: " + str(aproximacion))
print("El valor real es: " + str(valorreal))
print("La diferencia entre el valor real y la aproximacion es: " + str(diferenciavalores))

# Determinar el valor de n para un minimo error
errormaximo = 0.001
n = 1
while abs(sin(x) - aproximacionseno(x, n)) / abs(sin(x)) > errormaximo:
  n += 1

print("El valor mínimo de n para un minimo error del 0.001 es: " + str(n))