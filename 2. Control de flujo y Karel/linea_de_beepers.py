from karel.stanfordkarel import *

"""
Archivo: linea_de_beepers.py
------------------------------
Pone una linea de beepers en la parte inferior del mundo en un programa 'Karel'
Funciona para cualquier tamaño del mundo.

**NOTA: LAS FUNCIONES DE KAREL HAN SIDO TRADUCIDAS AL ESPAÑOL, ESTE CODIGO DEBE TRADUCIRSE AL INGLES PARA CORRER**
------------------------
Palabras claves de Python en este programa:
def: definir función.
while: mientras
"""


def main():
    while frente_sin_obstaculos():
        poner_beeper()
        mover()

    """
    Esta linea es necesaria para poner el
    ultimo beeper, si no se pone, la linea quedará incompleta
    porque se habrá movido una vez menos que los beepers que puso.
    """
    poner_beeper()


# No te preocupes por este codigo, no debe modificarse.
if __name__ == "__main__":
    run_karel_program()