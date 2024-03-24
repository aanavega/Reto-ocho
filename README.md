# Reto-ocho

### Codigo numero 1

- Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```Python

# Definimos el rango de los numeros cuyos cuadradados encontraremos
for i in range(1, 101):
    cuadrado = i**2
    print("El numero " + str(i) + " elevado al cuadrado es: " + str(cuadrado))

```

### Codigo numero 2

- Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

```Python

# Definimos el rango de los numeros impares (de 1 a 999, de 2 en 2)
for i in range(1, 1000, 2):
    print("Numeros impares: " + str(i))

# Definimos el rango de los numeros pares (de 2 a 1000, de 2 en 2)
for i in range(2, 1001, 2):
    print("Numeros pares: " + str(i))

```

### Codigo numero 3

- Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado.

```Python
# Definir desde que valor se evaluara la condicion
n: int = 50

# Definir la condicion del bucle
while n >= 2:
    if n % 2 == 0:
        print(n)
    n -= 2
    print(str(n))
```

### Codigo numero 4

- Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.

```Python
# Leer un numero natural
n = int(input("Ingrese un numero natural: "))

# Definimos el rango para el numero natural
factorial : int = 1
for i in range(1, n+1):
  factorial *= i
print("El factorial del numeroo " + str(n) + " es " + str(factorial))
```

### Codigo numero 5

- Calcular el valor de 2 elevado a la potencia n usando ciclos for.

```Python
# Leer un numero de potencia para dos
n = int(input("Ingrese numero de potencia: "))

# Definir el rango en el que se evaluara 2 elevado a la potencia dada
for i in range(1, n+1):
    i = 2**n
print("La potencia de 2 elevado a " +str(n) + " es: " + str(i))
```

### Codigo numero 6

- Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).

```Python

# Definir ambas variables, un numero natural y un numero real
n = int(input("Ingrese un número natural: "))
x = float(input("Ingrese un real: "))

# Definir la operacion a aplicar con ambas variables
potencia = 1

# Definir el rango de la operacion
for _ in range(n):
  potencia *= x
print("El numero real " + str(x) + " elevado al numero natural " + str(n) + " es: " + str(potencia))
```

### Codigo numero 7

- Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

```Python
# Se define la primera variable, tabla de multiplicar para el numero 1
n: int = 1

print("La tabla del numero " +str(n) + " es: ")

# Definir el rango del bucle, de 1 a 10, se repite 10 veces
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))

# Se define la segunda variable, tabla de multiplicar para el numero 2
n: int = 2

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))

# Se define la tercera variable, tabla de multiplicar para el numero 3
n: int = 3

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))

# Se define la cuarta variable, tabla de multiplicar para el numero 4
n: int = 4

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))

# Se define la quinta variable, tabla de multiplicar para el numero 5
n: int = 5

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))

# Se define la sexta variable, tabla de multiplicar para el numero 6
n: int = 6

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))

# Se define la septima variable, tabla de multiplicar para el numero 7
n: int = 7

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))

# Se define la octaba variable, tabla de multiplicar para el numero 8
n: int = 8

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))

# Se define la novena variable, tabla de multiplicar para el numero 9
n: int = 9

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))
```

### Codigo numero 8

- Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación. 

```Python
from math import exp

# Definir funcion para calcular la aproximacion de la funcion exponencial alrededor de 0
def aproximacionexpo(x, n):

# Se inicia en 1 (primer termino de la serie de Maclaurin)
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
```

### Codigo numero 9

- Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

```Python
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
```

### Codigo numero 10

- Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

```Python

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

```

