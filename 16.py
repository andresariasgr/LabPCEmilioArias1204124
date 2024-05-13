import random


print("Semana No. 16: Ejercicio 1")


numeros = [random.randint(1, 100) for _ in range(10)]


print("\nNúmeros:")
print(numeros)  

promedio = sum(numeros) / len(numeros)
print(f"Promedio: {promedio:.2f}")  

print(f"Longitud: {len(numeros)}")  


suma_pares = sum(numeros[i] for i in range(len(numeros)) if i % 2 == 0)
print(f"Suma de posiciones pares: {suma_pares}")  

suma_impares = sum(numeros[i] for i in range(len(numeros)) if i % 2 != 0)
print(f"Suma de posiciones impares: {suma_impares}")  




import random

print("Semana No. 16: Ejercicio 2")

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = [[random.randint(0, 1000) for _ in range(columnas)] for _ in range(filas)]


print("\nMatriz:")
for fila in matriz:
    print(fila)

pares = 0
impares = 0
mayor = matriz[0][0]
menor = matriz[0][0]

for fila in matriz:
    for num in fila:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num

print(f"\nEstadísticas:\n")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Número mayor: {mayor}")
print(f"Número menor: {menor}")