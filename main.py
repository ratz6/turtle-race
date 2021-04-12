import turtle as t
import random
screen = t.Screen()
screen.setup(500, 400)
screen.title("Bhaag Kachua Bhaag")
tuts = []
col = ['Red', 'Green', 'Blue', 'Orange', 'Black']
race_on = True
u_tut = screen.textinput("Which of the turtles will win the race ?", col)
if u_tut not in col:
    print("Enter a correct color")
    exit()
for i in range(5):
    tim = t.Turtle()
    tim.penup()
    tim.shape('turtle')
    tim.color(col[i])
    tim.setposition(-230, (-100 + 50*i))
    tuts.append(tim)
while race_on:
    for toys in tuts:
        toys.forward(random.randint(1, 10))
        if toys.pos() >= (230, toys.ycor()):
            race_on = False
            break
if u_tut == toys.pencolor():
    print(f"You Win!!! The winner is {toys.pencolor()}")
else:
    print(f"You Lose :( The winner is {toys.pencolor()}")
screen.exitonclick()

