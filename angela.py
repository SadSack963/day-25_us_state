import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the CSV into a Pandas DataFrame
csv = "50_states.csv"
data = pandas.read_csv(csv)

# Get a data series of the first column and convert to a list
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    # Get answer and convert to Title Case
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} States Correct", prompt="Name a U.S. state :").title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        # create new turtle
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        # Get the row where state = answer_state
        state_data = data[data.state == answer_state]
        # Then get the x and columns in that row and convert to an integer
        x = int(state_data.x)
        y = int(state_data.y)
        print(x, y)
        t.goto(x, y)
        # .item() grabs the FIRST element of the series
        # t.write(state_data.state.item(), align="center")
        t.write(answer_state, align="center")

turtle.mainloop()  # Keep the window open when the program ends
