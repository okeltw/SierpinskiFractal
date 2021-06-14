# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 20:29:44 2021

@author: twoke
"""

from graphics import GraphWin, Point, Text
import random
import math

axis = (500, 500)

def PointText(win,x,y,text):
    offsets = (15, -10)
    size = 8
    p = Point(x,y)
    pt = Point(x+offsets[0],y+offsets[1])
    t = Text(pt, text)
    t.setSize(size)
    t.draw(win)
    p.draw(win)
    return p

def CalculateMove(current, target):
    deltaX = math.ceil((current.getX() - target.getX())/2)
    deltaY = math.ceil((current.getY() - target.getY())/2)
    return Point(current.getX() - deltaX,
                 current.getY() - deltaY)
 
def main():
    win = GraphWin("Triangles", axis[0], axis[1])
    A = PointText(win,50,450,'A')
    B = PointText(win,450,450, 'B')
    C = PointText(win,225,50,'C')
    
    pos = (random.randint(50,450), random.randint(50,450))
    points = [Point(pos[0],pos[1])]
    points[-1].draw(win)
    
    for iter in range(0,50000):
        dice = random.randint(1,3)
        if dice == 1: #A
            points.append(CalculateMove(points[-1],A))
            print('Towards A {} {}'.format(points[-1].getX(), points[-1].getY()))
        elif dice == 2: #B
            points.append(CalculateMove(points[-1],B))
            print('Towards B')
        elif dice == 3: #C
            points.append(CalculateMove(points[-1],C))
            print('Towards C')
        else:
            print('Unknown dice roll {}, skipping...'.format(dice))
            continue
        
        points[-1].draw(win)
        
        #win.getMouse()
            
            
    #PointText(win,50,50,'trace')
    win.getMouse()
    win.close()
        
main()
