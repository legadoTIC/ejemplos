
from graphics import Canvas
import random

# El minimo y el maximo tamaño de las dimensiones para las formas.
TAMANO_MINIMO = 10
TAMANO_MAXIMO = 50


def main():
    lienzo = Canvas()
    lienzo.set_canvas_title("Figuras de Colores")

    # Creamos los Interactores (2 botones y un camppo de texto)
    lienzo.create_text_field("Color", Canvas.TOP)
    lienzo.create_button("Crear Ovalo", Canvas.TOP)
    lienzo.create_button("Crear Rectangulo", Canvas.TOP)

    while True:
        clicks_a_boton = lienzo.get_new_button_clicks()
        for click in clicks_a_boton:

            # Obtiene el color correspondiente.
            color = lienzo.get_text_field_text("Color")

            # Crea la forma correspondiente al boton que se haya presionado
            if click == "Create Oval":
                create_random_oval_with_color(lienzo, color)
            elif click == "Create Rectangle":
                create_random_rectangle_with_color(lienzo, color)

        lienzo.update()

    lienzo.mainloop()


def create_random_oval_with_color(lienzo, color):
    """
    Crea un ovalo con un lugar y un tamaño aleatorio en el lienzo, con el color dado.
    """
    ancho = random.randint(TAMANO_MINIMO, TAMANO_MAXIMO)
    alto = random.randint(TAMANO_MINIMO, TAMANO_MAXIMO)
    x = random.randint(0, lienzo.get_canvas_width() - ancho)
    y = random.randint(0, lienzo.get_canvas_height() - alto)

    # Crea un ovalo con el color pedido
    ovalo = lienzo.create_oval(x, y, x + ancho, y + alto)
    lienzo.set_color(ovalo, color)


def create_random_rectangle_with_color(lienzo, color):
    """
    Crea un ovalo con un lugar y un tamaño aleatorio en el lienzo, con el color dado.
    """
    ancho = random.randint(TAMANO_MINIMO, TAMANO_MAXIMO)
    alto = random.randint(TAMANO_MINIMO, TAMANO_MAXIMO)
    x = random.randint(0, lienzo.get_canvas_width() - ancho)
    y = random.randint(0, lienzo.get_canvas_height() - alto)

    # Crea un rectangulo con el color pedido
    rect = lienzo.create_rectangle(x, y, x + ancho, y + alto)
    lienzo.set_color(rect, color)


if __name__ == '__main__':
    main()
