from turtle import*
def nexus(x,y):
    penup()
    goto(x,y)
    pendown()
my_list=[[0,0,6,5,0,0,0,0,8],
           [0,9,5,0,0,0,0,2,0],
           [7,0,0,9,0,0,3,0,0],
           [0,0,0,0,4,0,2,7,0],
           [0,0,0,8,7,3,0,0,0],
           [0,7,9,0,5,0,0,0,0],
           [0,0,2,0,0,8,0,0,9],
           [0,5,0,0,0,0,8,1,0],
           [3,0,0,0,0,5,4,0,0]]
ans_list=[[1,3,6,5,2,4,7,9,8],
           [8,9,5,3,6,7,1,2,4],
           [7,2,4,9,8,1,3,5,6],
           [5,8,3,6,4,9,2,7,1],
           [2,6,1,8,7,3,9,4,5],
           [4,7,9,1,5,2,6,8,3],
           [6,4,2,7,1,8,5,3,9],
           [9,5,7,4,3,6,8,1,2],
           [3,1,8,2,9,5,4,6,7]]
def num(u,v,z):
    nexus(u,v)
    write(z,align="center", font=("Arial", 15, "normal"))
def extreme():
 pencolor("red")
 num(-160,70,"7")
 num(-160,-170,"3")
 num(-120,110,"9")
 num(-120,-50,"7")
 num(-120,-130,"5")
 num(-80,150,"6")
 num(-80,110,"5")
 num(-80,-50,"9")
 num(-80,-90,"2")
 num(-40,150,"5")
 num(-40,70,"9")
 num(-40,-10,"8")
 num(0,30,"4")
 num(0,-10,"7")
 num(0,-50,"5")
 num(40,-10,"3")
 num(40,-90,"8")
 num(40,-170,"5")
 num(80,70,"3")
 num(80,30,"2")
 num(80,-130,"8")
 num(80,-170,"4")
 num(120,110,"2")
 num(120,30,"7")
 num(120,-130,"1")
 num(160,150,"8")
 num(160,-90,"9")

 def getcords(x,y):
  if (((x not in range(-180,-140)) or (y not in range(60,100) and y not in range(-180,-140))) 
  and (x not in range(-140,-100) or (y not in range(100,140) and y not in range(-60,-20) 
  and y not in range(-140,-100))) and (x not in range(-100,-60) or (y not in range(100,180) 
  and y not in range(-100,-20))) and (x not in range(-60,-20) or (y not in range(140,180) 
  and y not in range(60,100) and y not in range(-20,20))) and (x not in range(-20,20) or (y not in range(-60,60))) 
  and (x not in range(20,60) or (y not in range(-20,20) 
  and y not in range(-100,-60) and y not in range(-180,-140))) and (x not in range(60,100) or (y not in range(20,100) 
  and y not in range(-180,-100))) and (x not in range(100,140) or (y not in range(100,140) and y not in range(20,60) 
  and y not in range(-140,-100))) and (x not in range(140,180) or (y not in range(140,180) and y not in range(-100,-60)))):
   t=(numinput(title='Enter a number',prompt="Your Number",minval=1,maxval=9))
   if x in range(-180,180):
    if y in range(-180,180):
     if x in range(-20,20):
      a=0
      if y in range(-20,20):
       b=0
       
       my_list[4][4]=int(t)
       
       
      if y in range(20,180):
       b=(int((y-20)/40)+1)*40 
       k=abs(int(b/40)-4)
       
       my_list[k][4]=int(t)
       
      if y in range(-180,-20):
       b=(int((y+20)/40)-1)*40  
       k=abs(int(b/40))+4
       
       my_list[k][4]=int(t)
       
     if y in range(-20,20):
         b=0
         if x in range(-180,-20):
             a=(int((x+20)/40)-1)*40  
             k=(int(a/40))+4
             my_list[4][k]=int(t)
             
         if x in range(20,180):
             a=(int((x-20)/40)+1)*40   
             k=(int(a/40))+4
             my_list[4][k]=int(t)
                       
     if x in range(20,180): 
         a=(int((x-20)/40)+1)*40
         if y in range(20,180):     
             b=(int((y-20)/40)+1)*40
             m=(int(a/40))+4
             k=abs(int(b/40)-4)
             
             my_list[k][m]=int(t)
             
         if y in range(-180,-20):
             b=(int((y+20)/40)-1)*40
             m=(int(a/40))+4
             k=abs(int(b/40)-4)
             
             my_list[k][m]=int(t)
                 
     if x in range(-180,-20):          
         a=(int((x+20)/40)-1)*40
         if y in range(20,180):             
             b=(int((y-20)/40)+1)*40
             m=(int(a/40))+4
             k=abs(int(b/40)-4)
             
             my_list[k][m]=int(t)
             
         if y in range(-180,-20):
             b=(int((y+20)/40)-1)*40
             m=(int(a/40))+4
             k=abs(int(b/40))+4
             
             my_list[k][m]=int(t)
     
     if my_list==ans_list:
         clear()
         nexus(0,0)
         pencolor("RED")
         write("You Win!",align="center", font=("Arial", 25, "normal"))
         
         done()
     
  hideturtle()
  pencolor("")
  nexus(a-17,b+17)
  begin_fill()
  setheading(0)
  forward(34)
  right(90)
  forward(34)
  right(90)
  forward(34)
  right(90)
  forward(34)
  fillcolor("light blue")
  end_fill()
  setheading(towards(a,b)) 
  nexus(a,b-10)
  pencolor("Black")
  write(int(t),align="center", font=("Arial", 15, "normal"))
   
   
    
 listen() 
 onscreenclick(getcords)
