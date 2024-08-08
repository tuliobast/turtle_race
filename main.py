from turtle import Turtle, Screen
import random 

screen = Screen()
screen.setup(width = 500, height = 400)
is_rece_on = False
set_bet =screen.textinput(title= 'Meke your bet', prompt= 'which turtle do you think to win?: write a color')
y_position = [-50, -30, -10, 10, 30, 50]
colors = [
  'cyan',
  'magenta',
  'yellow',
  'red',
  'green',
  'blue',
]

# def list_turtles():
turtles = []
if turtles == []:
  for turtle in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x = -240, y = y_position[turtle])
    print(new_turtle.position())
    turtles.append(new_turtle)
    
if set_bet:
  is_rece_on = True

while is_rece_on:
  for turtle in turtles:
    if turtle.xcor()>230:
      is_rece_on = False
      if turtle.pencolor() == set_bet:
        print(f'You win! The turtle is {turtle.pencolor()}')
      else:
        print(f'You lose! The turtle is {turtle.pencolor()}')
    rand_distance = random.randint(0,10)
    turtle.forward(rand_distance)


screen.exitonclick()