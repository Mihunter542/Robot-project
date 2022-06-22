# -*- coding: utf-8 -*-
import random
from graphics import *

class Stations():
    """Chekcs which implementation has been picked and runs the respective functions."""
    def __init__(self, win, implemetation):
        self.implemetation=implemetation
        self.win=win
        
        if implemetation==1:
           self.station_1()
           self.station_2()
            
        if implemetation==2 or implemetation==4:
            self.station_1()
            self.station_2()
            self.battery_station()
            
        if implemetation==3:
            self.read_document()
            self.station_1()
            self.station_2()
            self.battery_station()
            
            
    """Opens Ambiente.txt and collects the necessary data."""        
    def read_document(self):        
        with open("Ambiente.txt",'r') as data_file:
            content=data_file.readlines()
            number=len(content)
            for i in range(0, number):
                line=content[i]
                data = line.split()
                
                if data[0] == "stations":
                    self.st1_pos=content[i+1]
                    self.point1=self.st1_pos.split()
                    
                    self.st2_pos=content[i+2]
                    self.point2=self.st2_pos.split()
                    
                    self.st3_pos=content[i+3]
                    self.point3=self.st3_pos.split()
                    
   
    """Defines and draws station 1."""
    def station_1(self):        
        if self.implemetation==1 or self.implemetation==2:    
            self.station_1=Rectangle(Point(0 , 500), Point(40 ,540))
            self.station_1.setFill("black")
            self.station_1.draw(self.win)
            self.x1_pos, self.y1_pos= 20, 520
            
        if self.implemetation==4:
            self.random_positions()
            self.station_1=Rectangle(Point(self.x-20 , self.y-20), Point(self.x+20 ,self.y+20))
            self.station_1.setFill("black")
            self.station_1.draw(self.win)
            self.x1_pos, self.y1_pos=self.x, self.y
            
        if self.implemetation==3:
            self.station_1=Rectangle(Point(int(self.point1[0])-20 , int(self.point1[1])-20), Point(int(self.point1[0])+20 ,int(self.point1[1])+20))
            self.station_1.setFill("black")
            self.station_1.draw(self.win)
            self.x1_pos, self.y1_pos=int(self.point1[0]), int(self.point1[1])
            
            
    """Defines and draws station 2."""
    def station_2(self):
        
        if self.implemetation==1 or self.implemetation==2:
            self.station_2=Rectangle(Point(1000 , 100), Point(960 ,140))
            self.station_2.setFill("black")
            self.station_2.draw(self.win)
            self.x2_pos, self.y2_pos= 980, 120
           
        if self.implemetation==4:
            self.random_positions()
            self.verif_stations2()
            self.station_2=Rectangle(Point(self.x-20 , self.y-20), Point(self.x+20 ,self.y+20))
            self.station_2.setFill("black")
            self.station_2.draw(self.win)
            self.x2_pos, self.y2_pos=self.x,self.y
            
        if self.implemetation==3:
            self.station_2=Rectangle(Point(int(self.point2[0])-20 , int(self.point2[1])-20), Point(int(self.point2[0])+20 ,int(self.point2[1])+20))
            self.station_2.setFill("black")
            self.station_2.draw(self.win)
            self.x2_pos, self.y2_pos=int(self.point2[0]), int(self.point2[1])
           
            
    """Defines and draws the charging station (station 3)."""
    def battery_station(self):
        if self.implemetation==2:
            self.battery_station=Rectangle(Point(960 , 50), Point(1000 ,90))
            self.battery_station.setFill("black")
            lightning=Image(Point(980, 70), "sewy_final.png")
            self.battery_station.draw(self.win)
            lightning.draw(self.win)
            self.x3_pos, self.y3_pos= 980, 70
            
        if self.implemetation==4:
            self.random_positions()
            self.verif_stations3()
            self.battery_station=Rectangle(Point(self.x-20 , self.y-20), Point(self.x+20 ,self.y+20))
            self.battery_station.setFill("black")
            self.battery_station.draw(self.win)
            lightning=Image(Point(self.x, self.y), "sewy_final.png")
            lightning.draw(self.win)
            self.x3_pos, self.y3_pos=self.x, self.y
                        
        if self.implemetation==3:
            self.battery_station=Rectangle(Point(int(self.point3[0])-20 , int(self.point3[1])-20), Point(int(self.point3[0])+20 ,int(self.point3[1])+20))
            self.battery_station.setFill("black")
            self.battery_station.draw(self.win)
            lightning=Image(Point(int(self.point3[0]),int(self.point3[1])), "sewy_final.png")
            lightning.draw(self.win)
            self.x3_pos, self.y3_pos=int(self.point3[0]), int(self.point3[1])
      
     
    """Makes sure station 2 doesn't get placed on top of station 1 in the fourth implementation."""
    def verif_stations2(self):        
        while self.x<=self.x1_pos+20 and self.x>=self.x1_pos-20 and self.y<=self.y1_pos+20 and self.y>=self.y1_pos-20:
            self.random_positions()
            
         
    """Makes sure station 3 doesn't get placed on top of station 1 or station 2 in the fourth implementation."""
    def verif_stations3(self):
        while self.x<=self.x1_pos+20 and self.x>=self.x1_pos-20 and self.y<=self.y1_pos+20 and self.y>=self.y1_pos-20:
            self.random_positions()
            
        while self.x<=self.x2_pos+20 and self.x>=self.x2_pos-20 and self.y<=self.y2_pos+20 and self.y>=self.y2_pos-20:
            self.random_positions()
            
      
    """Randomises the positions of the stations in the fourth implementation."""
    def random_positions(self): 
        """Picks one of the four borders of the window and then places the station in a random position in that line."""
        line=random.randint(1, 4)
        
        if line==1:
            self.x=20
            self.y=random.randrange(20,580, 10)
            
        elif line==2:
            self.x=980
            self.y=random.randrange(20,530, 10)
            
        elif line==3:
            self.x=random.randrange(20, 980, 10)
            self.y=20
            
        elif line==4:
            self.x=random.randrange(20, 930, 10)
            self.y=580