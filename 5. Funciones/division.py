"""
Archivo: division.py
-------------------
Muestra informacion con respecto a una division especifica.
"""


def main():
    mostrar_informacion(50, 5)
    mostrar_informacion(99, 5)
    mostrar_informacion(73, 7)


def mostrar_informacion(dividendo, divisor):
    """
    Muestra la información de las funciones utilizadas al usuario, como
    podría serlo el valor de la división, si es impar o no, o el residuo
    de la division
    """
    print("valor = " + str(dividendo))
    print("    Es impar? " + str(es_impar(dividendo)))
    print("    valor / " + str(divisor)
          + " = " + str(division(dividendo, divisor))
          + " residuo " + str(residuo(dividendo, divisor)))


def es_impar(dividendo):
    """
    Muestra verdadero o falso dependiendo del valor del dividendo.
    """
    ret = (dividendo % 2) == 1
    if ret == True:
        return ("Verdadero")
    else:
        return ("Falso")


def division(dividendo, divisor):
    """
    Hace una division entera para dividendo / divisor.
    """
    return dividendo // divisor


def residuo(dividendo, divisor):
    """
    retorna el residuo de la division
    """
    return dividendo % divisor


if __name__ == '__main__':
    main()
