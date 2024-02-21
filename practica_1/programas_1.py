"""
170995 Ejercicios Lab 1
"""
import random

def problem_1():
    """
    Sum of numbers before
    """
    # get number
    n = int(input("Introduce an integer: "))
    print(f"The sum of all previous is: {(n*(n+1))/2}")


def problem_2():
    """
    Work and time 1.
    """
    # get hours and cost
    horas = int(input("Worked hours rounded to the nearest integer"))
    costo = int(input("cost per hour as a float"))

    print(f"The total is: {horas*costo}")


def problema_3():
    lista = ["Enrique", 20, 0, "Jesus", 20, 0, "Saturn", 20, 0, "Aldo", 20, 0, "Lalo", 20, 0, "Nacho", 20, 0,]
    print([y for x,y in enumerate(lista) if x%3 == 0])


def problem_4():
    """
    Obtener promedio de los numeros pares y el producto de los impares
    """
    # crear lista
    lista = [random.randint(0,100) for _ in range(10)]
    
    # calcular el promedio de pares 
    pares = [x for x in lista if x%2 == 0]
    promedio = sum(pares)/len(pares)

    # calcular el producto de impares
    impares = [x for x in lista if x%2 != 0]
    producto = 1; [producto := producto * x for x in lista]

    print(f"""
        La lista es la siguiente: {lista}.\n
        Los pares son los siguientes: {pares}.\n
        Los impares son los siguients: {impares}.\n
        El promedio es: {promedio}.\n
        El producto es: {producto}.\n
          """)
    

def problem_5():
    """
    Guessing the number.
    """
    # generate random number
    num = random.randint(1,10)

    # loop until the user guesses the number
    ans = -1
    tries = 0

    while ans != num:
        ans = int(input("Try to guess the number from 1-10:\n"))

        # check if higher
        if ans > num:
            print("the number you tried is higher!")
        # check if lower
        elif ans < num:
            print("the number you tried is lower!")
        tries += 1
        
    print(f"you got the number, congrats!, it took you {tries} tries")


def problem_6(length=5, obstacles=5):
    """
    Explorer robot.
    """
    # generate matrix
    matrix = [['o' for _ in range(length)] for _ in range(length)]
    print(matrix)
    
    # add random obstacles
    i = 0
    while i < obstacles:
        x = random.randint(0, length-1)
        y = random.randint(0, length-1)

        if matrix[x][y] == "o" and (x,y) != (length-1, length-1):
            matrix[x][y] = "x"
            i  += 1
    
    # spawn robot
    robot = (0,0)


    

if __name__ == "__main__":
    problem_6()