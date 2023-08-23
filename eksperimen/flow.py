import turtle

def draw_flower():
    screen = turtle.Screen()
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("purple")
    
    for _ in range(36):
        draw_petal(pen)
        pen.right(10)
    
    pen.hideturtle()
    screen.mainloop()

def draw_petal(pen):
    pen.circle(100, 60)
    pen.left(120)
    pen.circle(100, 60)
    pen.left(120)

if __name__ == "__main__":
    draw_flower()
