import turtle

vines = int(input("How big do you want the spiral (vines) to be? (200 to fill the whole screen): "))
petal = input("What colour do you want the petals to be? ")

t = turtle.Turtle()
t.speed(0)
t.color(petal)

vine_color = "green"
leaf_color = "darkgreen"

def draw_simple_leaf():
    # Draw a very simple leaf (just a green dot)
    t.color(leaf_color)
    t.stamp()  # Use the turtle itself as a leaf
    t.color(petal)  # Reset to petal color

def draw_spiral(steps, current_step=0):
    # Recursive function to draw the spiral with leaves
    if current_step >= steps:
        return

    t.pencolor(vine_color)
    t.forward(2 + current_step/4)
    t.left(30 - current_step/12)

    # Add leaves
    if current_step % 10 == 0 and current_step > 5:
        # Save state
        current_pos = t.pos()
        current_head = t.heading()

        # Draw leaf
        t.penup()
        t.right(90)
        t.forward(8)
        draw_simple_leaf()

        # Restore state
        t.penup()
        t.goto(current_pos)
        t.setheading(current_head)
        t.pendown()

    # Main flower stamp
    t.penup()
    t.dot(5, petal) # 5 is the diameter, petal is the color
    t.pendown()

    draw_spiral(steps, current_step + 1)

def start():
    draw_spiral(vines)

start()
turtle.done()