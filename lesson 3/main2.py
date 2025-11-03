import pgzrun
import random

WIDTH=500
HEIGHT=500

satellite = []
for i in range(8):
    s=Actor("satellite")
    s.pos = random.randint(50,500),random.randint(500,500)
    satellite.append(s)
def draw():
    screen.blit("galaxy",(0,0))
    numb=1
    for s in satellite:
        s.draw()
        screen.draw.text(str(numb),color="white",center=(s.x,s.y-20))
        numb+=1
pgzrun.go()