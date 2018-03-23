#Daniel Bandler 
#3/22/18 
#monkeybanana.py - best game ever

from ggame import *
from random import randint

#Constants


ROWS = 16
COLS = 34
CELL_SIZE = 30

#moves monkey right 1 cell

def moveRight(event):
    if monkey.x < (COLS-1)*CELL_SIZE:
        monkey.x += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
            data["frames2"] = 0
            
#moves monket left 1 cell           
         
def moveLeft(event):
   if monkey.x > 0:
        monkey.x -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
            data["frames2"] = 0

 #moves monket down 1 cell  
 
def moveDown(event):
    if monkey.y < (ROWS-1)*CELL_SIZE:
        monkey.y += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
            data["frames2"] = 0
            
 #moves monket up 1 cell
           
def moveUp(event):
    if monkey.y > 0:
        monkey.y -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()
            data["frames2"] = 0
            
#moves banana randomly around jungle

def moveBanana():
    data["frames"] = 0 #resets timer
    banana.x = randint(0,COLS-1)*CELL_SIZE
    banana.y = randint(0,ROWS-1)*CELL_SIZE
    
#Updates the score by 1, makes score box
    
def updateScore():    
    data["score"] += 1 
    data["scoreText"].destroy() #remove old writing
    scoreBox = TextAsset("Score = "+str(data["score"]))
    data["scoreText"] = Sprite(scoreBox,(0,ROWS*CELL_SIZE+4)) #puts new writing box

#timer for the banana (And Monkey's starvation, WIP). Keeps track of how many frames 
#have happened and moves banana if it has been > 300 frames since last move

def step():

    data["frames2"] += 1
    if data["frames2"] == 600:
        Sprite(diedBox)
        #Need to end progam
        
    data["frames"] += 1
    if data["frames"] == 200:
        moveBanana()

if __name__== "__main__":
    
    #hold variables in a dictionary
    data = {}
    data["score"] = 0
    data["frames"] = 0
    data["frames2"] = 0
    
    #Colors:
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    black = Color(0x000000,1)
    yellow = Color(0xFFFF00,1)
    red = Color(0xFF0000,1)
    
    #graphics
    
    jungleBox = RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(1,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),brown)
    bananaBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),yellow)
    scoreBox = TextAsset("Score = 0")
    diedBox = TextAsset("You Died by Starvation!", fill=red,style= "bold 50pt Georgia")

    #sprites things
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox)
    banana = Sprite(bananaBox, (CELL_SIZE*COLS/2,CELL_SIZE*ROWS/2))
    data["scoreText"] = Sprite(scoreBox, (0,ROWS*CELL_SIZE+4))
   
   #listens for keys
   
    App().listenKeyEvent("keydown", "right arrow", moveRight)
    App().listenKeyEvent("keydown", "down arrow", moveDown)
    App().listenKeyEvent("keydown", "left arrow", moveLeft)
    App().listenKeyEvent("keydown", "up arrow", moveUp)
    
    
    App().run(step)
    