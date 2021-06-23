from turtle import*
import easy  
import medium
import extreme
my_list=[[0,7,0,0,2,0,0,4,6],
           [0,6,0,0,0,0,8,9,0],
           [2,0,0,8,0,0,7,1,5],
           [0,8,4,0,9,7,0,0,0],
           [7,1,0,0,0,0,0,5,9],
           [0,0,0,1,3,0,4,8,0],
           [6,9,7,0,0,2,0,0,8],
           [0,5,8,0,0,0,0,6,0],
           [4,3,0,0,8,0,0,7,0]]
hideturtle()
bgcolor("light blue")
title("SUDOKU")
speed(0)
color("Black")
def nexus(x,y):
    penup()
    goto(x,y)
    pendown()
setup (width=440, height=426)
nexus(0,110)

pencolor("black")
write("SUDOKU",align="center", font=("Arial", 36, "normal"))
nexus(210,-203)
write("By ANHYDROUS-H20",align="right", font=("Arial", 15, "normal"))
nexus(0,50)
write("Choose Difficulty",align="center", font=("Arial", 10, "normal"))
nexus(-65,35)
begin_fill()
forward(130)
circle(-20,180)
forward(130)
circle(-20,180)
fillcolor("#00FFFF")
end_fill()
nexus(0,4)
write("Easy",align="center", font=("Arial", 15, "normal"))
nexus(-65,-12)
begin_fill()
forward(130)
circle(-20,180)
forward(130)
circle(-20,180)
fillcolor("#00FF00")
end_fill()
nexus(0,-42)
write("Medium",align="center", font=("Arial", 15, "normal"))
nexus(-65,-59)
begin_fill()
forward(130)
circle(-20,180)
forward(130)
circle(-20,180)
fillcolor("red")
end_fill()
nexus(0,-89)
write("Extreme",align="center", font=("Arial", 15, "normal"))


def homecords(x,y):
    if x in range(-85,85) and y in range(-5,35):
        draw()
        easy.easy()
        
    elif x in range(-85,85) and y in range(-51,-12):
        draw()
        medium.medium()
    elif x in range(-85,85) and y in range(-98,-58):
        draw()
        extreme.extreme()
listen()
onscreenclick(homecords)

def draw():
 clear()
 penup()
 speed(0)
 setx(-180)
 sety(180)
 pendown()
 forward(360)
 right(90)
 forward(360)
 right(90)
 forward(360)
 right(90)
 forward(360)
 nexus(-60,180)
 pensize("3")
 pencolor("blue")
 back(360)
 nexus(60,-180)
 forward(360)
 nexus(-180,60)
 right(90)
 forward(360)
 nexus(180,-60)
 right(180)
 forward(360)
 pensize("1")
 pencolor("grey")
 nexus(-140,180)
 left(90)
 forward(360)
 nexus(-100,-180)
 left(180)
 forward(360)
 nexus(-20,180)
 left(180)
 forward(360)
 nexus(20,-180)
 left(180)
 forward(360)
 nexus(100,180)
 left(180)
 forward(360)
 nexus(140,-180)
 left(180)
 forward(360)
 nexus(180,140)
 left(90)
 forward(360)
 nexus(-180,100)
 backward(360)
 nexus(180,20)
 forward(360)
 nexus(-180,-20)
 backward(360)
 nexus(180,-100)
 forward(360)
 nexus(-180,-140)
 backward(360)

def num(u,v,z):
    nexus(u,v)
    write(z,align="center", font=("Arial", 15, "normal"))

 
done()
 
