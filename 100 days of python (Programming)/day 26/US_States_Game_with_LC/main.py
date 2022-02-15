
from os import stat
import turtle
import pandas

'''Display US states gif'''
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800,height=600)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

'''Organize Data'''
data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name").title()
    
    # update code with list comprehension
    # Exit produce states_to_learn
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Add state to gif
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
