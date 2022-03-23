from karel.stanfordkarel import *

"""
Archivo: poner_100.py
------------------------
Con este programa, ponemos 100 beepers en un lugar determinado.

**NOTA: LAS FUNCIONES DE KAREL HAN SIDO TRADUCIDAS AL ESPAÑOL, ESTE CODIGO DEBE TRADUCIRSE AL INGLES PARA CORRER**
------------------------
Palabras claves de Python en este programa:
def: definir función.
"""

def main():
    mover()

    #Con esta linea, podemos repetir 100 veces el código indentado dentro, 
    #pero podríamos repetirlo cualquier cantidad de veces.
    for i in range(100):
        poner_beeper()
    #Esta linea ya no esta indentada, no se repetirá
    mover()


# No te preocupes por este codigo, no debe modificarse.

if __name__ == "__main__":
    run_karel_program()
