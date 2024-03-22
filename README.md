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
n = int(input("Ingrese el numero natural 1: "))

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))


n = int(input("Ingrese el numero natural 2: "))

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))


n = int(input("Ingrese el numero natural 3: "))

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))


n = int(input("Ingrese el numero natural 4: "))

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))



n = int(input("Ingrese el numero natural 5: "))

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))


n = int(input("Ingrese el numero natural 6: "))

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))


n = int(input("Ingrese el numero natural 7: "))

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))


n = int(input("Ingrese el numero natural 8: "))

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))


n = int(input("Ingrese el numero natural 9: "))

print("La tabla del numero " +str(n) + " es: ")
for i in range(1, 11):
    producto = n*i
    print(str(n) + "x" + str(i) + "=" + str(producto))
```

### Codigo numero 8
