"""
Archivo: fibonacci.py
-------------------------
Este programa nos ayuda la famosa secuencia de Fibonacci, hasta una constante
llamada maximo_valor, que es el mayor numero dentro de la secuencia que va a 
mostrar nuestro programa.
-------------------------
Palabras claves de Python en este programa:

def: definir
main: principal
while: mientras
print: imprimir
name: nombre
"""

#Aca definimos el maximo valor a mostrar.
maximo_valor = 10000

def main():
    print("Vamos a listar la Secuencia de Fibonacci: ")
    termino_actual = 0
    siguiente_termino = 1

    while termino_actual <= maximo_valor:
        print(termino_actual)
        termino_despues_del_siguiente = termino_actual + siguiente_termino
        termino_actual = siguiente_termino
        siguiente_termino = termino_despues_del_siguiente

if __name__ == '__main__':
    main()