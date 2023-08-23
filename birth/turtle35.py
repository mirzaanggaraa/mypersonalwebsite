import turtle as t

t.speed(0)
t.pensize(3)
t.left(90)
t.backward(100)
t.color("black")

def draw(length):
    if length < 10:
        return
    else:
        t.forward(length)
        t.color("red")
        t.circle(2)
        t.color("black")
        t.left(30)
        draw(3 * length / 4)
        t.right(60)
        draw(3 * length / 4)
        t.left(30)
        t.backward(length)

draw(100)
t.done()
