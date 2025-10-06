import pgzrun
import random

WIDTH = 670
HEIGHT = 670

def draw():
    screen.blit("galaxy",(0,0))
    for gab in satellites:
        gab.draw()

satellites = [ ]

for i in range(8):
    gab = Actor("satellite")
    gab.pos = (random.randint(0,670)),(random.randint(0,670))
    satellites.append(gab)

pgzrun.go()
