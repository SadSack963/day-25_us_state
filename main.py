import turtle

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)  # Sets the actual window size

# screen.screensize(canvwidth=725, canvheight=491)  # Sets the size of the canvas the turtles are drawing on
# screen.bgpic(image)

screen.addshape(image)
turtle.shape(image)

answer = screen.textinput(title="Answer", prompt="Name a U.S. state :").title()
print(answer)

turtle.mainloop()  # Keep the window open when the program ends

# screen.exitonclick()
