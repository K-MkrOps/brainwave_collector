import turtle

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()

# Set up the metasurface
metasurface = Metasurface()

# Get the scattering pattern of the metasurface
scattering_pattern = metasurface.scattering_pattern()

# Draw the metasurface based on the scattering pattern
if scattering_pattern == ScatteringPattern.DIFFUSE:
    turtle.pencolor('gray')
    for i in range(36):
        turtle.forward(100)
        turtle.left(170)
elif scattering_pattern == ScatteringPattern.SPECULAR:
    turtle.pencolor('silver')
    for i in range(72):
        turtle.forward(100)
        turtle.left(145)
elif scattering_pattern == ScatteringPattern.LASER:
    turtle.pencolor('red')
    for i in range(5):
        turtle.forward(100)
        turtle.left(144)

# Show the turtle
turtle.showturtle()

# Wait for the user to close the window
turtle.exitonclick()
