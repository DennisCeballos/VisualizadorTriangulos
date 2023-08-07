from re import T
import tkinter as tk
import turtle
from DibujoTriangulo_Clase import triangulo
import math

FUENTE2 = ("Arial",20)
FUENTE3 = [("Arial", 15), ("Arial", 12)]
ltr="ABC"
Bool_Debug = False       #Caso haya que verificar

#Funciones trigonometricas con pasos extra (Puede devolver "Indeterminado")
#Estas funciones calculan con grados
def seno(x):
    x = math.radians(x)
    return round( math.sin(x),3 )
def coseno(x):
    x = math.radians(x)
    return round( math.cos(x),3 )
def tangente(x):
    if x==90 or x==270:
        return "Indeterminado"
    else:
        x = math.radians(x)
        return round( math.tan(x),3 )
def cotangente(x):
    if x==0 or x==180:
        return "Indeterminado"
    else:
        x = math.radians(x)
        return round( 1/math.tan(x),3 )
def secante(x):
    if x==90 or x==270:
        return "Indeterminado"
    else:
        x = math.radians(x)
        return round( 1/math.cos(x),3 )
def cosecante(x):  
    if x==0 or x==180:
        return "Indeterminado"
    else:
        x = math.radians(x)
        return round( 1/math.sin(x),3 )

def entero(x):
    if type(x)!=str:
        x = int(x)
    
    else:
        if x.isdigit():
            x = int(x)
        
        elif x=="":
            x=0

        else:
            print("ERROR")
            print("Se pidió entero de un String")
            print("->",x)

    return(x)

