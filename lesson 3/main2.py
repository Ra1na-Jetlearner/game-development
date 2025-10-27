import pgzrun
import random

WIDTH=500
LENTH=500

satellite = []
for i in range(8):
    s=Actor("satellite")
    s.pos = random.randint(0,500),random.randint(0,500)
    satellite.append(s)
def draw():
    screen.blit("galaxy",(0,0))
    for s in satellite:
        s.draw()
pgzrun.go()