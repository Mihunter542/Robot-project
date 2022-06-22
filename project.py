# -*- coding: utf-8 -*-
from graphics import *
from tree_obstacles import *
from button import Button
from Harve_2 import Harve
from class_stations import *
import random
import math
import numpy as np
from itertools import product
    

"""First implemetation"""
def implemetation_1():
    
    """Implemetation window"""
    win=GraphWin("Project", 1000, 600)
    win.setBackground(color_rgb	(143,188,143))
    
    """Creates the stations"""
    s=Stations(win, 1)
    station1=Point(s.x1_pos, s.y1_pos)
    station2=Point(s.x2_pos, s.y2_pos)
    
    """Creates the quit button"""
    quitimplemetation_button=Button(win, Point(975,575), 50, 50, "Quit")
    
    """Creates navigation map"""
    mape=np.zeros((65, 105), dtype=np.int32)    
        
    """Creates tree and robot"""
    o=obstacles(1, win, mape)
    matrix=o.matrix
    np.set_printoptions(threshold=sys.maxsize)
    
    robot=Harve(win, matrix, station1, station2, "No")
    
    """Sets up the quit button and aligns the basket on the grid used by the robot"""
    while True:
        quitimplemetation_button.activate()
        pt=win.getMouse()
                
        if quitimplemetation_button.clicked(pt) == True:
            win.close()
            main()
            break
            
        else:
            """Deactivates the quit button and sends the converted coordinates to the robot"""
            robot.endx, robot.endy=round(pt.getX()/10) * 10, round(pt.getY()/10) * 10
            quitimplemetation_button.deactivate()            
            robot.place_basket()
    
    
"""Second implementation"""
def implemetation_2():
    
    """Implemetation window"""
    win=GraphWin("", 1000, 600)
    win.setBackground(color_rgb	(143,188,143))
    
    """Creates the stations"""
    s=Stations(win,2)
    station1=Point(s.x1_pos, s.y1_pos)
    station2=Point(s.x2_pos, s.y2_pos)
    station3=Point(s.x3_pos, s.y3_pos)
    
    """Creates the quit button"""
    quitimplemetation_button=Button(win, Point(975,575), 50, 50, "Quit")
    
    """Creates basic navigation map"""
    mape=np.zeros((65, 105), dtype=np.int32)
    
    """Creates fixed obstacles"""
    o=obstacles(2, win, mape)     
    matrix=o.matrix
    
    robot=Harve(win, matrix, station1, station2, station3)
    
    """Sets up the quit button and aligns the basket on the grid used by the robot"""
    while True:
        quitimplemetation_button.activate()
        pt=win.getMouse()
                
        if quitimplemetation_button.clicked(pt) == True:
            win.close()
            main()
            break
            
        else:
            """Deactivates the quit button and sends the converted coordinates to the robot"""
            robot.endx, robot.endy=round(pt.getX()/10) * 10, round(pt.getY()/10) * 10
            quitimplemetation_button.deactivate()            
            robot.place_basket()
        
    
"""Third implementation"""
def implemetation_3():
    win=GraphWin("", 1000, 600)
    win.setBackground(color_rgb	(143,188,143))
    
    """Creates the stations"""
    s=Stations(win, 3)
    station1=Point(s.x1_pos, s.y1_pos)
    station2=Point(s.x2_pos, s.y2_pos)
    station3=Point(s.x3_pos, s.y3_pos)
    
    """Creates the quit button"""
    quitimplemetation_button=Button(win, Point(975,575), 50, 50, "Quit")
    
    """Creates basic navigation map"""
    mape=np.zeros((65, 105), dtype=np.int32)
    
    """Creates the obstacles set in the .txt file and the robot"""
    o=obstacles(3, win, mape)
    matrix=o.matrix
    
    robot=Harve(win, matrix, station1, station2, station3)
    
    """Sets up the quit button and aligns the basket on the grid used by the robot"""
    while True:
        quitimplemetation_button.activate()
        pt=win.getMouse()
                
        if quitimplemetation_button.clicked(pt) == True:
            win.close()
            main()
            break
            
        else:
            """Deactivates the quit button and sends the converted coordinates to the robot"""
            robot.endx, robot.endy=round(pt.getX()/10) * 10, round(pt.getY()/10) * 10
            quitimplemetation_button.deactivate()            
            robot.place_basket()
            
            
