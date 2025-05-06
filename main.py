import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor ('pink')

t= turtle.Turtle()




t.penup()
t.goto(0, 100)
t.pendown()
t.write('What I Like',font=('arial',30,'bold'),align='center')

t.penup()
t.goto(0, -100)
t.pendown()
t.write('Max Kozar',font=('arial',30,'bold'),align='center')

t.penup()
t.goto(0,-100)
t.pendown()
#circle
t.fillcolor('black')
t.begin_fill()


t.penup()
t.goto(-100, 0)
t.pendown()
screen.addshape('inro1.gif')
t.shape('inro1.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(50, 0)
t.pendown()
screen.addshape('intro2.gif')
t.shape('intro2.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(0, -250)
t.pendown()

t.fillcolor('black')
t.begin_fill()
t.circle(35)
t.end_fill()



round=input('press enter to continue:')
t.clear()
screen.bgcolor('red')



t.penup()
t.goto(0, 100)
t.pendown()
t.write('My Favorite Foods',font=('arial',30,'bold'),align='center')

t.penup()
t.goto(0, -200)
t.pendown()
t.write('spaghetti,pizza,chicken tenders',font=('arial',30,'bold'),align='center')

t.penup()
t.goto(-100, 0)
t.pendown()
screen.addshape('chicken tenders.gif')
t.shape('chicken tenders.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(50, 0)
t.pendown()
screen.addshape('spaghetti.gif')
t.shape('spaghetti.gif')
t.stamp()
t.shape('classic')


t.penup()
t.goto(-50, -250)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()



round=input('press enter to continue:')
t.clear()
screen.bgcolor('green')

t.penup()
t.goto(0, 100)
t.pendown()
t.write('My Favorite Movies',font=('arial',30,'bold'),align='center')

t.penup()
t.goto(-100, 0)
t.pendown()
screen.addshape('brox tale.gif')
t.shape('brox tale.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(50, 0)
t.pendown()
screen.addshape('cars.gif')
t.shape('cars.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(0, -200)
t.pendown()
t.write('Bronx tale & Cars',font=('arial',30,'bold'),align='center')


t.penup()
t.goto(-50, -350)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()





round=input('press enter to continue:')
t.clear()
screen.bgcolor('blue')

t.penup()
t.goto(0, 100)
t.pendown()
t.write('My Favorite Hobbies',font=('arial',30,'bold'),align='center')

t.penup()
t.goto(0, -100)
t.pendown()
t.write('Golf, TV, Drawing, Being With friends',font=('arial',20,'bold'),align='center')

t.penup()
t.goto(-100, 0)
t.pendown()
screen.addshape('golf.gif')
t.shape('golf.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(50, 0)
t.pendown()
screen.addshape('tv.gif')
t.shape('tv.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(-50, -350)
t.pendown()
t.setheading(0)
t.fillcolor('black')
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.penup()
t.end_fill()


round=input('press enter to continue:')
t.clear()
screen.bgcolor('orange')

t.penup()
t.goto(250,0)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.goto(200,0)
t.goto(250,100)
t.goto(300,0)
t.end_fill()



t.penup()
t.goto(0, 100)
t.pendown()
t.write('My Favorite Sport',font=('arial',30,'bold'),align='center')

t.penup()
t.goto(0, -100)
t.pendown()
t.write('Basketball & Football',font=('arial',30,'bold'),align='center')


t.penup()
t.goto(-100, 0)
t.pendown()
screen.addshape('basketball.gif')
t.shape('basketball.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(50, 0)
t.pendown()
screen.addshape('football.gif')
t.shape('football.gif')
t.stamp()
t.shape('classic')











turtle.done()