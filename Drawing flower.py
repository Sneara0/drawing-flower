import  turtle

turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(0)
turtle.pensize(2)
turtle.color("yellow")

for i in range (36):
    for j in range(4):
        turtle.forward(100)
        turtle.right(90)
        turtle.right(10)

        turtle.mainloop()