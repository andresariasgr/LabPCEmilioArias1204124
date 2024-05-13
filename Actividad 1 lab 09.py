metros = input("Ingrese la cantidad en metros: ")

metros = int(metros)


millas = metros / 1609.34
kilometros = metros / 1000
pies = metros * 3.28
pulgadas = metros * 39.37


print(metros, "metros son:")
print(millas - (millas % 0.01), "millas")
print(kilometros - (kilometros % 0.01), "kilómetros")
print(pies - (pies % 0.01), "pies")
print(pulgadas - (pulgadas % 0.01),"pulgadas")