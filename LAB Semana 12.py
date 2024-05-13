print(" Semana No.12: Ejercicio 1")

print("Menu", "a sumatoria", 
"b. factorial", 
"c. Tablas de muiltiplicacion", 
"d. Número perfecto", 
sep= "\n")

opcion= input("Ingrese su opción: ")

match opcion: 
    case "a":
        n = int(input("Ingrese un número entero postivo:  "))

        if (n<= 0):
            print("Error, ingrese un número entero positivo")

        else: 

            sumatoria = 0
            for contador in range(1, n+1): 
                sumatoria += contador
                print(f"La sumatoria es: {sumatoria}") 
    case "b":
        print("tarea")
    case "c":
        tituloCol= "\t"
        #Imprimir titulo de columnas 
        for col in range(1, 11): 
            tituloCol += str(col) + "\t"

        print(tituloCol)

        #Imprimir filas 
        textoFila= ""
        for fila in range (1, 11):
            textoFila = str(fila) + "\t"
           
            for col in range (1, 11): 
                textoFila += str(fila * col)+ "\t"

            print(textoFila)
    case "d": 
        numero= int(input("ingrese un numero entero: "))
        if( numero<= 0):
            print("numero no valido")
        else:  
                resultado=numero//numero
print(resultado)