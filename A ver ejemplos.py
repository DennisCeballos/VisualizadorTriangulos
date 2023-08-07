# A ver ejemplos
'''
from tkinter import *
from tkinter import scrolledtext

master_window = Tk()

# Parent widget for the buttons
buttons_frame = Frame(master_window, bg='black')
buttons_frame.grid(row=0, column=0, sticky=W+E)    

btn_Image = Button(buttons_frame, text='Image')
btn_Image.grid(row=0, column=0, padx=(10), pady=10)

btn_File = Button(buttons_frame, text='File')
btn_File.grid(row=0, column=1, padx=(10), pady=10)

btn_Folder = Button(buttons_frame, text='Folder')
btn_Folder.grid(row=0, column=2, padx=(10), pady=10)

# Group1 Frame ----------------------------------------------------
group1 = LabelFrame(master_window, text="Text Box", padx=5, pady=5, bg='yellow')
group1.grid(row=1, column=0, columnspan=3, padx=100, pady=100, sticky=E+W+N+S)

master_window.columnconfigure(0, weight=1)
master_window.rowconfigure(1, weight=1)

group1.rowconfigure(0, weight=1)
group1.columnconfigure(0, weight=1)

# Create the textbox
txtbox = scrolledtext.ScrolledText(group1, width=40, height=10)
txtbox.grid(row=0, column=0,   sticky=E+W+N+S)

mainloop()
'''
'''
import tkinter
import turtle
import tkinter.messagebox

window = tkinter.Tk()

canvas = tkinter.Canvas(master = window, width = 800, height = 800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10) # , sticky='nsew')
#draw = turtle.Turtle()
draw = turtle.RawTurtle(canvas)

def Board(a, x, y, size):
    #draw.pu()
    draw.penup()
    draw.goto(x,y)
    #draw.pd()
    draw.pendown()
    for i in range (0, 4):
        draw.forward(size)
        draw.right(90)

def Board2():
    x =-40
    y = -40
    size = 40
    for i in range (0, 10):
        for j in range (0, 10):
            Board(draw, x + j*size, y + i*size, size)

def Button_click ():
    tkinter.messagebox.showinfo("Game", "Tic Tac Toe")

#button = tkinter.Button(window, text = "Play!", command = Button_click)
#button = Tk.Button(window, text = "Play!", command = Button_click)
#button.pack()
#
Play_Button = tkinter.Button(master = window, text ="Play!", command = Button_click)
Play_Button.config(bg="cyan",fg="black")
Play_Button.grid(padx=2, pady=2, row=0, column=11, sticky='nsew')

Board_Button = tkinter.Button(master = window, text ="Draw_Board", command = Board2)
Board_Button.config(bg="cyan",fg="black")
Board_Button.grid(padx=2, pady=2, row=1, column=11, sticky='nsew')
#
window.mainloop()
'''

from tkinter import *
from tkinter.tix import ButtonBox
root= Tk()

b = Button(root, text="Enter", width=10, height=2)
b.config()
b.pack(side=LEFT)

c = Button(root, text="Clear", width=10, height=2)
c.pack(side=LEFT)

root.mainloop()