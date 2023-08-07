from DibujoTriangulo_Clase import triangulo
import random
from math import *
import turtle


def bucle(t):
    print( "Angulo deseado 1? ")
    a = float(input())
    print( "Angulo deseado 2? ")
    b = float(input())
    print( "Angulo deseado 3? ")
    c = float(input())
    if t.recibir(a,b,c)==1:
        pantalla.bgcolor('red')
    else:
        t.limpiar()
        t.dibujarV2()
        t.escribir()

        


pantalla = turtle.Screen()
#pantalla.screensize(canvheight=1000, canvwidth=100)
pantalla.setup(width=800, height=600)

'''
circunferencia = turtle.Turtle()
circunferencia.speed(0)
circunferencia.penup()
circunferencia.goto(0,-250)
circunferencia.pendown()
circunferencia.circle(250)
'''


t = triangulo(pantalla)
bucle( t )
t.texto_central_escribir("Los ángulos interiores deben sumar 180°")
pantalla.onclick( lambda x,y: bucle(t) )
pantalla.mainloop()
print("End")
