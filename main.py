import os
import turtle

wn=turtle.Screen() #defining screen
wn.title("Pong by Will Chamberlain")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stops window form automatically updtaing se the code can do it when needd

#SCORE
score_a = 0
score_b= 0



#PADDLE A 
paddle_a = turtle.Turtle() 
paddle_a.speed(0) #speed of its animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) 
paddle_a.penup()
paddle_a.goto(-350, 0) #where it starts 



#PADDLE B
paddle_b = turtle.Turtle() 
paddle_b.speed(0) #speed of its animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.penup()
paddle_b.goto(350, 0) #where it starts 


#BALL
ball = turtle.Turtle() 
ball.speed(0) #speed of its animation
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) #where it starts 
ball.dx = 1.5 #d is for delta moves two pixels
ball.dy = -1.5

#PEN (TURTLE)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #only wants to see the text
pen.goto(0,260)
pen.write("Player A: 0     Player B: 0", align="center", font=("Courier", 24, "normal"))



#FUNCTION
def paddle_a_up():
  y = paddle_a.ycor() #assigns y cooridnate to variable 
  y += 20 #adds 20 pixels to y coordinate 
  paddle_a.sety(y)


def paddle_a_down():
  y = paddle_a.ycor() 
  y -= 20 
  paddle_a.sety(y)



def paddle_b_up():
  y = paddle_b.ycor() #assigns y cooridnate to variable 
  y += 20 #adds 20 pixels to y coordinate 
  paddle_b.sety(y)


def paddle_b_down():
  y = paddle_b.ycor() 
  y -= 20 
  paddle_b.sety(y)

#KEYBOARD BINDING
wn.listen() #window listens for keyboard movements 
wn.onkeypress(paddle_a_up, "w") #w is the key they press
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") #Up is up arrow key
wn.onkeypress(paddle_b_down, "Down")


  
#MAIN GAME LOOP
while True:
  wn.update() #updates screen 
  




  #MOVE THE BALL
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)


  #BORDER CHECKING
  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1 #reverses the direction 
    os.system("afplay bounce.wav&")
  
  elif ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1 

  if ball.xcor() > 390:
    ball.goto(0, 0) #reverse direction 
    ball.dx *= -1
    score_a +=1
    pen.clear()
    pen.write("Player A: {}     Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) #updates scoreboard 

  elif ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dy *= -1 
    score_b+=1
    pen.clear()
    pen.write("Player A: {}     Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

  #COLLISIONS

  if (ball.xcor() >340 and ball.xcor() <350)  and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor()> paddle_b.ycor()-40 ):  #340 is the edges touching , 350 is for edges,  40 is at the top or bottom of the paddle 
    ball.setx(340)
    ball.dx *=-1


  elif (ball.xcor() < -340 and ball.xcor() >-350)  and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor()> paddle_a.ycor()-40 ):  #340 is the edges touching , 350 is for edges,  40 is at the top or bottom of the paddle 
    ball.setx(-340)
    ball.dx *=-1







  
