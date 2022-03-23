from karel.stanfordkarel import *

"""
Archivo: paso_arriba.py
------------------------
El primer programa de ejemplo para Karel, toca que karel tome el 'beeper' 
en frente suyo y lo ponga en el tope de la colina.
(este es un comentario, no será leido por la computadora.)

**NOTA: LAS FUNCIONES DE KAREL HAN SIDO TRADUCIDAS AL ESPAÑOL, ESTE CODIGO DEBE TRADUCIRSE AL INGLES PARA CORRER**
------------------------
Palabras claves de Python en este programa:
def: definir función.
"""


def main():
    """
    Cuando inicies el programa, se correrá este código.
    """
    mover()
    recoger_beeper()
    girar_a_la_izquierda()
    mover()
    girar_a_la_derecha()
    mover()
    poner_beeper()
    mover()


def girar_a_la_derecha():
    """
    Creamos un nuevo comando, diciendole a Karel que gire 3 veces a la izquierda...
    Lo cual lo hace girar a la derecha.
    """
    girar_a_la_izquierda()
    girar_a_la_izquierda()
    girar_a_la_izquierda()

# No te preocupes por este codigo, no debe modificarse.

if __name__ == "__main__":
    run_karel_program()