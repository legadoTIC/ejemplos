"""
------------------------------
Archivo: karel_de_teclado.py
------------------------------

Un programa que nos permite hacer que Karel se mueva a partir del teclado.
"""
from graphics import Canvas

# El tamaño del lienzo en el que vamos a trabajar en pixeles
ANCHO_LIENZO = 500
ALTO_LIENZO = 500

# Cuantos pixeles recorre Karel por cada tecla presionada
RECORRIDO_DE_KAREL = 100


def main():
    Lienzo = Canvas()
    Lienzo.set_canvas_title("Karel de Teclado")

    # Creamos a Karel, en la esquina superior izquierda
    karel = Lienzo.create_image(0, 0, "images/karel.png")
    Lienzo.update()

    # Vamos consiguiendo los comandos que vengan del teclado y moviendo a Karel
    while True:
        teclas_pulsadas = Lienzo.get_new_key_presses()
        for comando in teclas_pulsadas:

            # Le decimos a canvas que mueva a Karel en la direccion correspondiente
            # dependiendo de la tecla presionada
            # Left: izquierda
            # Right: Derecha
            # Up: Arriba
            # Down: Abajo
            if comando.keysym == "Left":
                Lienzo.move(karel, -RECORRIDO_DE_KAREL, 0)
            elif comando.keysym == "Right":
                Lienzo.move(karel, RECORRIDO_DE_KAREL, 0)
            elif comando.keysym == "Up":
                Lienzo.move(karel, 0, -RECORRIDO_DE_KAREL)
            elif comando.keysym == "Down":
                Lienzo.move(karel, 0, RECORRIDO_DE_KAREL)
                
        Lienzo.update()

    Lienzo.mainloop()


if __name__ == "__main__":
    main()
