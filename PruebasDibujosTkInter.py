import tkinter as tk
import turtle

punto = 1

master = tk.Tk()
#master.configure( height=500, width=1000 )
master.geometry( "1200x550" )
master.grid_propagate( False )
master.resizable( True , True )


mayor = tk.LabelFrame( master=master, bg='white', height=480, width=1130)
mayor.pack( padx=35, pady=35 )
mayor.pack_configure( anchor='center' )
mayor.pack_propagate( False )


fra1 = tk.Frame( master=mayor )
fra1.grid( column=0, row=0 )
fra1.grid_anchor( 'center' )
fra1.grid_propagate( False )
fra1.configure( height=480, width=480, bg='red' )

fra2 = tk.Frame( master=mayor )
fra2.grid( column=1, row=0 )
fra2.grid_anchor( 'center' )
fra2.grid_propagate( False )
fra2.configure( height=480, width=480, bg='blue' )


def revisar( a ):
    global punto
    print("Analizando ", a)

    if (a=='1'):
        print("Verdadero", punto)
    else:
        print("Falso",punto)
    punto +=1
    print("//////////")
    return True


entrada = tk.Entry( master=fra2, validate='all')
entrada.configure( validate= "key", validatecommand = (master.register(revisar),"%P") )
entrada.pack()

dos= tk.Entry( master=fra2 )
dos.pack()

dsitraccion = tk.Button(fra2, text="Distraccion")
dsitraccion.pack()


lienzo = tk.Canvas( master=fra1, height=420, width=420, borderwidth=5 )
lienzo.grid( padx=15, pady=15)

tortu = turtle.RawTurtle( canvas=lienzo )

tortu.goto( tortu.xcor(), tortu.ycor()-200 )
tortu.circle( 200 )





master.mainloop()