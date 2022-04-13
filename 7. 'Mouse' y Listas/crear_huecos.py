"""
File: hole_puncher.py
---------------------
This program lets you click anywhere on the canvas to
"punch a hole" (e.g. draw a black circle there).

Este programa nos permite hacer click en cualquier lugar 
del lienzo y "hace un hueco" (es decir, dibuja un circulo negro)
"""

from graphics import Canvas

RADIO_DEL_HUECO = 10


def main():
    lienzo = Canvas()
    lienzo.set_canvas_title("Huecos")

    #Loop de animacionn
    while True:
        clicks = lienzo.get_new_mouse_clicks()
        for click in clicks:
            dibujar_hueco(lienzo, click.x, click.y)
        lienzo.update()

    lienzo.mainloop()


def dibujar_hueco(canvas, x, y):
    """
    Dibuja un circulo en el lienzo, centrada en un lugar dado del lienzo.
    """
    ovalo = canvas.create_oval(x - RADIO_DEL_HUECO, y - RADIO_DEL_HUECO,
                              x + RADIO_DEL_HUECO, y + RADIO_DEL_HUECO)
    canvas.set_color(ovalo, 'black')


if __name__ == "__main__":
    main()
