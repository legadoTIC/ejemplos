"""
Archivo: numero_favorito.py
-------------------------
Este programa le pide al usuario adivinar un numero, dandole pistas hasta
que lo adivine correctamente
-------------------------
Palabras claves de Python en este programa:

def: definir
main: principal
while: mientras
if: si
else: en otro caso
input: ingreso
print: imprimir
name: nombre
"""

def main():
    print("Intenta adivinar mi numero favorito! (Entre 0 y 100)")
    
    #Aca definimos el numero a adivinar
    numero_favorito = 43

    suposicion = int(input("Cuanto es?: "))
    while suposicion != numero_favorito:
        if suposicion < numero_favorito:
            print("muy bajo")
        else:
            print("muy alto")
        suposicion = int(input("Cuanto es?: "))

    print("Buen trabajo!")

if __name__ == '__main__':
    main()
