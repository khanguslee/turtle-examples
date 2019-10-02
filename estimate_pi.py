import turtle
import random

def renderSquare(input_width):
    # Setup turtle
    square = turtle.Turtle()
    square.hideturtle()
    square.speed(0)

    # Draw square in the middle of the canvas
    square.penup()
    square.goto(-input_width/2, input_width/2)
    square.pendown()
    for _ in range(4):
        square.forward(input_width)
        square.right(90)

def renderCircle(input_radius):
    # Setup turtle
    circle = turtle.Turtle()
    circle.hideturtle()
    circle.speed(0)

    # Draw circle in the middle of the canvas
    circle.penup()
    circle.sety(-input_radius)
    circle.pendown()

    circle.circle(input_radius)

def renderDot(x, y, colour):
    dot = turtle.Turtle()
    dot.hideturtle()
    dot.speed(0)

    dot.penup()
    dot.goto(x, y)
    dot.pendown

    dot.dot(5, colour)


def main():
    window = turtle.Screen()
    window.tracer(100, 0)
    window.title("Estimating Pi")

    square_width = 250
    renderSquare(square_width)

    circle_radius = square_width / 2
    renderCircle(circle_radius)

    number_of_dots = 1000
    count = 0
    for _ in range(number_of_dots):
        x = random.randint(-circle_radius, circle_radius)
        y = random.randint(-circle_radius, circle_radius)

        distance = (x**2 + y**2)**0.5

        if distance < circle_radius:
            colour = "red"
            count += 1
        else:
            colour = "blue"
        renderDot(x, y, colour)

    pi_estimate = 4*(count/number_of_dots)
    print("Pi Estimation: " + str(pi_estimate))
    window.exitonclick()

if __name__ == "__main__":
    main()
