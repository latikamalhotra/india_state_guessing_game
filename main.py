import turtle
import pandas
screen =turtle.Screen()
screen.title("India state gussing game")
image="political-map.gif"
screen.addshape(image)    # to load a image on screen
turtle.shape(image)       # now after load a image to screen it available for turtle to use that image
guessed_states =[]
while len(guessed_states) < 35:
     answer_state=screen.textinput(title =f"{len(guessed_states)}/35 States Correct",prompt="what's another state's name?")
     data = pandas.read_csv("states_and_unionterritories_ofindia.csv")

     if answer_state == None:
         break

     else:
          answer_state = answer_state.title()
          list_of_states= data["State Name"].to_list()
          if answer_state == "Exit":
               missing_states= [state for state in list_of_states if state if state not in guessed_states]
               df = pandas.DataFrame({
                     "states": missing_states
               })
               df.to_csv("missing_states")
               break

          if answer_state in list_of_states :
               guessed_states.append(answer_state)  #Before writing the text to the screen, you can hide the turtle, penup and move the turtle to a specific position.
               t =turtle.Turtle()
               t.hideturtle()
               t.penup()
               ans_data = data[data['State Name'] == answer_state]
               t.goto(float(ans_data.iloc[0,1]),float(ans_data.iloc[0,2]))
               t.write(answer_state)


