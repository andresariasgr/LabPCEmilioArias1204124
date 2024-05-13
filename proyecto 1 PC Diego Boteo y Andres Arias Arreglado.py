import turtle # Importa el módulo turtle para crear gráficos
import time # Importa el módulo time para manejar el tiempo


# Define variables 
class Historia:
    def __init__(self, titulo, color_fondo):
        self.titulo = titulo
        self.secuencias = []
        self.color_fondo = color_fondo

    def agregar_secuencia(self, secuencia):
        self.secuencias.append(secuencia)  # Agrega una nueva secuencia a la lista

    def imprimir_secuencia(self, num_secuencia, tortuga):
        secuencia = self.secuencias[num_secuencia - 1]  # Obtiene la secuencia específica
        titulo = f"Secuencia {num_secuencia}: {secuencia['titulo']}\n"
        narrativa = secuencia['narrativa']
        panel = f"Panel:\n- {secuencia['panel']}\n"
        
        tortuga.clear() # Borra cualquier dibujo anterior en la ventana de la tortuga

        tortuga.penup()
        tortuga.goto(-300, 250)  
        tortuga.write(titulo, font=("Arial", 14, "bold")) # Escribe el título de la secuencia
        tortuga.goto(-300, 200)  

        # Divide el texto narrativo en líneas para que se ajuste en la ventana
        palabras = narrativa.split()
        lineas = []
        linea_actual = ""
        for palabra in palabras:
            if len(linea_actual.split()) < 23:
                linea_actual += palabra + " "
            else:
                lineas.append(linea_actual)
                linea_actual = palabra + " "
        lineas.append(linea_actual)
        for i, linea in enumerate(lineas):
            tortuga.goto(-300, 200 - i * 20 - 20)  
            tortuga.write(linea, font=("Arial", 12, "normal")) # Escribe cada línea en la ventana de la tortuga

        tortuga.goto(-300, -50)  
        tortuga.write(panel, font=("Arial", 12, "normal"))

        self.dibujar_escena(num_secuencia, tortuga)

# Dibuja diferentes escenas según el número de secuencia

    def dibujar_escena(self, num_secuencia, tortuga):
        if num_secuencia == 1:
            
            tortuga.penup()
            tortuga.goto(-100, -250)  
            tortuga.pendown()
            tortuga.circle(50)
            tortuga.penup()
            tortuga.goto(100, -250)  
            tortuga.pendown()
            tortuga.circle(5)
            tortuga.penup()
            tortuga.goto(-120, -350)  
            tortuga.write("Olivia", font=("Arial", 12, "normal"))

        elif num_secuencia == 2:
           
            tortuga.penup()
            tortuga.goto(-200, -250)  
            tortuga.pendown()
            tortuga.circle(50)
            tortuga.penup()
            tortuga.goto(-50, -250)  
            tortuga.pendown()
            tortuga.circle(50)
            tortuga.penup()
            tortuga.goto(100, -250)  
            tortuga.pendown()
            tortuga.circle(50)
            tortuga.penup()
            tortuga.goto(-220, -350)  
            tortuga.write("Olivia", font=("Arial", 12, "normal"))
            tortuga.penup()
            tortuga.goto(-20, -350)  
            tortuga.write("Animales", font=("Arial", 12, "normal"))
            tortuga.penup()
            tortuga.goto(150, -350)  
            tortuga.write("Misterio", font=("Arial", 12, "normal"))

        elif num_secuencia == 3:
            
            tortuga.penup()
            tortuga.goto(-200, -350) 
            tortuga.pendown()
            tortuga.goto(200, -350)  
            tortuga.goto(0, -50)  
            tortuga.penup()
            tortuga.goto(-50, -150)  
            tortuga.pendown()
            tortuga.circle(50)
            tortuga.penup()
            tortuga.goto(-50, -50)  
            tortuga.pendown()
            tortuga.circle(5)
            tortuga.penup()
            tortuga.goto(-70, -370)  
            tortuga.write("Colina", font=("Arial", 12, "normal"))
            tortuga.penup()
            tortuga.goto(-10, 50) 
            tortuga.write("Sol", font=("Arial", 12, "normal"))

        elif num_secuencia == 4:
            
            tortuga.penup()
            tortuga.goto(-150, -250)  
            tortuga.pendown()
            tortuga.circle(50)
            tortuga.penup()
            tortuga.goto(100, -250)  
            tortuga.pendown()
            tortuga.circle(50)
            tortuga.penup()
            tortuga.goto(-170, -350)  
            tortuga.write("Olivia", font=("Arial", 12, "normal"))
            tortuga.penup()
            tortuga.goto(120, -350)  
            tortuga.write("Amigos", font=("Arial", 12, "normal"))

        elif num_secuencia == 5:
            
            tortuga.penup()
            tortuga.goto(0, -250)  
            tortuga.pendown()
            tortuga.circle(100)
            tortuga.penup()
            tortuga.goto(0, -50)  
            tortuga.pendown()
            tortuga.circle(10)
            tortuga.penup()
            tortuga.goto(-50, -450) 
            tortuga.write("Olivia", font=("Arial", 12, "normal"))

