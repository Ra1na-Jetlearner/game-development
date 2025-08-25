import pgzrun
import random


WIDTH=850
HEIGHT=550

ali=Actor("alien2")
ali.pos = (random.randint(0,750), random.randint(0,450))

def draw():
    screen.fill(color=(139,51,106))
    ali.draw()




pgzrun.go()