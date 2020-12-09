import turtle
import pandas
from messenger import Messenger

image = "blank_states_img.gif"
csv = "50_states.csv"


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

# state_name displays the state names on the map
state_name = Messenger(
    fontcolor="black",
    fontsize=10,
    fonttype="normal",
)

# Read the CSV into a Pandas DataFrame
df = pandas.read_csv(csv)
# print(df.head(3))
"""
             state    x    y
0          Alabama  139  -77
1           Alaska -204 -170
2          Arizona -203  -40
"""


# Game Loop
# =========
game_on = True
total = len(df.index)  # Total number of states
correct = 0  # Number of correct answers given
while game_on:
    answer = screen.textinput(title=f"{correct}/{total} States Correct", prompt="Name a U.S. state :")
    # Prevent .title() crash if cancelled or nothing is input
    if answer is None:
        player_msg.display_message("Incorrect!\nTry Again", 2)
    else:
        # Extract the corresponding Series from the DataFrame
        row = df[df["state"] == answer.title()]

        # Check that the answer given is valid
        if row.empty:
            player_msg.display_message("Incorrect!\nTry Again", 2)
        else:
            print(row["x"])

        game_on = False

turtle.mainloop()  # Keep the window open when the program ends

# screen.exitonclick()
