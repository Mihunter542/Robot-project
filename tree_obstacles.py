# -*- coding: utf-8 -*-
from graphics import *
import random

class obstacles():
    """Chekcs which implementation has been picked and runs the respective functions."""
    def __init__(self, implementation, win, matrix):        
        self.implementation=implementation
        self.win=win
        self.matrix=matrix
        
        if implementation==1:
            self.tree()
            
        if implementation==2 or implementation==4:
            self.tree()
            self.grass()
            self.bush()
            self.stone()
            
        if implementation==3:
            self.read_document()
 
            
    
    """Opens Ambiente.txt and collects the necessary data."""
    def read_document(self):
        with open("Ambiente.txt",'r') as data_file:
            content=data_file.readlines()
            number=len(content)
            for i in range(0, number):
                line=content[i]
                data = line.split()
                
                if data[0] == "tree":
                    self.tree_pos=content[i+1]
                    self.tree_point=self.tree_pos.split()
                    self.tree()
                    
                elif data[0]=="grass":
                    e=i+1
                    
                    while content[e].split()[0]!="bush":                        
                        self.grass_pos=content[e]
                        self.grass_point=self.grass_pos.split()
                        self.grass()
                        e+=1
                        
                elif data[0]=="bush":
                    e=i+1
                    
                    while content[e].split()[0]!="stone":                        
                        self.bush_pos=content[e]
                        self.bush_point=self.bush_pos.split()
                        self.bush()
                        e+=1
                        
                elif data[0]=="stone":
                    e=i+1
                    
                    while e<number:                        
                        self.stone_pos=content[e]
                        self.stone_point=self.stone_pos.split()
                        self.stone()
                        e+=1
                           
                        
    """Defines the form the tree will take when draw."""                    
    def tree_format(self):        
        """Rectangle centered on the given point with 2*w width and 2*h height (tree log) and a circle centered on the upper face of the triangle with r radius (tree leaves)."""
        self.xmax, self.xmin = self.x+self.w, self.x-self.w
        self.ymax, self.ymin = self.y+self.h, self.y-self.h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.tree = Rectangle(p1,p2)
        self.tree.setFill('Brown')
        self.tree.draw(self.win)
        self.leaves=Circle(Point(self.x, self.ymin), self.radius)
        self.leaves.setFill("green")
        self.leaves.draw(self.win)
        
    
    """From the chosen implementation, the function gets the position of the tree (user input/random) and places it if possible."""
    def tree(self):        
        if self.implementation==1 or self.implementation==2:
            """10 width and 40 height rectangle"""
            self.w, self.h = 5, 20  
            self.x, self.y = 220, 320
            """20 radius circle"""
            self.radius=20
            self.tree_format()
            self.tree_matrix()
            
        if self.implementation==4:
            self.random_pos()
            """10 width and 40 height rectangle."""
            self.w, self.h = 5, 20    
            """20 radius circle"""
            self.radius=20
            self.x, self.y = self.pos_x, self.pos_y
            self.tree_format()
            self.tree_matrix()
            
        if self.implementation==3:
            """10 width and 40 height rectangle."""
            self.w, self.h = 5, 20  
            """20 radius circle"""
            self.radius=20
            self.x, self.y =int(self.tree_point[0]), int(self.tree_point[1])
            self.tree_format()
            self.tree_matrix()
            
    
    """Fills the matrix spots occupied by the tree with 1's."""        
    def tree_matrix(self):
        for i in range(int((self.y/10)-4),int((self.y/10)+2)):
            for e in range(int((self.x/10)-2),int((self.x/10)+2)):
                self.matrix[i,e]=1
            
    
    """Defines the form the grass will take when draw"""  
    def grass_format(self):
        """A triangle with a base of 10 and height of 20 is formed from the given point, which is then cloned twice. Each clone is moved, the first 10 to the right and the second 20 to the right."""
        self.firsttriangle=Polygon(Point(self.x1, self.y1),Point(self.x1+5, self.y1-20), Point(self.x1+10, self.y1))
        self.firsttriangle.setFill(color_rgb(69, 139, 0))
        self.firsttriangle.draw(self.win)
        self.secondtrinagle=self.firsttriangle.clone()
        self.secondtrinagle.move(10,0)
        self.secondtrinagle.draw(self.win)
        self.thirdtrinagle=self.firsttriangle.clone()
        self.thirdtrinagle.move(20,0)
        self.thirdtrinagle.draw(self.win)
        
        
    """From the chosen implementation, the function gets the amount and positions of the grass obstacles (user input/random) and places each one if possible."""  
    def grass(self):
        if self.implementation==2:
            self.x1, self.y1 = 200, 200
            self.grass_format()
            self.grass_matrix()
            
        if self.implementation==4:
            number=random.randint(1,5)
            
            for i in range(1, number):
                self.random_pos()
                self.x1, self.y1= self.pos_x, self.pos_y
                self.grass_verification()
                
                if self.place=="yes":
                    self.grass_format()
                    self.grass_matrix()
                    
                elif self.place=="no":
                    number+=1
                    break
                
        if self.implementation==3:
            self.x1, self.y1= int(self.grass_point[0]), int(self.grass_point[1])
            self.grass_verification()

            if self.place=="yes":
                self.grass_format()
                self.grass_matrix()
                
            elif self.place=="no":
                print("object faulty")
                
    
    """Fills the matrix spots occupied by the grass with 1's."""  
    def grass_matrix(self):
        for i in range(int((self.y1/10)-2), int(self.y1/10)):
            for e in range(int(self.x1/10), int((self.x1/10)+3)):
                self.matrix[i, e]=1
                
    
    """Checks whether the grass can be placed in the selected position (user input/random)."""
    def grass_verification(self):
        self.place="yes"
        for i in range(int((self.y1/10)-6), int((self.y1/10)+4)):
            for e in range(int((self.x1/10)-4), int((self.x1/10)+7)):
                if self.matrix[i,e]==1:
                    self.place="no"
                    
        if self.x1>=930 or self.x1<=40 or self.y1<=60 or self.y1>= 560:
            self.place="no"

    
    """Defines the form the bush will take when draw"""                            
    def bush_format(self):
        """A circle with 20 radius and centered on the given point is made and cloned twice. The clones are then moved, the first 30 to the right and the second 60 to the right."""
        self.firstcircle=Circle(Point(self.x1,self.y1), 20)
        self.firstcircle.setFill(color_rgb(22, 61, 34))
        self.firstcircle.draw(self.win)
        self.secondcircle=self.firstcircle.clone()
        self.secondcircle.move(30,0)
        self.secondcircle.draw(self.win)
        self.thirdcircle=self.firstcircle.clone()
        self.thirdcircle.move(60,0)
        self.thirdcircle.draw(self.win)
        
    
    """From the chosen implementation, the function gets the amount and positions of the bush obstacles (user input/random) and places each one if possible."""    
    def bush(self):
        
        if self.implementation==2:
            self.x1, self.y1= 400, 400
            self.bush_format()
            self.bush_matrix()
            
        if self.implementation==4:
            number=random.randint(1,5)
            
            for i in range(1, number):
                self.random_pos()
                self.x1, self.y1= self.pos_x, self.pos_y
                self.bush_verification()
                
                if self.place=="yes":
                    self.bush_format()
                    self.bush_matrix()
                    
                elif self.place=="no":
                    number+=1
                    break
                
        if self.implementation==3:            
            self.x1, self.y1=int(self.bush_point[0]), int(self.bush_point[1])
            self.bush_verification()
            
            if self.place=="yes":
                self.bush_format()
                self.bush_matrix()
                
            elif self.place=="no":
                print("object faulty")
           
    
    """Fills the matrix spots occupied by the bush with 1's."""  
    def bush_matrix(self):
        for i in range(int((self.y1/10)-2), int((self.y1/10)+2)):
            for e in range(int((self.x1/10)-2), int((self.x1/10)+8)):
                self.matrix[i, e]=1
                
    
    """Checks whether the bush can be placed in the selected position (user input/random)."""
    def bush_verification(self):
        self.place="yes"
        for i in range(int((self.y1/10)-6), int((self.y1/10)+6)):
            for e in range(int((self.x1/10)-6), int((self.x1/10)+12)):
                if self.matrix[i,e]==1:
                    self.place="no"
                
     
    """Defines the form the stone will take when draw."""  
    def stone_format(self):
        """Oval limited by a rectangle formed by the given point and one derived from it."""        
        self.oval=Oval(Point(self.x1, self.y1), Point(self.x1+100, self.y1+50))
        self.oval.setFill(color_rgb(138, 136, 136))
        self.oval.draw(self.win)
        
    
    """From the chosen implementation, the function gets the amount and positions of the stone obstacles (user input/random) and places each one if possible.""" 
    def stone(self):
        if self.implementation==2:
            self.x1, self.y1= 750, 120
            self.stone_format()
            self.stone_matrix()
            self.x1, self.y1= 200, 420
            self.stone_format()
            self.stone_matrix()
            
        if self.implementation==4:
            number=random.randint(1,5)
            
            for i in range(1, number):
                self.random_pos()
                self.x1, self.y1= self.pos_x, self.pos_y
                self.stone_verification()
                
                if self.place=="yes":
                    self.stone_format()
                    self.stone_matrix()
                    
                elif self.place=="no":
                    number+=1
                    break
                
        if self.implementation==3:
            self.x1, self.y1=int(self.stone_point[0]), int(self.stone_point[1])
            self.stone_verification()
            
            if self.place=="yes":
                self.stone_format()
                self.stone_matrix()
            
            elif self.place=="no":
                print("object faulty")
                
      
    """Fills the matrix spots occupied by the stone with 1's"""  
    def stone_matrix(self):
        for i in range(int(self.y1/10), int((self.y1/10)+5)):
            for e in range(int(self.x1/10), int((self.x1/10)+10)):
                self.matrix[i, e]=1
        
    
    """Checks whether the stone can be placed in the selected position (user input/random)."""
    def stone_verification(self):
        self.place="yes"
        for i in range(int((self.y1/10)-4), int((self.y1/10)+9)):
            for e in range(int((self.x1/10)-4), int((self.x1/10)+14)):
                if self.matrix[i,e]==1:
                    self.place="no"
                    
    
    """Used in the fourth implementation to get the random positions of each obstacle."""
    def random_pos(self):
        self.pos_x=random.randrange(60, 860, 10)
        self.pos_y=random.randrange(80,490, 10)