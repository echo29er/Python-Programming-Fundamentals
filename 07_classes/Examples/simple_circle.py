import turtle

class Circle: 
    def __init__(self, x=0, y=0, radius=50, color="transparent", outline="black", edgeWidth=1):
        self.x = x
        self.y = y 
        self.color = color
        self.outline = outline
        self.edgeWidth = edgeWidth
        self.radius = radius

    def draw(self): # mutator method that mutates the turtle object
        t = turtle.Turtle()
        t.penup()
        t.goto(self.x, self.y - self.radius)  # Position at bottom of circle
        t.pendown()
        t.pensize(self.edgeWidth)
        t.pencolor(self.outline)
        t.fillcolor(self.color)
        t.begin_fill()
        t.circle(self.radius)
        t.end_fill()

# Create and draw the circle
x_value = 10
y_value = 30
radius_p = 40 

shape = Circle(x_value, y_value, radius_p, edgeWidth=3, color="red", outline ="grey")
shape.draw()
turtle.done()  # Keep the window open