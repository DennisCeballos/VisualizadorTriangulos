import turtle
from math import *

def parametrica( t ): #La paramétrica recibe los valores en grados
    t = t*pi/180 # Y luego los convierte a radianes
    x = 250*cos(t)
    y = 250*sin(t)
    return x,y

pantalla = turtle.Screen()
#pantalla.screensize(canvheight=1000, canvwidth=100)
pantalla.setup(width=800, height=600)

circunferencia = turtle.Turtle()
circunferencia.speed(0)
circunferencia.penup()
circunferencia.goto(0,-250)
circunferencia.pendown()
circunferencia.circle(250)

triangulo = turtle.Turtle()
puntos = []
angulos_parametric = []


for i in range(3):
    print("Angulo "+ str(i+1) + "?")
    a = float(input())
    puntos.append( parametrica( a ) )
    angulos_parametric.append( a )

letras = "ABCDEFGHIJKLMNOPQRSTVUWXYZ"
triangulo.penup()
triangulo.goto( puntos[0] )
triangulo.pendown()

triangulo.speed(5)

triangulo.begin_fill()
for i in range(3):
    #Va al punto i
    triangulo.goto( puntos[i] )
    #Guarda la posicion
    g_x = triangulo.xcor()
    g_y = triangulo.ycor()
    #Gira "hacia afuera", se mueve y escribe
    triangulo.seth( angulos_parametric[i] )
    triangulo.penup()
    triangulo.fd( 15 )#* round( angulos_parametric[i]/360 ) )
    triangulo.seth( 270 )
    triangulo.fd( 12 )
    triangulo.write( arg=letras[i], font=("Arial",15), align='center' )
    #Regresa al guardado
    triangulo.setx( g_x )
    triangulo.sety( g_y )
    triangulo.pendown()
triangulo.end_fill()


triangulo.goto( puntos[0] )

pantalla.exitonclick()
