import turtle

escenario = turtle.Screen()


cir1 = turtle.Turtle()
cir1.speed(0)
cir1.up()
cir1.setheading(270)
cir1.forward(50)
cir1.down()
cir1.setheading(0)
cir1.circle(50)

cir1.setheading(270)
cir1.forward(150)
cir1.setheading(0)
cir1.circle(200)



cir2 = turtle.Turtle()
cir2.up()
cir2.setheading(270)
cir2.forward(250)
cir2.down()
cir2.setheading(0)
cir2.circle(250)

cir2.up()
cir2.home()
cir2.down()

cir2.up()

for i in range(12):
    cir2.setheading( 30*i +15 )
    cir2.forward(200)

    cir2.down()
    cir2.forward(50)
    cir2.up()
    cir2.home()


prueba = turtle.Turtle()
prueba.circle( radius=100, extent=30)
prueba.circle( radius=100, extent=180)


escenario.mainloop()