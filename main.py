import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('cornflowerblue')

t = turtle.Turtle()
t.speed(0)

#sand
t.penup()
t.goto(-5000,-100)
t.pendown()
t.fillcolor('burlywood1')
t.pencolor('burlywood1')
t.begin_fill()
t.goto(-5000,-100)
t.goto(5000,-100)
t.goto(5000,-5000)
t.goto(-5000,-5000)
t.goto(-5000,-100)
t.end_fill()

#water

t.penup()
t.goto(-5000,0)
t.pendown()
t.fillcolor('blue')
t.pencolor('blue')
t.begin_fill()
t.goto(5000,0)
t.goto(5000,-100)
t.goto(-5000,-100)
t.goto(-5000,0)
t.end_fill()

#umbrellas stick
t.penup()
t.goto(-220,-175)
t.pendown()
t.fillcolor('Black')
t.pencolor('black')
t.begin_fill()
t.goto(-220,-350)
t.goto(-210,-350)
t.goto(-210, -175)
t.goto(-220, -175)
t.end_fill()

#Umbrella Top
t.penup()
t.goto(-117,-225)
t.pendown()
t.pencolor('pink')
t.fillcolor('pink')
t.setheading(90)
t.begin_fill()
t.circle(95,180)
t.end_fill()

#umbrella Curve
t.penup()
t.goto(-120,-225)
t.pendown()
t.pencolor('Bisque1')
t.fillcolor('bisque1')
t.setheading(90)
t.begin_fill()
t.circle(30, 180)
t.end_fill()

#umbrella curve 2
t.pencolor('bisque1')
t.fillcolor('bisque1')
t.setheading(90)
t.begin_fill()
t.circle(30, 180)
t.end_fill()

#umbrellas curve 3
t.pencolor('bisque1')
t.fillcolor('bisque')
t.setheading(90)
t.begin_fill()
t.circle(30, 180)
t.end_fill()



# t.penup()
# t.goto(200,-150)
# t.pendown()
# t.pencolor('black')
# t.pensize(5)
# t.forward(100)
# t.circle(20,180)

#Kite head
t.setheading(45)
t.penup()
t.goto(-75,-15)
t.pendown()
t.pencolor("cyan")
t.fillcolor("cyan")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

#Kite String
t.setheading(30)
t.penup()
t.goto(150,100)
t.pendown()
t.pencolor("white")
t.fillcolor("White")
t.goto(-220,-350)
t.goto(-210,-350)
t.goto(-210, -175)
t.goto(-220, -175)
t.end_fill()




#sun
t.penup()
t.goto(-200,200)
t.pendown()
t.fillcolor('yellow')
t.pencolor('yellow')
t.begin_fill()
t.circle(50)
t.end_fill()

#Clouds
t.penup()
t.goto(190,150)
t.pendown()
t.fillcolor('white')
t.pencolor('white')
t.begin_fill()
t.circle(40)
t.end_fill()
t.penup()
t.goto(140,150)
t.pendown()
t.fillcolor('white')
t.pencolor('white')
t.begin_fill()
t.circle(40)
t.end_fill()
t.penup()
t.goto(90,150)
t.pendown()
t.fillcolor('white')
t.pencolor('white')
t.begin_fill()
t.circle(40)
t.end_fill()

t.penup()
t.goto(-200,150)
t.pendown()
t.fillcolor('white')
t.pencolor('white')
t.begin_fill()
t.circle(40)
t.end_fill()
t.penup()
t.goto(-150,150)
t.pendown()
t.fillcolor('white')
t.pencolor('white')
t.begin_fill()
t.circle(40)
t.end_fill()
t.penup()
t.goto(-100,150)
t.pendown()
t.fillcolor('white')
t.pencolor('white')
t.begin_fill()
t.circle(40)
t.end_fill()

#beachball
t.penup()
t.goto(100,-200)
t.pendown()
t.fillcolor('yellow')
t.pencolor('yellow')
t.begin_fill()
t.circle(25)
t.end_fill()

#shark
t.penup()
t.goto(0, -50)
t.pencolor('gray')
t.fillcolor('gray')
t.pendown()
t.begin_fill()
t.goto(25, -50)
t.goto(0, -25)
t.goto(0, -50)
t.end_fill()

#Base of the tress
t.penup()
t.goto(100, -150)
t.pencolor('brown')
t.fillcolor('brown')
t.pendown()
t.pensize(10)

t.goto(100, -50)

t.fillcolor('green')
t.pencolor('green')
t.setheading(135)
t.circle(80,45)
t.penup()
t.goto(140, -10)
t.pendown()
t.setheading(200)
t.circle(80,45)
t.penup()
t.goto(100, -50)
t.pendown()
t.setheading(100)
t.circle(80,45)

t.penup()
t.goto(0, 200)
t.pendown()
t.write('Spring Scene', font=("ariel", 30, "italic"), align="center")


# t.begin_fill()
# t.goto(-220,-350)
# t.goto(-210,-350)
# t.goto(-210, -175)
# t.goto(-220, -175)
# t.end_fill()






turtle.done()