"""
File: barra_que_dispara.py
-------------------
Crea una barra que rastrea el mouse del usuario, y que dispara 
'cohetes' cuando el usuario hace clic, que van hacia arriba.
"""

from graphics import Canvas
import time

DIAMETRO_COHETE = 10

# movimiento de un cohete en cada fotograma
MOVIMIENTO_COHETE = 5

# lugar y dimensiones de la barra
CORRECCION_BARRA_EN_Y = 50
ANCHO_BARRA = 100
ALTO_BARRA = 20

RETRASO_ANIMACION_SEGUNDOS = 0.02


def main():
    lienzo = Canvas()
    lienzo.set_canvas_title("Barra que dispara")

    # Lista de los cohetes en el lienzo.
    lista_de_cohetes = []
    barra = crear_barra(lienzo)
    lienzo.update()

    while True:
        actualizar_posicion_barra(lienzo, barra)
        buscar_nuevos_cohetes(lienzo, lista_de_cohetes)
        animar_cohetes(lienzo, lista_de_cohetes)

        lienzo.update()
        time.sleep(RETRASO_ANIMACION_SEGUNDOS)

    lienzo.mainloop()


def crear_barra(lienzo):
    """
    Crea la barra a partir de los parametros. En una
    posicion adecuada segun estos y en color negro  .  
    """
    y = lienzo.get_canvas_height() - CORRECCION_BARRA_EN_Y
    barra = lienzo.create_rectangle(0, y, ANCHO_BARRA, y + ALTO_BARRA)
    lienzo.set_color(barra, 'black')
    return barra


def actualizar_posicion_barra(lienzo, barra):
    """
    Updates the paddle location to track the mouse.  The paddle y
    coordinate will not change, but the x coordinate will be centered
    at the mouse x.
    """
    lienzo.moveto(barra, lienzo.get_mouse_x() - lienzo.get_width(barra) / 2,
                  lienzo.get_top_y(barra))


def buscar_nuevos_cohetes(lienzo, lista_cohetes):
    """
    Revisa si han hecho clicks, y en tal caso, añade un cohete a la pantalla en
    la ubicación del click, también lo añade a la lista de cohetes.
    """
    clicks = lienzo.get_new_mouse_clicks()
    for click in clicks:
        y = lienzo.get_canvas_height() - CORRECCION_BARRA_EN_Y
        cohete = lienzo.create_oval(click.x, y,
                                    click.x + DIAMETRO_COHETE,
                                    y + DIAMETRO_COHETE)
        lienzo.set_color(cohete, 'blue')
        lista_cohetes.append(cohete)


def animar_cohetes(lienzo, lista_cohetes):
    """
    Anima todos los cohetes en la lista de cohetes aún visibles en el
    lienzo
    """
    for cohete in lista_cohetes:
        if lienzo.get_top_y(cohete) + lienzo.get_height(cohete) >= 0:
            lienzo.move(cohete, 0, -MOVIMIENTO_COHETE)


if __name__ == "__main__":
    main()