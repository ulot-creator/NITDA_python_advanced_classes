import turtle

colors = ["red", "blue", "green", "yellow", "purple", "orange"]

t = turtle.Pen()
turtle.bgcolor("black")

for x in range(360):
    t.pencolor(color[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)

t.mainloop()