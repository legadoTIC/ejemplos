"""
Archivo: promedio.py
-------------------
Este programa es una implementacion de la formula de promedio, 
esta toma dos numeros y nos muestra el promedio entre ambos
valores.
"""


def main():
    print(promedio(4, 5))
    print(promedio(10, 2))
    print(promedio(-4.1, 9.8))


def promedio(a, b):
    """
    toma dos valores y retorna su promedio.
    """
    return (a + b) / 2


if __name__ == '__main__':
    main()
