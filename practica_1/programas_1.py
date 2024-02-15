"""
170995 Ejercicios Lab 1
"""
def problema1():
    n = int(input("introduzca numero entero positivo: "))
    print((n*(n+1))/2)


def problema2():
    horas = int(input("horas trabajadas redondeadas al entero"))
    costo = int(input("costo por hora en flotante"))

    print(f"Tu total es: {horas*costo}")


def problema3():
    lista = ["Enrique", 20, 0, "Jesus", 20, 0, "Saturn", 20, 0, "Aldo", 20, 0, "Lalo", 20, 0, "Nacho", 20, 0,]
    print([y for x,y in enumerate(lista) if x%3 == 0])



if __name__ == "__main__":
    problema3()