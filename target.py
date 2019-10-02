import turtle

window  = turtle.Screen()
window.title('Target')
number_of_sides = 4
number_of_squares = 100

outer_circle = turtle.Turtle()
outer_circle.speed(0)
outer_circle.pencolor("red")
for petal in range(number_of_squares):
    for side in range(number_of_sides):
        outer_circle.forward(100)
        outer_circle.right(90)
    outer_circle.right(360/number_of_squares)

inner_circle = turtle.Turtle()
inner_circle.speed(0)
inner_circle.pencolor("red")
for petal in range(number_of_squares):
    for side in range(number_of_sides):
        inner_circle.forward(50)
        inner_circle.right(90)
    inner_circle.right(360/number_of_squares)



window.exitonclick()
