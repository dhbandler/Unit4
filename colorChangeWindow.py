#Daniel
#3/28/18
#colorChangeWindow.py changes color randomly
from ggame import *
from random import randint

def mouseClick(event):
    num = randint(1,5)
    if num == 1:
        Sprite(color1)
    elif num == 2:
        Sprite(color2)
    elif num == 3:
        Sprite(color3)
    elif num == 4:
        Sprite(color4)
    else:
        Sprite(color5)

green = Color(0x006600,1)
brown = Color(0x8B4513,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)
red = Color(0xFF0000,1)
    
color1 = RectangleAsset(1000,1000,LineStyle(1,green),green)
color2 = RectangleAsset(1000,1000,LineStyle(1,brown),brown)
color3 = RectangleAsset(1000,1000,LineStyle(1,black),black)
color4 = RectangleAsset(1000,1000,LineStyle(1,yellow),yellow)
color5 = RectangleAsset(1000,1000,LineStyle(1,red),red)

App.listenMouseEvent("click", mouseClick)

App.run()