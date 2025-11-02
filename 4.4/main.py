import turtle
num = input("how big do you want the spiral to be? (200 is average)")
number = int(num)
turtle = turtle.Turtle()


for i in range(number):
    turtle.forward(2+i/4)
    turtle.left(30-i/12)
    turtle.speed(100)
    turtle.stamp()

turtle.done()