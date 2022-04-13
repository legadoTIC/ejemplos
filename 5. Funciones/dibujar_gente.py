"""
Archivo: dibujar_gente.py
-------------------
Este programa implementa una funcion llama dibujar_persona, la cual dibuja una
representacion grafica de una persona centrada en unas coordenadas (x, y), este
programa dibuja varias personas con esa lógica en mente.
"""

from graphics import Canvas


# Dimensiones del cuerpo
ANCHO_CUERPO = 20
ALTO_CUERPO = 60

# Dimensiones de los brazos
ANCHO_BRAZOS = 40
ALTO_BRAZOS = 40

# Tamaño de la cabeza
DIAMETRO_CABEZA = 40


def main():
    lienzo = Canvas()
    lienzo.set_canvas_title("Draw People")

    dibujar_persona(lienzo, 50, 150)
    dibujar_persona(lienzo, 100, 300)
    dibujar_persona(lienzo, 500, 200)
    dibujar_persona(lienzo, 300, 250)
    dibujar_persona(lienzo, 700, 310)

    lienzo.mainloop()



def dibujar_persona(lienzo, x, y):
    """
    Dibuja una persona a partir de los parametros, la persona tiene un cuerpo verde,
    brazos negros a los lados y una cabeza azul.
    """

    cuerpo_superior_izquierda_y = y - ALTO_CUERPO

    """
    Los brazos son un solo rectangulo 'debajo' del
    cuerpo, pero ponerlo por encima hace que parezcan 2.
    """
    brazos_x = x - ANCHO_BRAZOS / 2
    brazos = lienzo.create_rectangle(brazos_x,
                                   cuerpo_superior_izquierda_y,
                                   brazos_x + ANCHO_BRAZOS,
                                   cuerpo_superior_izquierda_y + ALTO_BRAZOS)
    lienzo.set_color(brazos, "green")

    """
    El cuerpo es un solo rectangulo encima de los brazos.
    """
    cuerpo_superior_izquierda_x = x - ANCHO_CUERPO / 2
    cuerpo = lienzo.create_rectangle(cuerpo_superior_izquierda_x,
                                   cuerpo_superior_izquierda_y,
                                   cuerpo_superior_izquierda_x + ANCHO_CUERPO,
                                   cuerpo_superior_izquierda_y + ALTO_CUERPO)
    lienzo.set_color(cuerpo, "black")

    # La cabeza es un circulo azul encima del cuerpo
    cabeza_superior_izquierda_y = cuerpo_superior_izquierda_y - DIAMETRO_CABEZA
    cabeza_superior_derecha_x = x - DIAMETRO_CABEZA / 2
    cabeza = lienzo.create_oval(cabeza_superior_derecha_x,
                              cabeza_superior_izquierda_y,
                              cabeza_superior_derecha_x + DIAMETRO_CABEZA,
                              cabeza_superior_izquierda_y + DIAMETRO_CABEZA)
    lienzo.set_color(cabeza, "blue")


if __name__ == "__main__":
    main()
