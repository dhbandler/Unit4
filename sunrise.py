#Daniel Bandler
#3/30/18
#sunrise.py -- makes the sun rise by the divine power of the lord Ra

from ggame import *


def moveSun():
    if sun
    data["frames"] = 0 #resets timer
    sun.x += 0
    sun.y += 50

def step():
    data["frames"] += 1
    if data["frames"] == 10:
        moveSun()

if __name__ == "__main__":
    
    data = {}
    data["frames"] = 0
    
    yellow = Color(0xFFFF00,1)
    orange = Color(0xFF8C00,1)
    red = Color(0xFF0000,1)
    lightgreen = Color(0x7CFC00,1)
    midgreen = Color(0x228B22,1)
    darkgreen = Color(0x006400,1)
    lightblue = Color(0x00BFFF,1)
    midblue = Color(0x7B68EE,1)
    darkblue = Color(0x191970,1)
    black = Color(0x000000,1)


    blackOutline = LineStyle(1,black)

    sun1 = CircleAsset(100,blackOutline,red)
    sun2 = CircleAsset(100,blackOutline,orange)
    sun3 = CircleAsset(100,blackOutline,yellow)
    earth1 = RectangleAsset(1000,400, blackOutline, darkgreen)
    earth2 = RectangleAsset(1000,400, blackOutline, midgreen)
    earth3 = RectangleAsset(1000,400, blackOutline, lightgreen)
    sky1 = RectangleAsset(1000,300, blackOutline, darkblue)
    sky2 = RectangleAsset(1000,300, blackOutline, midblue)
    sky3 = RectangleAsset(1000,300, blackOutline, lightblue)
    
    Sprite(sky1)
    Sprite(sun1,(350,250))
    Sprite(earth1,(0,300))


    
    App().run(step)



