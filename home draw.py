import turtle

def draw_rectangle(t, width, height, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_parallelogram(t, width, height, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(45)
        t.forward(height)
        t.left(135)
    t.end_fill()

def draw_triangle(t, base, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(3):
        t.forward(base)
        t.left(120)
    t.end_fill()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create turtle
t = turtle.Turtle()
t.speed(2)

# Draw the house front face
t.penup()
t.goto(-150, -100)
t.pendown()
t.color("black", "blue")
draw_rectangle(t, 100, 100, "blue")

# Draw the right face of the house
t.penup()
t.goto(-50, -100)
t.pendown()
t.setheading(45)
t.color("black", "yellow")
draw_parallelogram(t, 100, 70.71, "yellow")

# Draw the left roof
t.penup()
t.goto(-150, 0)
t.pendown()
t.setheading(0)
t.color("black", "pink")
draw_triangle(t, 100, "pink")

# Draw the right roof
t.penup()
t.goto(-50, 0)
t.pendown()
t.setheading(45)
t.color("black", "orange")
t.begin_fill()
t.fillcolor("orange")
t.forward(70.71)
t.right(90)
t.forward(70.71)
t.right(135)
t.forward(100)
t.end_fill()

# Draw the door
t.penup()
t.goto(-120, -100)
t.pendown()
t.setheading(0)
t.color("black", "lightgreen")
draw_rectangle(t, 30, 50, "lightgreen")

# Draw the window
t.penup()
t.goto(-20, -50)
t.pendown()
t.setheading(0)
t.color("black", "brown")
draw_rectangle(t, 20, 20, "brown")

# Draw the tree trunk
t.penup()
t.goto(100, -100)
t.pendown()
t.setheading(0)
t.color("black", "brown")
draw_rectangle(t, 20, 40, "brown")

# Draw the tree lower triangle
t.penup()
t.goto(80, -60)
t.pendown()
t.setheading(0)
t.color("black", "lightgreen")
draw_triangle(t, 60, "lightgreen")

# Draw the tree middle triangle
t.penup()
t.goto(80, -30)
t.pendown()
t.color("black", "lightgreen")
draw_triangle(t, 60, "lightgreen")

# Draw the tree upper triangle
t.penup()
t.goto(80, 0)
t.pendown()
t.color("black", "lightgreen")
draw_triangle(t, 60, "lightgreen")

# Finish up
t.hideturtle()
screen.mainloop()
