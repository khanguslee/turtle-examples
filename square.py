import turtle

window  = turtle.Screen()
window.title('Square')

square = turtle.Turtle()
number_of_sides = 4
for side in range(number_of_sides):
    square.forward(100)
    square.right(90)

window.exitonclick()
