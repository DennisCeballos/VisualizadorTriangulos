import turtle
from math import *
import random

'''
ULTIMO CAMBIO, SE MODIFICÓ EL TAMAÑO DEL PARAMETRICO
EL CIRCULO DEBE SER DE RADIO 180
'''

class triangulo:
    def __init__(self, superficie): #Crear las variables iniciales
        self.tria = turtle.RawTurtle( canvas=superficie )
        self.tria.color('#BF0000', '#993EBC')
        self.tria.hideturtle()
        self.tria.speed(0)
        self.letras = "ABCDEFG"
        self.a = 0
        self.b = 0
        self.c = 0
        self.puntos = [0 , 1 , 2]
        self.angulost = [0 , 1 , 2]
        self.distancias = [0 , 1 , 2] # 1.a-b   2.b-c   3.c-a
        self.version = 1 #Version 1 tiene circulo, version 2 no tiene circulo        

        if self.version==2:
            #De ser la version 2, se debe crear un circulo externo
            self.circunferencia = turtle.RawTurtle( canvas=superficie )
            self.circunferencia.hideturtle()
            self.circunferencia.color('black','blue')
            self.circunferencia.speed(0)

            self.circunferencia.up()
            self.circunferencia.goto( self.circunferencia.xcor(), self.circunferencia.ycor()-180)
            self.circunferencia.down()
            self.circunferencia.circle( 180 )


        #Tortuga escritora de enunciado
        self.escritor = turtle.RawTurtle( canvas=superficie )
        self.escritor.hideturtle()
        self.tria.speed(0)

    def get(self):
        return self.version


    
    def principal(self, a, b, c):
        self.recibir( a, b, c )

        if self.version==1:   self.dibujarV1()
        elif self.version==2: self.dibujarV2()

        self.escribir()


    def recibir(self, a=float, b=float, c=float): #Solo recibe los angulos
        self.a = a
        self.b = b
        self.c = c
        if self.a==0 and self.b==0 and self.c==0:
            return 1


    def dibujarV1(self): #Dibujará el triangulo coloreado 
        #VERSION 1 sin circulo exterior
        #Primero hallar los angulos para la parametrica
        self.angulost[0] = 0
        self.angulost[1] = 2*self.c
        self.angulost[2] = 2*self.a + self.angulost[1]

        self.tria.clear()

        #Se agrega el giro(k) aleatorio
        k = random.randint( 0 , 180 )
        print("Giro(k) = ", k)
        for i in range(3):
            self.angulost[i] = self.angulost[i] + k

        #Se guardan los puntos con la parametrica
        for i in range(3):
            self.puntos[i] = self.parametrica( self.angulost[i] )
        
        #Ahora centrar el dibujo luego de calcular el punto medio
        retroceso = [ 0 , 0 ] #Este son las coord del punto promedio
        retroceso[0] = ( self.puntos[0][0]+self.puntos[1][0]+self.puntos[2][0] ) / 3
        retroceso[1] = ( self.puntos[0][1]+self.puntos[1][1]+self.puntos[2][1] ) / 3

        for i in range(3):
            nuevo = [0,0]
            nuevo[0] = self.puntos[i][0] - retroceso[0]
            nuevo[1] = self.puntos[i][1] - retroceso[1]
            self.puntos[i] = (nuevo[0], nuevo[1])
        
        print("AngulosT: ", self.angulost)
        print("Puntos:", self.puntos )

        #Ahora añadir el escalado
        self.calcularDistancias()
        m = max( self.distancias ) # La "constante" para el escalado
        print( "m =", m)
        for i in range(3):
            self.puntos[i] = ( self.puntos[i][0] * 90/m, self.puntos[i][1]* 90/m ) #Originalmente 0.5*180/m

        #Dibujar con los puntos y pintar
        self.tria.up()
        self.tria.goto( self.puntos[0] )
        self.tria.down()
        self.tria.begin_fill()
        self.tria.goto( self.puntos[1] )
        self.tria.goto( self.puntos[2] )
        self.tria.goto( self.puntos[0] )
        self.tria.end_fill()        

    def dibujarV2(self): #Dibujará el triangulo coloreado
        #VERSION 2 con triangulo exterior
        #Primero hallar los angulos para la parametrica
        self.angulost[0] = 0
        self.angulost[1] = 2*self.c
        self.angulost[2] = 2*self.a + self.angulost[1]

        self.tria.clear()

        #Se agrega el giro(k) aleatorio
        k = random.randint( 0 , 180 )
        print("Giro(k) = ", k)
        for i in range(3):
            self.angulost[i] = self.angulost[i] + k

        #Se guardan los puntos con la parametrica
        for i in range(3):
            self.puntos[i] = self.parametrica( self.angulost[i] )
        
        #Dibujar con los puntos y pintar
        self.tria.up()
        self.tria.goto( self.puntos[0] )
        self.tria.down()
        self.tria.color('black','red')
        self.tria.begin_fill()
        self.tria.goto( self.puntos[1] )
        self.tria.goto( self.puntos[2] )
        self.tria.goto( self.puntos[0] )
        self.tria.end_fill()        


    def texto_central_escribir(self, enunciado):
        self.escritor.clear()
        self.escritor.write( arg=enunciado, align='center', font=('Arial',16) )
    
    def texto_central_limpiar(self):
        self.escritor.clear()


    def escribir(self): # Escribirá las letras de los puntos del triangulo
        self.tria.up()
        for i in range(3):
            self.tria.goto( self.puntos[i] )
            self.tria.seth( self.angulost[i] )
            self.tria.fd( 15 )
            self.tria.seth( 270 )
            self.tria.fd( 12 )
            self.tria.write( arg=self.letras[i], font=("Arial",15), align='center' )
        self.tria.down()

    def limpiar(self): # Simplemente limpiar la pantalla
        self.tria.clear()


    def calcularDistancias(self):
        # 1.a-b   2.b-c   3.c-a
        self.distancias[0] = min( self.angulost[1]-self.angulost[0], 360-(self.angulost[1]-self.angulost[0]) )
        self.distancias[1] = min( self.angulost[2]-self.angulost[1], 360-(self.angulost[2]-self.angulost[1]) )
        self.distancias[2] = min( self.angulost[2]-self.angulost[0], 360-(self.angulost[2]-self.angulost[0]) )


    def parametrica( self, t ): #La funcion paramétrica que recibe los *valores en grados*
        t = t*pi/180 # Y luego los convierte a radianes
        x = round( 180*cos(t), 3)
        y = round( 180*sin(t), 3)
        return x,y

