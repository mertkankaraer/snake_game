import turtle
import random

width = 500
height = 500
food_size = 10
delay_time = 100

directions = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def initialize():
    global snake_body, snake_direction, food_pos, drawer
    snake_body = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_direction = "up"
    food_pos = generate_food_position()
    food.goto(food_pos)
    move()

def move():
    global snake_direction
    
    new_head = snake_body[-1].copy()
    new_head[0] += directions[snake_direction][0]
    new_head[1] += directions[snake_direction][1]
    
    if new_head in snake_body[:-1]:
        initialize()
    else:
        snake_body.append(new_head)
        
        if not check_food_collision():
            snake_body.pop(0)
        
        if snake_body[-1][0] > width / 2:
            snake_body[-1][0] -= width
        elif snake_body[-1][0] < -width / 2:
            snake_body[-1][0] += width
        elif snake_body[-1][1] > height / 2:
            snake_body[-1][1] -= height
        elif snake_body[-1][1] < -height / 2:
            snake_body[-1][1] += height
        
        drawer.clearstamps()
        
        for segment in snake_body:
            drawer.goto(segment[0], segment[1])
            drawer.stamp()
        
        screen.update()
        turtle.ontimer(move, delay_time)

def check_food_collision():
    global food_pos
    if calculate_distance(snake_body[-1], food_pos) < 20:
        food_pos = generate_food_position()
        food.goto(food_pos)
        return True
    return False

def generate_food_position():
    x = random.randint(int(-width / 2 + food_size), int(width / 2 - food_size))
    y = random.randint(int(-height / 2 + food_size), int(height / 2 - food_size))
    return (x, y)

def calculate_distance(pos1, pos2):
    return ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5

def move_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def move_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def move_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def move_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

screen = turtle.Screen()
screen.setup(width, height)
screen.title("Snake Game")
screen.bgcolor("darkgreen")
screen.tracer(0)

drawer = turtle.Turtle("square")
drawer.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(food_size / 20)
food.penup()

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_right, "Right")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")

initialize()
turtle.done()
