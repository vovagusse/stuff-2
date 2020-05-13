import turtle

screen = turtle.getscreen()
t = turtle.Turtle()

#code itself

class DrawShape:
    def draw(self, sides, angles):
        for distance in sides:
            t.forward(distance)
            t.left(angles)

class Square(DrawShape):
    def __init__(self, sides):
        self.sides = sides
        self.angles = 90

class Triangle(DrawShape):
    def __init__(self, sides):
        self.sides = sides
        self.angles = 120

# square = Square([50]*4)

triangle = Triangle([50]*3)
triangle.draw(triangle.sides, triangle.angles)

screen.mainloop()