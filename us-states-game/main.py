import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_csv = pandas.read_csv("50_states.csv")
states_list = states_csv["state"].to_list()


correct_guesses = []
state_object = turtle.Turtle()
state_object.hideturtle()

while len(correct_guesses) <= 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Correct", prompt="Name a state: ").title()
    state_coordinates = states_csv[states_csv["state"] == answer_state]
    if answer_state.lower() == "exit":
        missing_states = [state for state in states_list if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer_state in states_list:
        correct_guesses.append(answer_state)
        state_object.penup()
        state_object.goto(int(state_coordinates["x"]), int(state_coordinates["y"]))
        state_object.write(answer_state)
