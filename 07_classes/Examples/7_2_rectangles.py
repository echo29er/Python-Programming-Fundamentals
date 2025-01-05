import turtle

class Rectangle:
    def __init__(self, x=0, y=0, width=50, height=50, color="transparent", outline="black", edgeWidth=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.outline = outline 
        self.edgeWidth = edgeWidth

    def draw(self):
        shape = turtle.Turtle()
        shape.penup() # stops the line drawing
        shape.goto(self.x,self.y)
        shape.pendown()
        shape.pensize(self.edgeWidth)
        shape.pencolor(self.outline)
        shape.fillcolor(self.color)
        shape.begin_fill()
        for side in range(2):
            shape.forward(self.width)
            shape.left(90)
            shape.forward(self.height)
            shape.left(90)
        shape.end_fill()

# Create and draw the rectangle
shape1 = Rectangle(10, 10, 20,30, edgeWidth=3, color="red", outline ="grey")
shape1.draw()

shape2 = Rectangle(100, 100, 50,30, edgeWidth=4, color="blue", outline ="grey")
shape2.draw()

turtle.done()  # Keep the window open