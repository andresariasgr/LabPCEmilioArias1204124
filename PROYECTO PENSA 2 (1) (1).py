class TableroAjedrez:
    def __init__(self):                  #Inicia el tamaño del tablero y crea una matriz.
        self.tamano = 8
        self.tamano = 8
        self.tablero = [[' ' for _ in range(self.tamano)] for _ in range(self.tamano)]

    def mostrartablero(self):          #Muestra el tablero de ajedrez con las piezaz.
        print("Matriz del tablero:")
        print("  a b c d e f g h")
        print(" ♥-----------------♥")
        for i, fila in enumerate(self.tablero):
            print(f"{i + 1}|{'|'.join(fila)}|")
            if i < self.tamano - 1:
                print("  ♥-----------------♥")
        print(" ♥-----------------♥")

    def colocarpieza(self, fila, columna, pieza):     #Coloca una pieza en una posición del tablero de ajedrez.
        self.tablero[fila][columna] = pieza

    def obtenerpieza(self, fila, columna):         #Obtiene la pieza en una posición del tablero ajedrez.
        return self.tablero[fila][columna]

    def validarposicion(self, fila, columna):
        return 0 <= fila < self.tamano and 0 <= columna < self.tamano and self.tablero[fila][columna] == ' '   #Verifica si una posición en el tablero es válida y no está ocupada por otra pieza.

    def obtenermovimientoscaballo(self, fila, columna):    #Calcula los movimientos válidos de un caballo en una posiciopn que dio el usuario.
        movimientosposibles = [
            (fila + 2, columna + 1), (fila + 2, columna - 1),
            (fila - 2, columna + 1), (fila - 2, columna - 1),
            (fila + 1, columna + 2), (fila + 1, columna - 2),
            (fila - 1, columna + 2), (fila - 1, columna - 2)
        ]
        movimientosvalidos = []
        for nuevafila, nuevacolumna in movimientosposibles:
            if 0 <= nuevafila < self.tamano and 0 <= nuevacolumna < self.tamano:
                movimientosvalidos.append((nuevafila, nuevacolumna))
        return movimientosvalidos


def main():
    tablero = TableroAjedrez()     #Crea Tablero ajedrez
 
    posicioncaballo = input("Ingrese la posición del caballo a evaluar (ejemplo: a1): ").strip().lower()     # Solicita al usuario la posición del caballo
    if len(posicioncaballo) != 2 or not ('a' <= posicioncaballo[0] <= 'h') or not ('1' <= posicioncaballo[1] <= '8'):     #Verifica si la posición es válida
        print("Posición inválida. Intente nuevamente.")
        return

    columnacaballo = ord(posicioncaballo[0]) - ord('a')    #Convierte la posición a coordenada en la matriz
    filacaballo = int(posicioncaballo[1]) - 1

    if tablero.validarposicion(filacaballo, columnacaballo):     #Coloca el caballo en el tablero si es que la posicion es valida
        tablero.colocarpieza(filacaballo, columnacaballo, 'C')
    else:
        print("Posición inválida o ya ocupada. Intente nuevamente.")
        return

    numpiezas = int(input("Ingrese la cantidad de piezas a colocar en el tablero (además del caballo): "))     #Solicita la cantidad y posicion de las otras piezas
    for _ in range(numpiezas):           #Solicita tipo, color y posición de la piezas que ingreso el usuario
        tipopieza = input("Ingrese el tipo de pieza (alfil, peón, caballo, torre, rey, reina): ").strip().lower()
        colorpieza = input("Ingrese el color de la pieza (blanco/negro): ").strip().lower()
        posicion = input("Ingrese la posición de la pieza (ejemplo: a1): ").strip().lower()

        if tipopieza not in ["alfil", "peón", "caballo", "torre", "rey", "reina"]:    #Verifica la validez 
            print("Tipo de pieza inválido. Intente nuevamente.")
            continue

        if colorpieza not in ["blanco", "negro"]:
            print("Color de pieza inválido. Intente nuevamente.")
            continue

        if len(posicion) != 2 or not ('a' <= posicion[0] <= 'h') or not ('1' <= posicion[1] <= '8'):
            print("Posición inválida. Intente nuevamente.")
            continue

        columna = ord(posicion[0]) - ord('a')     #Convierte la posicio a coordenada en la matriz
        fila = int(posicion[1]) - 1

        if tablero.validarposicion(fila, columna):                      #Coloca la pieza en el tablero si es que es valida
            pieza = f"{colorpieza[0].upper()}{tipopieza[0].upper()}"
            tablero.colocarpieza(fila, columna, pieza)
        else:
            print("Posición inválida o ya ocupada. Intente nuevamente.")

    movimientoscaballo = tablero.obtenermovimientoscaballo(filacaballo, columnacaballo)     #Obtiene y muestra los movimientos validos del caballo
    print("\nMovimientos válidos del caballo:")
    for filamov, colmov in movimientoscaballo:
        pieza = tablero.obtenerpieza(filamov, colmov)
        if pieza == ' ':
            print(f"{chr(colmov + ord('a'))}{filamov + 1} - Casilla vacía")
        elif pieza[0] != 'C':
            print(f"{chr(colmov + ord('a'))}{filamov + 1} - {pieza}")

    print("\nTablero:")       #Muestra el tablero con las piezas 
    tablero.mostrartablero()


if __name__ == "__main__":
    main()
