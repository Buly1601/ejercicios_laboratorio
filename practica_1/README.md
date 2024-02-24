# Introducción a Python

Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Es conocido por su sintaxis simple y legible, lo que lo hace ideal para principiantes y también poderoso para desarrolladores experimentados. En esta introducción, exploraremos algunos conceptos fundamentales de Python.

## Tipos de variables

En Python, las variables pueden contener diferentes tipos de datos. Algunos de los tipos de variables más comunes incluyen:

- **Enteros (int):** Números enteros, como 5 o -3.
- **Flotantes (float):** Números decimales, como 3.14 o -0.001.
- **Cadenas (str):** Secuencias de caracteres, como "hola" o "Python".
- **Booleanos (bool):** Valores verdaderos o falsos, True o False.

## Estructura de un bucle 'for'

Un bucle `for` en Python se utiliza para iterar sobre una secuencia (como una lista, tupla, o rango) o cualquier objeto iterable. La estructura básica de un bucle `for` es la siguiente:

```python
for elemento in secuencia:
    # Código a ejecutar en cada iteración
```

## Estructura de un bucle 'while'

Un bucle `while` se utiliza para repetir un bloque de código mientras se cumpla una condición específica. La estructura básica de un bucle `while` es la siguiente:

```python
while condicion:
    # Código a ejecutar mientras se cumpla la condición
```

## Listas

Las listas en Python son colecciones ordenadas y mutables de elementos. Pueden contener elementos de diferentes tipos y se definen utilizando corchetes `[]`. Algunas operaciones comunes con listas incluyen agregar elementos, eliminar elementos, y acceder a elementos por índice.

```python
mi_lista = [1, 2, 3, "hola", True]
```

## Operadores

Python admite una variedad de operadores para realizar diferentes tipos de operaciones. Algunos de los operadores más comunes incluyen:

- **Aritméticos:** `+`, `-`, `*`, `/`, `//` (división entera), `%` (módulo).
- **Comparación:** `==`, `!=`, `<`, `>`, `<=`, `>=`.
- **Lógicos:** `and`, `or`, `not`.
- **Asignación:** `=`, `+=`, `-=`.

## Sentencia 'if' - 'else'

La sentencia `if` se utiliza para ejecutar un bloque de código si se cumple una condición específica. La sentencia `else` se utiliza para ejecutar un bloque de código si la condición del `if` no se cumple. La estructura básica es la siguiente:

```python
if condicion:
    # Código a ejecutar si la condición es verdadera
else:
    # Código a ejecutar si la condición es falsa
```
## Explicación del código
En este apartado se explicará la dinámica e idea de los programas escritos.

### Programa 1: Suma de números.
Para este programa, se usó la fórumula para sumar los números anteriores: `(n*(n+1))/2`. Por lo tanto, se usa un `print(f"")` para concatenar datos del tipo `string` con datos del tipo `int`.

### Programa 2: Costo por hora.
Para este programa, se tiene que calcular el costo de horas trabajadas. Se le pide al usuario datos que se tienen que convertir a int de la siguiente forma: `x = int(input("texto a imprimir")`. Después se multiplican las horas y el costo por hora para imprimir el resultado.

### Programa 3: Trabajadores y salarios 
Para este programa, se tiene que imprimir datos de una lista que contiene los nombres de los trabajadores, sus horas de trabajo y su salario por hora. Para ello, se crea previamente una lista, sabiendo que los nombres están en los lugares que son múltiplos de 3, dentro de un ciclo `for`, para obtener los índices y los valores, se usa la siguiente sintaxis: `for x,y in enumerate(lista)`. Una vez se obtiene el nombre, se imprime, y se multiplican las horas por el salario, para después volver el valor del salario a 1.

### Programa 4: Promedio y producto
Para este programa, se tiene una lista con 100 números aleatorios, dicha lista se declara usando el método `randint` la librería `random` de la siguiente forma: `[random.randint(0,100) for _ in range(10)]`. Una vez se tiene la lista, usando el operador `%`, se busca saber si es par o impar de la siguiente forma: `if x % 2 == 0`. Al tener una lista de pares y otra de impares, se suma la lisa de pares y se divide entre su tamaño, y la de impares se multiplica por las impares.

### Programa 5: Adivinando el número
Para este programa, el objetivo es iniciar con un número aleatorio del 1-10 usando `random.randint(1,10)`. Una vez hecho, se declaran dos variables, `ans = -1` y `count = 0`, se usa un bucle `while` para ciclar en lo que la variable "ans" no sea igual al resultado, ans se sobreescribe por cada iteración por el número nuevo del usuario usando `ans = input("texto")`. Si el número adivinado es mayor al real o menor, se dan pistas acorde usando un `if - else`.

### Programa 6: Robot 
Para este programa, se tiene que declarar una lista de listas de largo `length` cuyo valor predeterminado es 5 (modificable al llamar la función), usando: `matrix = [['o' for _ in range(length)] for _ in range(length)]`. Una vez se tiene la matriz, se tiene que crear obstáculos, la cantidad de obstáculos son el largo de la lista, es decir `length`, las dos resticciones es que no pueden haber obstáculos en la entrada ni en la salida del laberinto, usando:

```python
    # add random obstacles
    i = 0
    while i < obstacles:
        x = random.randint(0, length-1)
        y = random.randint(0, length-1)

        if matrix[x][y] == "o" and (x,y) != (length-1, length-1):
            matrix[x][y] = "x"
            i  += 1
```
Una vez el laberinto está terminado, se crea el robot en `[0,0]`. y se declaran sus posibles movimientos en una lista de la siguiente forma: `directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]`. Ya que se sabe por donde se puede mover, se busca uno de los posibles movimientos, dentro de un bucle `for`, si este no entra en el caso, y por ende no rompe el bucle usando `break`, entonces significa que no se puede mover y no hay una posible salida a este problema (cabe recalcar que no se usó un algoritmo de IA para resolverlo, solo no puede volver por donde ha pasado). Si es que el `break` se activa, el bucle `while` continúa y por lo tanto, no se genera un error. Al final se imprime la matriz con los puntos por los que pasó el robot usando unicode: `unicodes = ['\u2192', '\u2193', '\u2190', '\u2191']`.
