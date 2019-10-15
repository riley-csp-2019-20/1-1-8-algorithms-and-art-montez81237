import turtle as trtl
t = trtl.Turtle()
t.speed(-50)

tx = -100
ty = 100

for i in range(3):
    #pacman
    t.fillcolor("yellow")
    t.begin_fill()
    t.penup()
    t.goto(tx,ty)
    t.pendown()
    t.setheading(180)
    t.circle(100,240)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.circle(100,30)
    t.end_fill()

    #make pellets
    t.fillcolor("white")
    t.penup()
    t.goto(50,-25)
    t.pendown()
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.end_fill
    t.clear()

    tx = tx + 50



wn = trtl.Screen()
wn.mainloop()