"""Fourth implementation"""
def implemetation_4():
    
    win=GraphWin("", 1000, 600)
    win.setBackground(color_rgb	(143,188,143))
    
    """Creates the stations"""
    s=Stations(win, 4)
    station1=Point(s.x1_pos, s.y1_pos)
    station2=Point(s.x2_pos, s.y2_pos)
    station3=Point(s.x3_pos, s.y3_pos)
    
    """Creates the quit button"""
    quitimplemetation_button=Button(win, Point(975,575), 50, 50, "Quit")
    
    """Creates basic navigation map"""
    mape=np.zeros((65, 105), dtype=np.int32)
        
    """Creates the random obstacles and the robot"""
    o=obstacles(4, win, mape)
    matrix=o.matrix
    
    robot=Harve(win, matrix, station1, station2, station3)
    
    """Sets up the quit button and aligns the basket on the grid used by the robot"""
    while True:
        quitimplemetation_button.activate()
        pt=win.getMouse()
                
        if quitimplemetation_button.clicked(pt) == True:
            win.close()
            main()
            break
            
        else:
            """Deactivates the quit button and sends the converted coordinates to the robot"""
            robot.endx, robot.endy=round(pt.getX()/10) * 10, round(pt.getY()/10) * 10
            quitimplemetation_button.deactivate()            
            robot.place_basket()
            
    
def menu(win_menu):
    
    sky=Rectangle(Point(0,0), Point(1000, 370))
    grass=Rectangle(Point(0,370), Point(1000, 600))
    grass.setOutline(color_rgb(118, 172, 32))
    sky.setFill(color_rgb(10, 133, 205))
    sky.setOutline(color_rgb(10, 133, 205))
    grass.setFill(color_rgb(118, 172, 32))
    sky.draw(win_menu)
    grass.draw(win_menu)
    title = Text(Point(400, 150), "Newton's Apple Adventure")
    title.setFace("courier")
    title.setSize(33)
    title.setStyle("bold")
    image=Image(Point(400, 300), "menu_image_final.png")
    
    image.draw(win_menu)
    title.draw(win_menu)
    
    
"""Opens the menu to select the desired implementation"""
def main():
    win_menu=GraphWin("The robot that collects a basket", 1000, 600)
    menu(win_menu)
    
    imp1_button=Button(win_menu, Point(850,100), 120, 65, "Implemetation 1")
    imp1_button.activate()
    
    imp2_button=Button(win_menu, Point(850,200), 120, 65, "Implemetation 2")
    imp2_button.activate()
    
    imp3_button=Button(win_menu, Point(850,300), 120, 65, "Implemetation 3")
    imp3_button.activate()
    
    imp4_button=Button(win_menu, Point(850, 400), 120, 65, "Implemetation 4")
    imp4_button.activate()
    
    quit_button=Button(win_menu, Point(950,550), 50, 50, "Quit")
    quit_button.activate()
    
    pt=win_menu.getMouse()
    
    while True:
        if imp1_button.clicked(pt):
            win_menu.close()
            implemetation_1()
            break
        
        elif imp2_button.clicked(pt):
            win_menu.close()
            implemetation_2()
            break
        
        elif imp3_button.clicked(pt):
            win_menu.close()
            implemetation_3()
            break        
        
        elif imp4_button.clicked(pt):
            win_menu.close()
            implemetation_4()
            break
        
        elif quit_button.clicked(pt):
            win_menu.close()
            sys.exit()
            
main()