import turtle
import pandas
from messenger import Messenger

image = "blank_states_img.gif"
csv = "50_states.csv"


def extract_and_display_state(row):
    # Reset the row index to zero (old index retained in a new column)
    row1 = row.reset_index()
    state_name = row1.at[0, "state"]
    state_x = int(row1.at[0, "x"])  # Convert numpy.int64 to int
    state_y = int(row1.at[0, "y"])
    state_msg.display_state(message=state_name, position=(state_x, state_y))


# Set up the Screen
# =================
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)  # Sets the actual window size
# screen.screensize(canvwidth=725, canvheight=491)  # Sets the size of the canvas the turtles are drawing on

screen.bgpic(image)
# screen.addshape(image)
# turtle.shape(image)

# player_msg displays information to the player
player_msg = Messenger(
    fontcolor="red",
    fontsize=24,
    fonttype="bold italic",
)

# state_msg displays the state names on the map
state_msg = Messenger(
    fontcolor="black",
    fontsize=10,
    fonttype="normal",
)

# Read the CSV into a Pandas DataFrame
df = pandas.read_csv(csv)


# Game Loop
# =========
game_on = True
total = len(df.index)  # Total number of states
score = 0  # Number of correct answers given
correct_states = []

while game_on:
    answer = screen.textinput(title=f"{score}/{total} States Correct", prompt="Name a U.S. state :")

    # Prevent .title() crash if cancelled or nothing is input
    if answer is None:
        player_msg.display_message("Incorrect!\nTry Again.", 2)
    else:
        answer = answer.title()  # Convert to Title Case

        # Extract the corresponding Series from the DataFrame
        series = df[df["state"] == answer]

        # Check that the answer given is valid
        if series.empty:
            player_msg.display_message("Incorrect!\nTry Again.", 2)
        else:

            # Check if already answered
            if answer in correct_states:
                player_msg.display_message(f"You already got\n{answer}.\nTry Again.", 2)
            else:
                score += 1
                correct_states.append(answer)
                extract_and_display_state(series)

                # End game
                if score == total:
                    game_on = False
                    player_msg.pencolor("green")
                    player_msg.display_message("Completed.\nWell Done!", 5)

turtle.mainloop()  # Keep the window open when the program ends
