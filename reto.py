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
    for y in range(250):
        t.goto(0,y)
        for x in range(250):
            t.forward(1)
            i=t.pos()
            #Imprimir pocision en todo momento
            print(i)
            #Que hacer si encuentra un punto
            for z in lista:
                if x==z:
                    movimiento_secundario(lista,a)
        t.home()
    
#Movimiento del cursor una vezz encontro un punto
def movimiento_secundario(conjunto,a):
    d=t.pos
    for angulo in range(360):
        t.left(angulo)
        for x in range(250):
            t.forward(1)
            j=t.pos()
            #Imprimir pocision en todo momento
            print(j)
            #Que hacer si encuentra otro punto
            for c in conjunto:
                if x==c:
                    d
                    localizar_punto(d,c,a)

#Movimiento para localizar el punto
def localizar_punto(a,b,c):
    m=(a+b)/2
    t.goto(m)
    t.right(90)
    t.forward(25)
    n=t.pos
    if n==c:
        t.forward(2)
        t.circle(2)
#Mantener ventana abierta
t.screen.mainloop()