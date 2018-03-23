#Daniel Bandler 
#3/22/18 
#monkeybanana.py - best game ever

from ggame import *
from random import randint

#Constants


ROWS = 16
COLS = 34
CELL_SIZE = 30

def moveRight(event):
    if monkey.x < (COLS-1)*CELL_SIZE:
        monkey.x += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
         
def moveLeft(event):
   if monkey.x > 0:
        monkey.x -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
           
def moveDown(event):
    if monkey.y < (ROWS-1)*CELL_SIZE:
        monkey.y += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
           
def moveUp(event):
    if monkey.y > 0:
        monkey.y -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()

def moveBanana():
    banana.x = randint(0,COLS-1)*CELL_SIZE
    banana.y = randint(0,ROWS-1)*CELL_SIZE
    updateScore()
    
def updateScore():    
    data["score"] += 1
    data["scoreText"].destroy() #remove old writing
    scoreBox = TextAsset("Score = "+str(data["score"]))
    data["scoreText"] = Sprite(scoreBox,(0,ROWS*CELL_SIZE+4))

if __name__== "__main__":
    
    #hold variables in a dictionary
    data = {}
    data["score"] = 0
    
    #Colors:
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    black = Color(0x000000,1)
    yellow = Color(0xFFFF00,1)
    
    jungleBox = RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(1,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),brown)
    bananaBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),yellow)
    scoreBox = TextAsset("Score = 0")

    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox)
    banana = Sprite(bananaBox, (CELL_SIZE*COLS/2,CELL_SIZE*ROWS/2))
    data["scoreText"] = Sprite(scoreBox, (0,ROWS*CELL_SIZE+4))
   
    App().listenKeyEvent("keydown", "right arrow", moveRight)
    App().listenKeyEvent("keydown", "down arrow", moveDown)
    App().listenKeyEvent("keydown", "left arrow", moveLeft)
    App().listenKeyEvent("keydown", "up arrow", moveUp)
    
    
    App().run()
    