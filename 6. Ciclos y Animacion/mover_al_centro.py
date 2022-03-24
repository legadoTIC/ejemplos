"""
File: move_to_center.py
-------------------
Moves a square from the left edge to the center of the screen.
"""

import time
from graphics import Canvas

tamano_cuadrado = 100
retraso_animacion = 0.02
movimiento_cuadrado = 2

def main():
    lienzo = Canvas()
    lienzo.set_canvas_title("Mover al centro.")


    # dibuja un cuadrado en el Lienzo, centrado en el eje Y.
    y = (lienzo.get_canvas_height() - tamano_cuadrado) / 2
    cuadrado = lienzo.create_rectangle(0, y, tamano_cuadrado, y + tamano_cuadrado)
    lienzo.set_color(cuadrado, "black")
    
    # Se mueve horizontalmente hasta llegar al centro.
    target_x = (lienzo.get_canvas_width() - lienzo.get_width(cuadrado)) / 2

    while lienzo.get_left_x(cuadrado) < target_x:
        lienzo.move(cuadrado, movimiento_cuadrado, 0)
        time.sleep(retraso_animacion)
        lienzo.update()
    
    lienzo.mainloop()


if __name__ == "__main__":
    main()