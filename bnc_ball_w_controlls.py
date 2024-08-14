import turtle
from random import randrange


def exit():
    turtle.done()
    return 0

def throwUp():
    global newVelocity
    newVelocity = 0.2
    global velocityY
    for i, _ in enumerate(velocityY):
        if(velocityY[i] > 0):
            velocityY[i] += newVelocity
        
    
        if (newVelocity >= 0):
            newVelocity -= 0.1




def goLeft():
    
    global velocityX
    for i, _ in enumerate(velocityX):
        velocityX[i] -= 0.2
        ball.setx(ball.xcor() - 3)

    
def goRight():
    global velocityX
    for i, _ in enumerate(velocityX):
        velocityX[i] += 0.2
        ball.setx(ball.xcor() + 3)
    



width = 1000
height = 700
# Set window and ball
window = turtle.Screen()
tmp = window.numinput("How many balls?", "input your balls:", 1, minval=1, maxval=10000)
window.setup(width, height)
window.tracer(0)
window.title("Bouncing Balls <<use arrows to controll>>")


colors = ["red", "blue", "green", "purple", "yellow", "pink"]
ballcount = int(tmp)

balls = []

for x in range(ballcount):
    ball = x
    ball = turtle.Turtle()

    ball.penup()
    ball.setpos(randrange(-300, 300), randrange(-300, 300))
    ball.shape("circle")
    ball.color(colors[randrange(0,len(colors))])
    ball.right(90)
    balls.append(ball)



# #ball init.. facing down, falling
# ball1 = turtle.Turtle()
# ball1.penup()
# ball1.setpos(-300,-300)
# ball1.shape("circle")
# #ball1.pendown()
# ball1.color("red")
# ball1.right(90)

# ball2 = turtle.Turtle()
# ball2.penup()
# ball2.setpos(-200, 200)
# ball2.shape("circle")
# #ball1.pendown()
# ball2.color("blue")
# ball2.right(90)




# balls.append(ball1)
# balls.append(ball2)


energy_loss = 0.95
newVelocity = 0
gravity = -0.0009   # pixels/(time of iteration)^2
velocityY = []   
velocityX = []
for i in balls:
    velocityY.append(1)
    velocityX.append(0.25)

ground = (-height/2) + 15
wall = (width / 2) - 12
seeling = height/2
turtle.listen()
turtle.onkeypress(throwUp, 'Up')
turtle.onkeypress(goLeft, 'Left')
turtle.onkeypress(goRight, 'Right')
turtle.onkeypress(exit, 'Escape')

#turtle.onkeypress(goRight, 'Right')

while(1):
    for i, ball in enumerate(balls):


        ball.sety(ball.ycor() + velocityY[i])
        ball.setx(ball.xcor() + velocityX[i])

        # Acceleration due to gravity
        velocityY[i] += gravity
        # Bounce off the ground
        if ball.ycor() > seeling:
            velocityY[i] = -velocityY[i]
        if ball.ycor() < ground:
            velocityY[i] = -velocityY[i] * energy_loss
            # Set ball to ground level to avoid it getting "stuck"
            ball.sety(ground)
        # Bounce off the walls (left and right)
        if ball.xcor() > wall or ball.xcor() < -(wall):
            velocityX[i] = -velocityX[i]
        #print(ball.position())
    
    
    window.update()
    






