"""
Archivo: cara_de_robot.py
-------------------
Dibuja un Robot a partir de los parametros usando funciones,
también escribe el titulo.
"""

from graphics import Canvas

# Dimensiones de la cara
ANCHO_CARA = 300
ALTO_CARA = 350

# Diametro de los ojos
DIAMETRO_OJOS = 70

# Distancia de la parte superior de la cabeza con el ojo
AJUSTE_OJO_Y = 40

# distancia entre los ojos
SEPARACION_OJOS_EN_X = 40

# DImensiones de la boca del robot.
ANCHO_BOCA = 150
ALTO_BOCA = 30

# Distancia de la boca con la parte superior de la cabeza
AJUSTE_BOCA_Y = 200

# Distancia del titulo con la parte superior del lienzo
TITULO_Y = 40


def main():
    lienzo = Canvas()
    lienzo.set_canvas_title("Cara de Robot.")

    dibujar_cabeza(lienzo)
    dibujar_boca(lienzo)
    dibujar_ojos(lienzo)
    dibujar_titulo(lienzo)

    lienzo.mainloop()



def dibujar_cabeza(lienzo):
    """
    Dibuja un rectangulo amarillo, que representa la cabeza
    del robot.
    """
    x = (lienzo.get_canvas_width() - ANCHO_CARA) / 2
    y = (lienzo.get_canvas_height() - ALTO_CARA) / 2
    cabeza = lienzo.create_rectangle(x, y, x + ANCHO_CARA, y + ALTO_CARA)
    lienzo.set_fill_color(cabeza, "yellow")


def dibujar_boca(lienzo):
    """
    dibuja un rectangulo negro a partir de los parametros dados, el cual
    representa la boca del robot
    """
    cabeza_x = (lienzo.get_canvas_width() - ANCHO_CARA) / 2
    cabeza_y = (lienzo.get_canvas_height() - ALTO_CARA) / 2

    boca_x = cabeza_x + (ANCHO_CARA - ANCHO_BOCA) / 2

    # Ajuste para la boca a partir de las dimensiones dadas
    boca_y = cabeza_y + AJUSTE_BOCA_Y

    boca = lienzo.create_rectangle(boca_x, boca_y,
                                    boca_x + ANCHO_BOCA, boca_y + ALTO_BOCA)
    lienzo.set_fill_color(boca, "black")


def dibujar_ojos(lienzo):
    """
    Draws both eyes as filled ovals at the appropriate offset from the top of the face,
    centered horizontally and spaced apart according to EYE_X_SEPARATION.
    """
    cabeza_y = (lienzo.get_canvas_height() - ALTO_CARA) / 2

    # Ajuste desde la parte superios de la cabeza
    ojo_y = cabeza_y + AJUSTE_OJO_Y

    ojo_x = lienzo.get_canvas_width() / 2 - SEPARACION_OJOS_EN_X / 2 - DIAMETRO_OJOS
    dibujar_ojo(lienzo, ojo_x, ojo_y, "blue")

    ojo_x += DIAMETRO_OJOS + SEPARACION_OJOS_EN_X
    dibujar_ojo(lienzo, ojo_x, ojo_y, "green")

def dibujar_ojo(lienzo, x, y, color):
    """
    dibuja un circulo en el lugar especificado por parametros, y con el color especificado.
    el ojo es tan grande como la constante DIAMETRO_OJOS
    """
    ojo = lienzo.create_oval(x, y, x + DIAMETRO_OJOS, y + DIAMETRO_OJOS)
    lienzo.set_fill_color(ojo, color)

def dibujar_titulo(lienzo):
    """
    Dibuja el titulo "Cara de Robot" en la pantalla, centrado horizontalmente.
    """
    titulo = lienzo.create_text(lienzo.get_canvas_width() / 2, TITULO_Y, "Cara de Robot")
    lienzo.set_font(titulo, "Times New Roman", 44)

if __name__ == "__main__":
    main()
