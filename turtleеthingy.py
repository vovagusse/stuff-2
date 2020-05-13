import turtle

screen = turtle.getscreen()
t = turtle.Turtle()

#code itself

#movement
t.begin_fill()
for i in range(10):
    t.forward(100)
    t.right(120)

screen.mainloop()