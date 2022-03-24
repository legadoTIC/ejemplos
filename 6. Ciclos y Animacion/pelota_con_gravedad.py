"""
Archivo: pelota_con_gravedad.py
-------------------
Una pelota rebota, simulando el efecto de la gravedad. Especificamente,
lo simulamos aumentando la velocidad en y cada fotograma, pero haciendo 
que cada vez que rebote pierda un poco de dicha velocidad.
"""
import time
from graphics import Canvas


DIAMETRO_PELOTA = 20
RETRASO_ANIMACION = 0.2

GRAVEDAD = 0.5
AMORTIGUAMIENTO = 0.7

def main():
    lienzo = Canvas()
    lienzo.set_canvas_title("Pelota con Gravedad.")

    # Dibuja una pelota en la esquina superior izquierda.
    pelota = lienzo.create_oval(0, 0, DIAMETRO_PELOTA, DIAMETRO_PELOTA)
    lienzo.set_color(pelota, "black")

    #variables para velocidad.
    vx = 3
    vy = 0

    while True:
        vy += GRAVEDAD

        #Deberia rebotar la pelota?
        if (lienzo.get_top_y(pelota) > ((lienzo.get_canvas_height()) - lienzo.get_height(pelota))):
            vy = vy * AMORTIGUAMIENTO
        
        lienzo.move(pelota, vx, vy)
        time.sleep(RETRASO_ANIMACION)
        lienzo.update()

    lienzo.mainloop()



if __name__ == "__main__":
    main()
