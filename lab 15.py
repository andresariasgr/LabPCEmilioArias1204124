# Actividad 01
def area_triangulo(base, altura):
    return (base * altura) / 2

def area_cuadrado(lado):
    return lado * lado
def area_rectangulo(base, altura):
    return base * altura


import math
def area_circulo(radio):
    return math.pi * radio**2


print("Semana No. 12: Ejercicio 1")


print("Seleccione la opción que desea calcular:")
print("a. Área de triángulo")
print("b. Área de cuadrado")
print("c. Área de rectángulo")
print("d. Área de círculo")


opcion = input("Ingrese la opción (a, b, c o d): ")


if opcion == "a":
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    print("El área del triángulo es:", area_triangulo(base, altura))
elif opcion == "b":
    lado = float(input("Ingrese el lado del cuadrado: "))
    print("El área del cuadrado es:", area_cuadrado(lado))
elif opcion == "c":
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    print("El área del rectángulo es:", area_rectangulo(base, altura))
elif opcion == "d":
    radio = float(input("Ingrese el radio del círculo: "))
    print("El área del círculo es:", area_circulo(radio))
else:
    print("Opción no válida")

#Actividad 02
X = 0
Y = 0


def MoverHaciaArriba():
    global Y
    Y += 1

def MoverHaciaAbajo():
    global Y
    Y -= 1

def MoverHaciaLaDerecha():
    global X
    X += 1


def MoverHaciaLaIzquierda():
    global X
    X -= 1

print("Semana No. 12: Ejercicio 2")

while True:
    
    print("\nSeleccione una opción:")
    print("a. Sube")
    print("b. Baja")
    print("c. Izquierda")
    print("d. Derecha")
    print("e. Salir")

  
    opcion = input("Ingrese la opción: ")

    
    if opcion == "a":
        MoverHaciaArriba()
    elif opcion == "b":
        MoverHaciaAbajo()
    elif opcion == "c":
        MoverHaciaLaIzquierda()
    elif opcion == "d":
        MoverHaciaLaDerecha()
    elif opcion == "e":
        
        print("Coordenadas finales del personaje:", X, ",", Y)
        break
    else:
        print("Opción no válida. Intente de nuevo.")
