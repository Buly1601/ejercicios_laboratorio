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


def problem_3():
    """
    Get name and salary for every worker.
    """
    # create list
    list = ["Enrique", 20, 2, "Jesus", 20, 5, "Saturn", 20, 6, "Aldo", 20, 9, "Lalo", 20, 8, "Nacho", 20, 1]
    
    # get names an salaries
    names = [y for x,y in enumerate(list) if x%3 == 0]
    i = 0
    salary = 1
    for x,y in enumerate(list):
        if x%3 != 0:
            salary *= y
        else:
            print(f"The salary for {names[i]} is {salary}")
            i += 1
            salary = 1
            

def problem_4():
    """
    Get median of the pair nums and product of odd
    """
    # create list
    list = [random.randint(0,100) for _ in range(10)]
    
    # calcular el promedio de pares 
    pair = [x for x in list if x%2 == 0]
    median = sum(pair)/len(pair)

    # calcular el producto de impares
    odd = [x for x in list if x%2 != 0]
    product = 1; [product := product * x for x in list]

    print(f"""
        La lista es la siguiente: {list}.\n
        Los pares son los siguientes: {pair}.\n
        Los impares son los siguients: {odd}.\n
        El promedio es: {median}.\n
        El producto es: {product}.\n
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
    Robot can only move down, left or right
    """
    # generate matrix
    matrix = [['o' for _ in range(length)] for _ in range(length)]
    
    # create unicode list
    unicodes = ['\u2192', '\u2193', '\u2190', '\u2191']
    # add random obstacles
    i = 0
    while i < obstacles:
        x = random.randint(0, length-1)
        y = random.randint(0, length-1)

        if matrix[x][y] == "o" and (x,y) != (length-1, length-1):
            matrix[x][y] = "x"
            i  += 1

    # right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    # starting position
    row, col = 0, 0  
    while (row, col) != (length-1, length-1):
        for i,direction in enumerate(directions):
            new_row = row + direction[0]
            new_col = col + direction[1]
            if 0 <= new_row < length and 0 <= new_col < length and matrix[new_row][new_col] == 'o':
                row, col = new_row, new_col
                # mark with arrows
                matrix[row][col] = unicodes[i]  # marking the path of the robot
                break
        else:
            print("Destiny unreachable")
            break
    
    # marking the final destination
    matrix[row][col] = 'R'  
    # mark initial position with r
    matrix[0][0] = "R"
    
    # print
    print("Robot's path: \n")
    for row in matrix:
        print(row)

if __name__ == "__main__":
    problem_6()