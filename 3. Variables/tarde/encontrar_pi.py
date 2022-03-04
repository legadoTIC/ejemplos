"""
Archivo: encontrar_pi.py
-------------------------
Este programa nos fa el valor de pi a partir del lanzamiento de dardos aleatorios
hacia en circulo inscrito en un cuadrado. La fracción que quede en el circulo debería ser pi/4
-------------------------
Palabras claves de Python en este programa:

def: definir
main: principal
for-in: por cada - en
range: rango
print: imprimir
name: nombre

---librerias---
random: aleatorio
math: matematicas
"""

#aca importamos librerías para poder generar valores aleatorios
import random
#...y aca importamos librerías para calcular raices
import math

#esta es la cantidad de dardos que vamos a lanzar.
num_dardos = 20000000

def main():
    print("este programa es un poco lento, gracias por tu paciencia!")
    num_en_circulo = 0
    #definimos una variable i que servirá par nuestro ciclo
    for i in range(num_dardos):
        """
        obtenemos un valor aleatorio de -1 a 1 en x y en y.
        0,0 es el centro del circulo, - 1 y 1 son los limites positivos y 
        negativos del cuadrado.
        """
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        """
        Miramos si el dardo cayó en el circulo calculando la longitud de la
        hipotenusa del triangulo creado a este punto, el radio del circulo es 1, asi 
        que si nos da mas allá de eso, esta distancia estará por fuera
        """
        distancia = math.sqrt(x * x + y * y)
        if distancia <= 1:
            num_en_circulo += 1
        
    # Approximamos a pi
    fraccion = num_en_circulo / num_dardos
    pi = fraccion * 4
    print(pi)

if __name__ == '__main__':
    main()
