from turtle import*
def nexus(x,y):
    penup()
    goto(x,y)
    pendown()
my_list=[[5,0,7,2,0,0,0,9,0],
           [0,0,6,0,3,0,7,0,1],
           [4,0,0,0,0,0,0,6,0],
           [1,0,0,4,9,0,0,0,7],
           [0,0,0,5,0,8,0,0,0],
           [8,0,0,0,2,7,0,0,5],
           [0,7,0,0,0,0,0,0,9],
           [2,0,9,0,8,0,6,0,0],
           [0,4,0,0,0,9,3,0,8]]
ans_list=[[5,1,7,2,6,4,8,9,3],
             [9,2,6,8,3,5,7,4,1],
             [4,8,3,9,7,1,5,6,2],
             [1,3,5,4,9,6,2,8,7],
             [7,9,2,5,1,8,4,3,6],
             [8,6,4,3,2,7,9,1,5],
             [3,7,8,6,4,2,1,5,9],
             [2,5,9,1,8,3,6,7,4],
             [6,4,1,7,5,9,3,2,8]] 
def num(u,v,z):
    nexus(u,v)
    write(z,align="center", font=("Arial", 15, "normal"))
def medium():
 pencolor("red")
 num(-160,150,"5")
 num(-160,70,"4")
 num(-160,30,"1")
 num(-160,-50,"8")
 num(-160,-130,"2")
 num(-120,-90,"7")
 num(-120,-170,"4")
 num(-80,150,"7")
 num(-80,110,"6")
 num(-80,-130,"9")
 num(-40,150,"2")
 num(-40,30,"4")
 num(-40,-10,"5")
 num(0,110,"3")
 num(0,30,"9")
 num(0,-50,"2")
 num(0,-130,"8")
 num(40,-10,"8")
 num(40,-50,"7")
 num(40,-170,"9")
 num(80,110,"7")
 num(80,-130,"6")
 num(80,-170,"3")
 num(120,150,"9")
 num(120,70,"6")
 num(160,110,"1")
 num(160,30,"7")
 num(160,-50,"5")
 num(160,-90,"9")
 num(160,-170,"8")

 def getcords(x,y):
  if (((x not in range(-180,-140)) or (y not in range(140,180) and y not in range(60,100) and y not in range(20,60) 
  and y not in range(-60,-20) and y not in range(-140,-100))) and (x not in range(-140,-100) or (y not in range(-100,-60) 
  and y not in range(-180,-140))) and (x not in range(-100,-60) or (y not in range(140,180) 
  and y not in range(100,140) and y not in range(-140,-100))) and (x not in range(-60,-20) or (y not in range(140,180) 
  and y not in range(20,60) and y not in range(-20,20))) and (x not in range(-20,20) or (y not in range(100,140) and y not in range(20,60) 
  and y not in range(-60,-20) and y not in range(-140,-100))) and (x not in range(20,60) or (y not in range(-20,20) 
  and y not in range(-60,-20) and y not in range(-180,-140))) and (x not in range(60,100) or (y not in range(100,140) 
  and y not in range(-180,-100))) and (x not in range(100,140) or (y not in range(140,180) and y not in range(60,100))) 
  and (x not in range(140,180) or (y not in range(100,140) and y not in range(20,60) 
  and y not in range(-100,-20) and y not in range(-180,-140)))):
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
