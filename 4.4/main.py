import turtle

vines = int(input("How big do you want the spiral (vines) to be? (200 to fill the whole screen): ").lower().strip())
petal = input("What colour do you want the petals to be? (put no spaces in between the words):  ").lower().strip()

t = turtle.Turtle()
t.speed(0)
t.pencolor("green") # Vine colour
leaf_color = "green" # Lead colour

def draw_triangle_leaf(size):
  # Draw a triangle leaf (pointing forward)
  t.color(leaf_color)
  t.begin_fill()
  t.forward(size * 1.5) # Point of triangle faces forward
  t.left(150)
  t.forward(size)
  t.left(60)
  t.forward(size)
  t.left(150)
  t.end_fill()
  t.color("green") # Reset to vine color

def draw_spiral(steps, current_step = 0):
  # Recursive function to draw the spiral 
  if current_step >= steps:
    return

  t.forward(2 + current_step / 4)
  t.left(30 - current_step / 12)

  # Make petals grow bigger as spiral grows
  petal_size = 3 + (current_step * 0.1)

  # Draw the petal
  t.penup()
  t.dot(petal_size, petal)
  t.pendown()

  # Add triangle leaves
  if current_step % 2 == 0 and current_step > 10:
    # Save current state
    current_pos = t.pos()
    current_heading = t.heading()

    # Draw triangle leaf
    t.penup()
    # Position leaf on the side but keep it pointing along the spiral
    side_offset = 10
    if current_step % 16 == 0: # Alternate sides
      t.right(90)
      t.forward(side_offset)
    else:
      t.left(90)
      t.forward(side_offset)

    # Draw triangle pointing in spiral direction
    leaf_size = 3 + (current_step * 0.06)
    draw_triangle_leaf(leaf_size)
    
    # Return to original position
    t.penup()
    t.goto(current_pos)
    t.setheading(current_heading)
    t.pendown()

  # Recursive call
  draw_spiral(steps, current_step + 1)

def start():
  draw_spiral(vines)

start() # Start the function
turtle.done()