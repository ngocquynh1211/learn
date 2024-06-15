import turtle

# Function to draw a rectangle
def draw_rectangle(t, width, height, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw a triangle
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

# Define dimensions and colors
house_base_width = 100
house_base_height = 100
roof_height = 50
door_width = 30
door_height = 50
window_size = 20
tree_trunk_width = 20
tree_trunk_height = 40
tree_triangle_size = 40
house_color = {
    "front": "blue",
    "side": "yellow",
    "roof_left": "pink",
    "roof_right": "orange",
    "door": "lightgreen",
    "window": "brown"
}
tree_color = {
    "trunk": "brown",
    "foliage": "lightgreen"
}

# Draw the house front face
t.penup()
t.goto(-150, -100)
t.pendown()
t.color("black", house_color["front"])
draw_rectangle(t, house_base_width, house_base_height, house_color["front"])

# Draw the right face of the house
t.penup()
t.goto(-150 + house_base_width, -100)
t.pendown()
t.setheading(0)
t.color("black", house_color["side"])
t.begin_fill()
t.fillcolor(house_color["side"])
t.forward(house_base_width)
t.left(90)
t.forward(house_base_height)
t.left(45)
t.forward(house_base_width * (2 ** 0.5))  # using Pythagorean theorem for diagonal
t.left(135)
t.forward(house_base_height)
t.end_fill()

# Draw the left roof
t.penup()
t.goto(-150, -100 + house_base_height)
t.pendown()
t.setheading(0)
t.color("black", house_color["roof_left"])
draw_triangle(t, house_base_width, house_color["roof_left"])

# Draw the right roof
t.penup()
t.goto(-150 + house_base_width, -100 + house_base_height)
t.pendown()
t.setheading(0)
t.color("black", house_color["roof_right"])
t.begin_fill()
t.fillcolor(house_color["roof_right"])
t.forward(house_base_width)
t.left(135)
t.forward(house_base_width * (2 ** 0.5))  # using Pythagorean theorem for diagonal
t.left(45)
t.forward(house_base_width)
t.end_fill()

# Draw the door
t.penup()
t.goto(-150 + house_base_width / 3, -100)
t.pendown()
t.setheading(0)
t.color("black", house_color["door"])
draw_rectangle(t, door_width, door_height, house_color["door"])

# Draw the window
t.penup()
t.goto(-150 + house_base_width * 2 / 3, -100 + house_base_height / 2)
t.pendown()
t.setheading(0)
t.color("black", house_color["window"])
draw_rectangle(t, window_size, window_size, house_color["window"])

# Draw the tree trunk
t.penup()
t.goto(100, -100)
t.pendown()
t.setheading(0)
t.color("black", tree_color["trunk"])
draw_rectangle(t, tree_trunk_width, tree_trunk_height, tree_color["trunk"])

# Draw the tree foliage (triangles)
for i in range(3):
    t.penup()
    t.goto(90, -100 + tree_trunk_height + i * (tree_triangle_size / 2))
    t.pendown()
    t.setheading(0)
    t.color("black", tree_color["foliage"])
    draw_triangle(t, tree_triangle_size, tree_color["foliage"])

# Finish up
t.hideturtle()
screen.mainloop()
