import turtle

vines = int(input("how big do you want the spiral (vines) to be? (200 to fill the whole screen)"))
petal = input("what colour do you want the petals to be?")

t = turtle.Turtle()
t.shape("circle")
t.colour(petal)

for i in range(vines):
    t.forward(2+i/4)
    t.left(30-i/12)
    t.speed(125)
    t.stamp()

turtle.done()