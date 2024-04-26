import time
import datetime
import turtle

# Creating Turtle for displaying time
tt1 = turtle.Turtle()
# Creating turtle for rectangular box
tt2 = turtle.Turtle()
# Creating turtle for displaying screen
screen=turtle.Screen()
screen.bgcolor("Pink")

# Importing current time
secs = datetime.datetime.now().second  
mins = datetime.datetime.now().minute  
hrs = datetime.datetime.now().hour 


tt2.pensize(2.5)
tt2.color('purple')
tt2.penup

# tt2.goto(15,-15,-15,15)  
# tt2.pendown()

for j in range(2):  
   tt2.forward(200)  
   tt2.left(90)  
   tt2.forward(70)  
   tt2.left(90)

tt1.hideturtle()

while True:
   tt1.hideturtle()
   tt1.clear

   tt1.write(str(hrs).zfill(2)+":"+str(mins).zfill(2)+":"+str(secs).zfill(2),font=("Bebas Neue",37,"bold"))
time.sleep(1)
secs += 1
if secs == 60:
   secs = 0 
   mins += 1
if mins == 60:
   mins = 0
   hrs += 1
if hrs == 13:
   hrs = 1