class FormularioTriangulo():
    #El inicio, la construccion del formulario
    def __init__(self):
        # Pantalla o Tk
        self.master = tk.Tk()
        self.master.geometry( "1200x550" )
        self.master.grid_propagate( False )
        self.master.resizable( True , True )

        # Creacion del frame mayor
        self.mayor = tk.LabelFrame( master  =self.master,
                                    bg      ='white',
                                    height  =480,
                                    width   =1130)
        self.mayor.pack( padx=35, pady=35 )
        self.mayor.pack_configure(  anchor  ='center' )
        self.mayor.pack_propagate( False )

        #Creacion de los frames principales
        #Son muy similares por lo que pueden crearse con un par de args y una misma funcion
        self.fra1 = self.Creador_Fra(columna=0, ancho=480, colorFondo='#FF8080')
        self.fra2 = self.Creador_Fra(columna=1, ancho=325, colorFondo='#80DA80')
        self.fra3 = self.Creador_Fra(columna=2, ancho=325, colorFondo='#80A3D5')

        #Creando las variables globales necesarias
        self.permiso = tk.BooleanVar()

        self.angle_a = tk.StringVar()
        self.angle_b = tk.StringVar()
        self.angle_c = tk.StringVar()

        #Diseñando el interior de los frames respectivamente
        self.Interior_fra1()
        self.Interior_fra2()
        self.Interior_fra3()

        Boton_Debug = tk.Button( self.fra2, text="Debug", command= self.Operaciones_debug )
        Boton_Debug.grid()


    
    # El "constructor" para los 3 frames principales
    def Creador_Fra(self, columna, ancho, colorFondo):
        fra = tk.Frame( master=self.mayor,
                        height=480,
                        width =ancho, # <- ancho
                        bg    =colorFondo) # <- colorFondo
        fra.grid( column= columna , row=0 ) # <- Aca columna
        fra.grid_anchor( 'center' )
        fra.grid_propagate( False )
        return fra


    # PARTES DEL FRA1
    def Interior_fra1(self):
        self.lienzo = tk.Canvas( master=self.fra1, height=420, width=420)
        self.lienzo.grid( padx=15, pady=15 )

        self.tortu = triangulo( superficie=self.lienzo )

        #Variables relacionadas al lienzo
        self.pantalla_roja = False


    def Dibujar(self, a, b, c):
        print("Recibido en dibujar")
        print("con",a,b,c)
        print("Con permiso==", self.permiso.get())

        if self.permiso.get(): #Si verdadero, que se mande dibujar el triangulo
            self.lienzo.configure(bg="white")
            self.tortu.texto_central_limpiar()
            self.pantalla_roja = False

            #Este comando ya se encarga completamente de la pizarra
            self.tortu.principal(a, b, c)


        else: #Caso contrario, que se quede/ponga rojo

            if not self.pantalla_roja:
                #Acciones para poner roja la pantalla
                self.tortu.limpiar()
                self.lienzo.configure(bg='red')
                self.tortu.texto_central_escribir("Los ángulos internos deben sumar 180°")
                self.pantalla_roja = True




    def Interior_fra2(self): # Terminado ;)
        # Labels que señalan los Angulos(A,B,C)
        for i in range(3):
            lab = tk.Label(master=self.fra2, text=("Ángulo "+ltr[i]), font=FUENTE2)
            lab.grid( column=0, row=i, pady=45 )

        # Valor a los angulos por defecto
        self.angle_a.set( 90 )
        self.angle_b.set( 45 )
        self.angle_c.set( 45 )

        #Register importante para el validatecommand
        reg = self.master.register(self.Validar_Entrada)

        # Creación de los Entrys
        self.inbox1 = tk.Entry( master = self.fra2, textvariable=self.angle_a, font=FUENTE2, 
                                width=4, bd=3, validate="key", validatecommand = (reg,"%P","A") )
        self.inbox1.grid( column=1, row=0 )

        self.inbox2 = tk.Entry( master = self.fra2, textvariable=self.angle_b, font=FUENTE2,
                                width=4, bd=3, validate="key", validatecommand = (reg,"%P","B") )
        self.inbox2.grid( column=1, row=1 )

        self.inbox3 = tk.Entry( master = self.fra2, textvariable=self.angle_c, font=FUENTE2,
                                width=4, bd=3, validate="key", validatecommand = (reg,"%P","C") )
        self.inbox3.grid( column=1, row=2 )

        # Añadir la bolita de angulos °
        for i in range(3):
            lab = tk.Label(master=self.fra2, text=("°"), font=FUENTE2)
            lab.grid( column=2, row=i, pady=45 )




    def Interior_fra3(self): # Terminado :)

        # Por estética, hace falta un primer frame auxiliar
        auxiliar = tk.Frame( master=self.fra3, width=150, height=50 )
        auxiliar.grid( column=0, row=0, pady=20, columnspan=2, sticky='ew' )
        auxiliar.grid_propagate( False )
        # Por estética, el auxiliar 2 realmente sostendrá la "x=" y option menu "angulo"
        auxiliar2 = tk.Frame( master=auxiliar )
        auxiliar2.pack()
        
        # Se crea el Label "x="
        lab = tk.Label( master=auxiliar2, text = "X =", font=FUENTE3[0] )
        lab.pack( side='left', anchor='center')

        # OptionMenu y variable necesaria <cambiante>
        self.cambiante = tk.StringVar()
        self.cambiante.set( "A" )
        self.opciones = tk.OptionMenu( auxiliar2, self.cambiante, *['A','B','C'], command=self.Recalcular_Razones )
        self.opciones.configure( font=FUENTE3[0] )
        self.opciones.pack( side='left', anchor='center' )
        
        #Lista de Razones trigonometricas
        palabras = ["Sin(x)=", "Cos(x)=", "Tan(x)=", "Ctg(x)=", "Sec(x)=", "Csc(x)="]
        for i in range(6):
            label = tk.Label( master=self.fra3, text=palabras[i], font=FUENTE3[1] )
            label.grid( column=0, row=i+1, padx=10, pady=15)
            label.grid_propagate( False )

        self.razones = []
        for i in range(6):
            testo = tk.StringVar()
            self.razones.append( testo )
            label = tk.Label( master=self.fra3, textvariable=testo, font=FUENTE3[1])
            label.grid( column=1, row=i+1, padx=10, pady=15, )
            label.grid_propagate( False )
        


    # Operaciones

    def Recalcular_Razones(self, actual):
        numeros = {
            "A": self.inbox1.get(),
            "B": self.inbox2.get(),
            "C": self.inbox3.get()
        }

        #Obtiene el numero y lo envia a cada label con su respectiva funcion trignonometrica
        valor = float ( numeros.get(actual) )

        e = self.razones[0]
        e.set( seno( valor ))

        e = self.razones[1]
        e.set( coseno( valor ) )

        e = self.razones[2]
        e.set( tangente(valor) )

        e = self.razones[3]
        e.set( cotangente(valor) )

        e = self.razones[4]
        e.set( secante(valor) )

        e = self.razones[5]
        e.set( cosecante(valor) )


    #Verifica los Entry's y la veriable BLOQUEADO
    def Validar_Entrada(self, dato, entrada):
        if Bool_Debug: print("Validando ", dato)
        if Bool_Debug: print("B =",entrada)
        
        # Si el dato ingresado es valido (numero o espacio en blanco)
        #   ,se procede a revisar la suma para self.permitido
        if str.isdigit( dato ) or dato=="":

            #Primero igualar todos a los entrys
            a = entero( self.angle_a.get() )
            b = entero( self.angle_b.get() )
            c = entero( self.angle_c.get() )

            #Luego agregar el cambio nuevo segun la entrada señalada en la funcion
            if entrada=='A':
                a = entero(dato)
            elif entrada=='B':
                b = entero(dato)
            elif entrada=='C':
                c = entero(dato)

            suma = a+b+c
            if suma==180:
                self.permiso.set( True )

            else:
                self.permiso.set( False )

            if Bool_Debug: print("Permiso?(==180)", self.permiso.get() ), print("//////")

            #Finalmente, se llama a la funcion que dibujará en el fra1
            self.Dibujar(a,b,c)

            return True

        else: return False
    

    def Operaciones_debug(self):
        #   Boton Debug
        print("")
        print("-DEBUG-")
        print("Angulos A,B,C ->", self.angle_a.get(),";", self.angle_b.get(),";", self.angle_c.get() )
        print("Valor X ->", self.cambiante.get() )
        print("Bloqueo/Validacion ->", self.permiso.get() )
        print("/////////////////")


                



    def run(self):
        self.Recalcular_Razones("A")
        self.master.mainloop()



if __name__=="__main__":
    uno = FormularioTriangulo()
    uno.run()