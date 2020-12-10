import turtle
import pandas


def save_missing_states():
    # Write a plain text file, states on separate lines
    # with open("states_to_learn.csv", mode="x") as file:
    #     for state in all_states:
    #         if state not in guessed_states:
    #             file.write(f"{state}\n")

    # Write a Pandas DataFrame structure to csv
    # missing_states = []
    # for state in all_states:
    #     if state not in guessed_states:
    #         missing_states.append(state)

    # Using List Comprehension:
    missing_states = [state for state in all_states if state not in guessed_states]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv", header=["state"])


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
    if answer_state == "Exit" or answer_state == "Quit":
        save_missing_states()
        break
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
        t.goto(x, y)
        # .item() grabs the FIRST element of the series
        # t.write(state_data.state.item(), align="center")
        t.write(answer_state, align="center")


turtle.mainloop()  # Keep the window open when the program ends