def obtener_informacion_usuario():
    nombre = input("Hola, ¿cuál es tu nombre?: ")
    edad = input("¿Cuántos años tienes?: ")
    color_favorito = input("¿Cuál es tu color favorito (Escribelo en ingles)?: ")
    return nombre, edad, color_favorito


nombre, edad, color_favorito = obtener_informacion_usuario()

# Crea una nueva ventana de pantalla con el color de fondo proporcionado

pantalla = turtle.Screen()
pantalla.bgcolor(color_favorito)

historia_olivia = Historia("El Avestruz Curioso", color_favorito)

tortuga = turtle.Turtle()
tortuga.speed(1)

# Define las secuencias de la historia y las agrega a la historia
secuencia1 = {
    'titulo': 'El Descubrimiento',
    'narrativa': "En las vastas llanuras de la sabana africana, vivía un avestruz llamado Olivia. A diferencia de sus compañeros, Olivia era curiosa y siempre buscaba nuevas aventuras. Un día, mientras paseaba por la pradera, encontró un extraño objeto redondo que brillaba bajo el sol. Intrigada, se acercó y descubrió que era un misterioso círculo brillante.",
    'panel': "En el panel, se muestra a Olivia, el avestruz, observando con curiosidad el círculo brillante en medio de la pradera."
}
historia_olivia.agregar_secuencia(secuencia1)

secuencia2 = {
    'titulo': 'El Misterio del Círculo',
    'narrativa': "Olivia se preguntaba qué podría ser ese misterioso círculo. Decidió emprender un viaje para descubrir su origen. Durante su recorrido, conoció a diferentes animales que le hablaron de leyendas y mitos sobre objetos redondos y brillantes. Sin embargo, nadie sabía exactamente de dónde provenía.",
    'panel': "En el panel, se representa a Olivia hablando con otros animales y buscando respuestas sobre el círculo."
}
historia_olivia.agregar_secuencia(secuencia2)

secuencia3 = {
    'titulo': 'La Iluminación',
    'narrativa': "Después de varios días de búsqueda, Olivia llegó a una colina desde donde pudo ver un gran río. Al acercarse, descubrió que el círculo era un reflejo del sol en el agua. ¡El misterio se había resuelto! Estaba feliz y emocionada por haber descubierto la verdad.",
    'panel': "En el panel, se muestra a Olivia llegando a la colina y viendo el reflejo del sol en el río, junto al círculo brillante."
}
historia_olivia.agregar_secuencia(secuencia3)

secuencia4 = {
    'titulo': 'El Regreso',
    'narrativa': "Olivia regresó a su hogar y contó a sus amigos sobre su aventura y el misterioso círculo. Todos quedaron asombrados y admiraron la curiosidad y la determinación de Olivia. Desde entonces, Olivia siempre estuvo dispuesta a aprender cosas nuevas y a explorar el mundo que la rodeaba.",
    'panel': "En el panel, se representa a Olivia contando su historia a sus amigos y todos escuchando atentamente."
}
historia_olivia.agregar_secuencia(secuencia4)

secuencia5 = {
    'titulo': 'El Legado de Olivia',
    'narrativa': "La historia de Olivia se convirtió en una leyenda entre los animales de la sabana. Su curiosidad y su espíritu aventurero inspiraron a muchos a buscar nuevas experiencias y a aprender cosas nuevas. Olivia siempre sería recordada como la avestruz que resolvió el misterio del círculo brillante.",
    'panel': "En el panel, se muestra a Olivia con el círculo brillante en el fondo, simbolizando su aventura y su legado."
}
historia_olivia.agregar_secuencia(secuencia5)

# Itera sobre cada secuencia de la historia e imprime la secuencia con una pausa de 10 segundos entre cada una 

for i in range(1, 6):
    historia_olivia.imprimir_secuencia(i, tortuga)
    time.sleep(10)

turtle.done()
