"""
Archivo: mitad_verde.py
-------------------
Dibuja circulos al azar, donde los circulos en la parte superior derecha
son verdes, mientras que el resto son azules.
"""

from graphics import Canvas
import random
import time

# Tamaño del lienzo
ANCHO_LIENZO = 500
ALTO_LIENZO = 500

# El diametro de cada circulo
TAMANO_CIRCULO = 20

# Circulos a dibujar
NUMERO_CIRCULOS = 1000


def main():
    lienzo = Canvas(ANCHO_LIENZO, ALTO_LIENZO)
    lienzo.set_canvas_title("Mitad Verde")

    # Draw 1000
    for i in range(NUMERO_CIRCULOS):
        x = random.randint(0, lienzo.get_canvas_width() - TAMANO_CIRCULO)
        y = random.randint(0, lienzo.get_canvas_height() - TAMANO_CIRCULO)

        circulo = lienzo.create_oval(x, y, x + TAMANO_CIRCULO, y + TAMANO_CIRCULO)

        # Obtiene el color del que deberia ser el circulo
        lienzo.set_color(circulo, obtener_color(x, y))

        lienzo.update()
        time.sleep(0.002)

    lienzo.mainloop()


def obtener_color(x, y):
    """
    Revisa el nombre del color que debería tener el circulo a partir de sus coordenadas
    x, y. Como (0, 0) es la coordenada en la esquina superior izquierda, x empieza a 
    aumentar entre mas nos acerquemos a la derecha, y Y aumenta cuando vamos abajo.
    entonces la linea f(x) = y es la diagonal de la parte superior izquierda hacia
    la parte inferior derecha. Entonces, si y < x, el valor del circulo debería ser
    verde y si no, debería ser azul.
    """
    if x > y:
        return "green"
    return "blue"


if __name__ == "__main__":
    main()
