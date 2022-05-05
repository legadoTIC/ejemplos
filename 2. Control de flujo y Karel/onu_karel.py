from karel.stanfordkarel import *

"""
Archivo: onu_karel.py
------------------------------
Karel construye casas en los lugares definidos en el mundo.

**NOTA: LAS FUNCIONES DE KAREL HAN SIDO TRADUCIDAS AL ESPAÑOL, ESTE CODIGO DEBE TRADUCIRSE AL INGLES PARA CORRER**
------------------------
Palabras claves de Python en este programa:
def: definir función.
while: mientras
if: si/en caso de
"""

def main():
    while frente_sin_obstaculos():
        mover()
        if beepers_presente():
            construir_casa()

def construir_casa():
    """
    Construye una casa en la posición actual de Karel.
    """

    #Cosntruye la primera columna
    recoger_beeper()
    girar_180()
    mover()
    girar_a_la_derecha()
    poner_tres()
    #...Ahora la segunda columna.
    girar_a_la_derecha()
    mover()
    girar_a_la_derecha()
    poner_tres()
    #...y la tercera
    girar_a_la_izquierda()
    mover()
    girar_a_la_izquierda()
    poner_tres()
    girar_180()
    mover_al_muro()
    girar_a_la_izquierda()

def mover_al_muro():
    while frente_sin_obstaculos():
        mover()

def girar_180():
    """
    gira a karel 180 grados
    """
    girar_a_la_izquierda()
    girar_a_la_izquierda()

def girar_a_la_derecha():
    """
    Creamos un nuevo comando, diciendole a Karel que gire 3 veces a la izquierda...
    Lo cual lo hace girar a la derecha.
    """
    girar_a_la_izquierda()
    girar_a_la_izquierda()
    girar_a_la_izquierda()

def poner_tres():
    for i in range(3):
        poner_beeper()
        mover()


# No te preocupes por este codigo, no debe modificarse.

if __name__ == "__main__":
    run_karel_program()
