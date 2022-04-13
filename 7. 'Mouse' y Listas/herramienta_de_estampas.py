"""
Archivo: herramienta_de_estampas.py
-------------------
Este programa te deja mover una 'Estampa' alrededor de la pantalla, y donde
se haga 'click', deja una 'estampa' en ese lugar.
"""

from graphics import Canvas

TAMANO_ESTAMPAS = 50


def main():
    lienzo = Canvas()
    lienzo.set_canvas_title("Herramienta de Estampas.")

    herramienta_estampas = dibujar_estampa(lienzo, lienzo.get_mouse_x(), lienzo.get_mouse_y(), 'blue')
    while True:
        clicks = lienzo.get_new_mouse_clicks()
        for click in clicks:
            dibujar_estampa(lienzo, click.x, click.y, 'black')

        lienzo.raise_to_front(herramienta_estampas)
        centrar_estampa(lienzo, herramienta_estampas, lienzo.get_mouse_x(), lienzo.get_mouse_y())
        lienzo.update()

    lienzo.mainloop()

def dibujar_estampa(lienzo, x, y, color):
    """
    Dibuja una estampa rectangular del color dado.
    """
    rect = lienzo.create_rectangle(x - TAMANO_ESTAMPAS / 2, y - TAMANO_ESTAMPAS / 2,
                                   x + TAMANO_ESTAMPAS / 2, y + TAMANO_ESTAMPAS / 2)
    lienzo.set_color(rect, color)
    return rect


def centrar_estampa(lienzo, estampa, x, y):
    """
    Reposiciona una estampa para que este centrada con respecto a un punto.
    """
    lienzo.moveto(estampa, x - lienzo.get_width(estampa) / 2, y - lienzo.get_height(estampa) / 2)


if __name__ == "__main__":
    main()