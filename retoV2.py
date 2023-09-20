#Reto Navegacion autonoma
#imports
from turtle import Turtle
from random import random

#Pantalla y cursor de turtle
t = Turtle()
t.screen.title('Autonomus Navigation')
t.color("blue")

#Funcion que crea el punto
def punto_inicial():
    #Genera coordenadas aleatorias
    rand1=int(random()*25)
    rand2=int(random()*25) 
    #Crear punto del codigo ArUco
    t.up()
    t.goto(rand1,rand2)
    t.dot()
    a=t.pos()
    print(a)
    t.home()
    t.down()
    puntos_d_apoyo(a)

#Funcion que genera los puntos de apoyo
def puntos_d_apoyo(a):
    #Generar puntos alrededor para ubicar el punto principal
    guardarojos=[]
    t.up()
    for i in range(12):
        t.goto(a)
        t.fd(10)
        t.dot("red")
        b=t.pos()
        t.right(30)
        t.fd(15)
        guardarojos.append(b)
    t.home()
    t.down()
    print(guardarojos)
    movimiento_inicial(guardarojos,a)

#Primer movimiento del cursor
def movimiento_inicial(lista,a):
    #Mover el cursor del centro arriba y a la derecha
    for y in range(15):
        t.goto(0,y)
        for x in range(30):
            t.forward(1)
            pos=t.pos()
            #Imprimir pocision en todo momento
            #print(pos)
            #Que hacer si encuentra un punto
            for z in range(len(lista)):
                var=lista[z]
                puntox=int(var[0])
                puntoy=int(var[1])
                posx=int(pos[0])
                posy=int(pos[1])
                if (posx==puntox)and(posy==puntoy):
                    movimiento_secundario(lista,a,posx,posy)
                    
        t.home()


#Movimiento del cursor una vez encontro un punto
def movimiento_secundario(conjunto,a,coordx,coordy):
    viva=0
    for angulo in range(10):
        t.left(angulo)
        for x in range(20):
            t.forward(1)
            ubi=t.pos()
            #Imprimir pocision en todo momento
            #print(j)
            #Que hacer si encuentra otro punto
            for z in range(len(conjunto)):
                coords=conjunto[z]
                puntox=int(coords[0])
                puntoy=int(coords[1])
                ubix=int(ubi[0])
                ubiy=int(ubi[1])
                if (ubix!=coordx)and (ubiy!=coordy):
                    if (ubix==puntox)and(ubiy==puntoy):
                        localizar_punto(coordx,coordy,ubix,ubiy,a)
        t.goto(coordx,coordy)

#Movimiento para localizar el punto
def localizar_punto(coordx,coordy,ubix,ubiy,a):
    bisx=(coordx+ubix)/2
    bisy=(coordy+ubiy)/2
    t.goto(bisx,bisy)
    t.left(90)
    t.forward(25)
    tray=t.pos()
    trayx=int(tray[0])
    trayy=int(tray[1])
    ax=a[0]
    ay=a[1]

    if (trayx<(ax+15))and(trayx>(ax-15)):
        print(tray)
        t.goto(ax+10,ay)
        t.color("black")
        t.circle(10)
        t.up()
        t.hideturtle()


#Llamafunciones
punto_inicial()    

#Mantener ventana abierta
t.screen.mainloop()