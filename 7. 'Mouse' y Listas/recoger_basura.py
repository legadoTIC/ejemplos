"""
File: debris_sweeper.py
-------------------
Puts a random collection of debris (ovals) on the screen
and then allows the user to click and remove the debris.
"""

from graphics import Canvas
import random

# tamaños minimo y maximo de las piezas
TAMANO_MINIMO = 50
TAMANO_MAXIMO = 150

# numero de piezas de basura
PIEZAS_DE_BASURA = 2


def main():
    lienzo = Canvas()
    lienzo.set_canvas_title("Recoger Basura")

    crear_basura(lienzo)
    while True:
        clicks = lienzo.get_new_mouse_clicks()
        for click in clicks:
            eliminar_basura(lienzo, click.x, click.y)
        lienzo.update()

    lienzo.mainloop()


def crear_basura(lienzo):
    """
    Crea un numero fijo de piezas de 'basura' para recolectarse
    """
    for i in range(PIEZAS_DE_BASURA):
        # Calcula una posicion y tamaño aleatorio
        ancho = random.randint(TAMANO_MINIMO, TAMANO_MAXIMO)
        alto = random.randint(TAMANO_MINIMO, TAMANO_MAXIMO)
        x = random.randint(0, lienzo.get_canvas_width() - ancho)
        y = random.randint(0, lienzo.get_canvas_height() - alto)

        # Crea la pieza con un color aleatorio
        pieza = lienzo.create_oval(x, y, x + ancho, y + alto)
        lienzo.set_color(pieza, lienzo.get_random_color())


def eliminar_basura(lienzo, x, y):
    """
    Quita la pieza de basura que hay en un lugar especifico, si
    hay mas de una en un solo lugar, quita la de encima.
    """
    item = lienzo.find_element_at(x, y)
    if item:
        lienzo.delete(item)


if __name__ == "__main__":
    main()
