# -*- coding: utf-8 -*-
from graphics import *
import math
import time
import numpy as np

class Harve:    
    """Simulates the robot, its movement and battery."""
    def __init__(self, win, matrix, station1, station2, station3):        
        """Creates the robot, with a format of a circle"""
        self.robot=Circle(Point(20, 520), 20)
        self.robot.setFill("white")
                
        """Creates an indicator for the battery of the robot."""
        self.br1=Rectangle(Point(26, 514), Point(29, 508))
        self.br1.setFill("orange")
        self.br2=self.br1.clone()
        self.br2.move(-5, 0)
        self.br3=self.br1.clone()
        self.br3.move(-10, 0)
        self.br4=self.br1.clone()
        self.br4.move(-15, 0)
        self.bb=Rectangle(Point(10, 515), Point(30, 507))
        self.bb.setFill("black")    
        
        """Creates a light to indicate if the robot has collected an apple."""
        self.loaded=Circle(Point(20, 530), 5)
        self.loaded.setFill("black")  
           
        """Creates the center of the robot as a point."""
        self.point=Point(20, 520)
        
        """Connects everything in a list."""
        self.list=[self.point, self.robot, self.bb, self.br4, self.br3, self.br2, self.br1, self.loaded]
        
        self.win=win
        self.x1_pos, self.y1_pos=station1.getX(), station1.getY()
        self.x2_pos, self.y2_pos=station2.getX(), station2.getY()
        
        """Checks if the implementation being ran will use the battery."""
        if station3=="No":
            self.bat=False
            self.x3_pos, self.y3_pos=0, 0
            
        else:
            self.bat=True
            self.x3_pos, self.y3_pos=station3.getX(), station3.getY()
        
        self.total=6400        
        self.matrix=matrix        
        self.dx, self.dy, self.endx, self.endy=0, 0, 0, 0

        """Draws the robot"""
        for i in self.list[1:8]:
            i.draw(win)
             
            
    """Moves the robot and updates the energy remaining in the battery."""
    def dislocation(self, dx, dy):
        for e in range(1,11):
            for i in self.list:
                i.move(dx, dy)
            
            self.total-=math.sqrt(dx**2+dy**2)
            update(170)
        
     
    """Simulates the battery of the robot."""
    def battery(self):
        """Checks if the battery is being used in the current implementation."""
        if self.bat == True:
            
            """Changes the colour of the indicators when the battery hits 3/4, 1/2 and 1/4 of its remaining energy."""
            if self.total<=4800:
                self.br1.setFill("black")
                
            if self.total<=3200:
                self.br2.setFill("black")
            
            """The robot hits 1/4 energy and starts moving to the charging station."""
            if self.total<=1600:
                self.br3.setFill("black")
                self.startx, self.starty=self.point.getX(), self.point.getY()
                self.endx, self.endy=self.x3_pos, self.y3_pos
                self.move_total()        
                
                """The battery is recharged and the robot resumes its original trajectory."""                
                if self.point.getX()==self.x3_pos and self.point.getY()==self.y3_pos:
                    time.sleep(1)
                    
                    for i in self.list[3:7]:
                        i.setFill("orange")
                        time.sleep(0.5)
                        
                    self.total=6400
                    
                    if self.b==True:
                        self.endx=self.tempx
                        self.endy=self.tempy
                        self.go(True)
                        
                    else:
                        self.nearest()
                        
            """Running out of energy."""
            if self.total<=0:
                self.br4.setFill("black")
                time.sleep(50)
            
    
    """The movement commands move the robot until it's aligned with the respective axis of the target location's coordinates."""
    def right(self):
        """The robot moves to the right."""
        if self.point.getX()<self.endx:
            self.dx=1
            self.dy=0
            self.verification_right()  
            
            if self.r==1:
                self.dodge_right()
                
            else:
                self.dislocation(self.dx, self.dy)
                update(170)
                self.battery()
            
            
    def left(self):
        """The robot moves to the left."""
        if self.point.getX()>self.endx:
            self.dx=-1
            self.dy=0
            self.verification_left()  
            
            if self.l==1:                
                self.dodge_left()
                
            else:                
                self.dislocation(self.dx, self.dy)
                update(170)
                self.battery()

            
    def up(self):
        """The robot moves up."""
        if self.point.getY()>self.endy:
            self.dx=0
            self.dy=-1
            self.verification_up()  
            
            if self.u==1:                
                self.dodge_up()
                
            else:                
                self.dislocation(self.dx, self.dy)
                update(170)
                self.battery()
             
            
    def down(self):
        """The robot moves down."""     
        if self.point.getY()<self.endy:
            self.dx=0
            self.dy=1            
            self.verification_down() 
            
            if self.d==1:                
                self.dodge_down()    
                
            else:                
                self.dislocation(self.dx, self.dy)
                update(170)
                self.battery()
             
                
    """Diagonal movement commands. A check for an obstacle diagonally from the robot is ran to prevent issues."""        
    def right_up(self):
        """The robot moves up and to the right."""        
        while self.point.getX()<self.endx and self.point.getY()>self.endy:
            self.dx=1
            self.dy=-1            
            self.verification_up()  
            self.verification_right() 
            
            if self.u==1:                
                self.dodge_up()
                
            elif self.r==1:                
                self.dodge_right()
            
            elif self.matrix[round(self.point.getY()/10)-3, round(self.point.getX()/10)+2]==1:
                self.dodge_up()
                
            else:
                self.dislocation(self.dx, self.dy)
                update(170)
                self.battery()

                         
    def right_down(self):
        """The robot moves down and to the right."""        
        while self.point.getX()<self.endx and self.point.getY()<self.endy:
            self.dx=1
            self.dy=1            
            self.verification_down()  
            self.verification_right() 
            
            if self.d==1:                
                self.dodge_down()  
                
            elif self.r==1:                
                self.dodge_right()
            
            elif self.matrix[round(self.point.getY()/10)+2, round(self.point.getX()/10)+2]==1:
                self.dodge_down()
                
            else:
                self.dislocation(self.dx, self.dy)
                update(170)
                self.battery()
         
            
    def left_up(self):
        """The robot moves up and to the left."""        
        while self.point.getX()>self.endx and self.point.getY()>self.endy:
            self.dx=-1
            self.dy=-1            
            self.verification_up()  
            self.verification_left() 
            
            if self.u==1:                
                self.dodge_up()    
                
            elif self.l==1:                
                self.dodge_left()
            
            elif self.matrix[round(self.point.getY()/10)-3, round(self.point.getX()/10)-3]==1:
                self.dodge_up()
                
            else:
                self.dislocation(self.dx, self.dy)
                update(170)
                self.battery()
            
            
    def left_down(self):
        """The robot moves down and to the left."""        
        while self.point.getX()>self.endx and self.point.getY()<self.endy:
            self.dx=-1
            self.dy=1            
            self.verification_down()  
            self.verification_left() 
            
            if self.d==1:                
                self.dodge_down()  
                
            elif self.l==1:                
                self.dodge_left()
                
            elif self.matrix[round(self.point.getY()/10)+2, round(self.point.getX()/10)-3]==1:
                self.dodge_down()
                
            else:                
                self.dislocation(self.dx, self.dy)
                update(170)
                self.battery()
                  
                
    """Groups up the movement commands for ease of use."""            
    def move_total(self):
        self.diagonal()
        
        
        """Between each movement, the robot checks whether moving diagonally would be better."""
        self.right()
        self.diagonal()
        self.left()
        self.diagonal()
        self.up()
        self.diagonal()
        self.down()  
        self.diagonal()
            
    
    """Diagonal movement check."""
    def diagonal(self):
        if self.point.getX()!=self.endx and self.point.getY()!=self.endy:
            self.right_up()
            self.left_down()
            self.right_down()
            self.left_up()
             
            
    """Verification commands for the 4 main directions, they check the matrix positions in said directions to see if there are obstacles."""
    def verification_right(self):   
        self.r=0
        for i in range(round(self.point.getY()/10)-2, round(self.point.getY()/10)+2):                    
            if self.matrix[i, round(self.point.getX()/10)+2]==1 or self.point.getX()>=980:
                self.r=1                
                break
            
            
    def verification_left(self):
        self.l=0
        for i in range(round(self.point.getY()/10)-2, round(self.point.getY()/10)+2):
            if self.matrix[i, round(self.point.getX()/10)-3]==1 or self.point.getX()<=20:
                self.l=1                
                break
        
        
    def verification_up(self):   
        self.u=0
        for e in range(round(self.point.getX()/10)-2, round(self.point.getX()/10)+2): 
            if self.matrix[round(self.point.getY()/10)-3, e]==1 or self.point.getY()<=20:
                self.u=1                
                break
        
        
    def verification_down(self):  
        self.d=0
        for e in range(round(self.point.getX()/10)-2, round(self.point.getX()/10)+2):            
            if self.matrix[round(self.point.getY()/10)+2, e]==1 or self.point.getY()>=580:
                self.d=1                
                break    
    
    
    """Dodge commands for the 4 main directions. These move the robot if an obstacle is found in said direction (dodge_right for example will move the robot if an obstacle is to its right)."""
    def dodge_right(self):        
        self.verification_up()
        self.verification_down()
        
        if self.starty>=self.endy and self.u==0:
            self.dislocation(0, -1)   
            update(170)
            self.battery()
            self.verification_up()
                           
        elif self.d==0:            
            self.dislocation(0, 1)
            update(170)
            self.battery()
            self.verification_down()
                    
            
    def dodge_left(self):        
        self.verification_up()
        self.verification_down()
            
        if self.starty>=self.endy and self.u==0:
            self.dislocation(0, -1)   
            update(170)
            self.battery()
            self.verification_up()
                           
        elif self.d==0:            
            self.dislocation(0, 1)
            update(170)
            self.battery()
            self.verification_down()
                
            
    def dodge_up(self):        
        self.verification_right()
        self.verification_left()
        
        if self.startx<=self.endx and self.r==0:           
            self.dislocation(1, 0)  
            update(170)
            self.battery()
            self.verification_right()
                      
        elif self.l==0:           
            self.dislocation(-1, 0)
            update(170)
            self.battery()
            self.verification_left()
                
              
    def dodge_down(self):        
        self.verification_right()
        self.verification_left()
        
        if self.startx<=self.endx and self.r==0:           
            self.dislocation(1, 0)  
            update(170)
            self.battery()
            self.verification_right()
                      
        elif self.l==0:           
            self.dislocation(-1, 0)
            update(170)
            self.battery()
            self.verification_left()
            
                
    """Checks which station is closest and moves towards it after collecting the basket."""
    def nearest(self):
        dist_station_1=math.sqrt((self.x1_pos-self.point.getX())**2+(self.y1_pos-self.point.getY())**2)
        dist_station_2=math.sqrt((self.x2_pos-self.point.getX())**2+(self.y2_pos-self.point.getY())**2)
        
        if dist_station_1<=dist_station_2:
            self.endx=self.x1_pos
            self.endy=self.y1_pos
            self.go(False)
            
        else:
            self.endx=self.x2_pos
            self.endy=self.y2_pos
            self.go(False)
    
    
    """Places the basket."""
    def place_basket(self):
        self.bcheck=True
        
        bds1=math.sqrt((self.x1_pos-self.endx)**2+(self.y1_pos-self.endy)**2)
        bds2=math.sqrt((self.x2_pos-self.endx)**2+(self.y2_pos-self.endy)**2)        
        if self.bat==True:
            bds3=math.sqrt((self.x3_pos-self.endx)**2+(self.y3_pos-self.endy)**2)
        else:
            bds3=40
        
        """Checks if the basket location is valid."""
        for i in range(round((self.endy/10)-2), round((self.endy/10)+2)):
            for e in range(round((self.endx/10)-2), round((self.endx/10)+2)):
                """Makes sure the basket can be accessed by the robot and can't be placed on a station or inside of the quit button."""
                if self.matrix[i, e]==1 or self.endx>980 or self.endx<20 or self.endy>580 or self.endy<20 or (self.endx>930 and self.endy>530) or bds1<40 or bds2<40 or bds3<40:
                    self.bcheck=False
                    break
        
        """If the location is valid, the basket will be placed there."""
        if self.bcheck==True:
            """Draws the basket."""                    
            self.basket_fruit=Rectangle(Point(self.endx-10, self.endy+10), Point(self.endx+10, self.endy-10))
            self.basket_fruit.setFill("red")
            self.basket_fruit.draw(self.win)
            self.go(True)
            
            
    """Main movement command."""
    def go(self, b):
        self.b=b 
            
        """Saves the trajectory startpoint and endpoint so the original trajectory can be resumed after the robot goes to the charging station."""
        self.tempx, self.tempy=self.endx, self.endy
        self.startx, self.starty=self.point.getX(), self.point.getY()       
          
        """Starts the robot's movement and loops the list of movement commands until the robot reaches its destination."""
        while self.point.getX()!=self.endx or self.point.getY()!=self.endy:
            self.move_total()         
         
        time.sleep(0.5)
        
        """The robot reaches the basket and collects the apple."""
        if self.b==True:
            self.basket_fruit.undraw()
            self.loaded.setFill("red")
            self.nearest()
        else:
           self.loaded.setFill("black")