import pgzrun
import random

WIDTH=800
HEIGHT=567

ITEMS=["batteryimg","bottleimg","chipsimg","bagimg"]
main_item="paperimg"
selected_item=[]
Actors=[]
level=1

def draw():
    screen.fill("orange")
    screen.blit("newbg",(0,0))
    for a in Actors:
        a.draw()

def setup():
    
    selected_item.append(main_item)
    for i in range (level):
        random_item=random.choice(ITEMS)
        selected_item.append(random_item)
    
    for i in range(level+1):
        idk=Actor(selected_item[i])
        Actors.append(idk)
        idk.pos=random.randint(0,800),50

def update():
    pass


setup()
pgzrun.go()