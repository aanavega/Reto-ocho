from math import atan

# Definir funcion para calcular la aproximacion de la funcion arcotangentel alrededor de 0
def aproximacionarcotan(x, n):

# Se inicia en 0 (primer termino de la serie de Maclaurin)
    aproximacion = 0.0

# Definir un bucle que inicia en 1 y calcula el siguiente termino de la serie
    for i in range(1, n + 1):
        aproximacion += ((-1)**(i+1))*(x**(2*i+1))/(2*i+1)
    return aproximacion

# Definir funcion para determinar el valor de n para un minimo error
def errormaximo(x, errormaximo):
    n = 1
    while diferenciavalores > errormaximo:
      n += 1
    return n

# Definir variables (un valor real x y la cantidad de terminos de la serie n)
x = 1
n = 2

# Definir el error maximo
errormaximo = 0.001

aproximacion = aproximacionarcotan(x, n)
valorreal = atan(x)
diferenciavalores = abs(valorreal - aproximacion)

print("La aproximación para " + str(x) + " con " + str(n) + " terminos es: " + str(aproximacion))
print("El valor real es: " + str(valorreal))
print("La diferencia entre el valor real y la aproximacion es: " + str(diferenciavalores))
print("El valor mínimo de n para un minimo error del 0.001 es: " + str(n))


