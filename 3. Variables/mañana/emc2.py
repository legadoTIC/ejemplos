"""
Archivo: emc2.py
E = m*(C^2)
-------------------------
Este programa nos ayuda a calcular cuanta energía podríamos
obtener si transformaramos una masa. Gracias por la fórmula, Einstein!
-------------------------
Palabras claves de Python en este programa:

def: definir
main: principal
while: mientras
True: verdadero
print: imprimir
if: si/en caso de que
float: numero flotante (es decir, decimal)
str: cadena de caracteres
name: nombre
"""


# Aca declaramos la constante de la velocidad de la luz en metros por segundo (m/s)
C = 299792458

def main():
    #Aca creamos un ciclo que va a correr por siempre.
    while True:
        print("E = m*(C^2)")
        #Ingresamos la cantidad de masa para la cual calcular.
        masa_en_kilos = float(input("Entre los kilos de masa: "))

        #Calculamos la energia que nos da esa masa.
        energia_en_julios = masa_en_kilos * (C*C)

        #Le mostramos el resultado de nuestra operacion al usuario.
        #Notese como estamos convirtiendo los numeros a cadenas de caracteres para concatenarlos.
        print("Calculos de E = m*(C^2) ...")
        print("m = "+ str(masa_en_kilos) +" kg.")
        print("C = "+str(C)+" m/s")
        print(str(energia_en_julios)+" Julios de energia generados!")


if __name__ == '__main__':
    main()