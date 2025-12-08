import pgzrun
import random

WIDTH=800
HEIGHT=670

ITEMS=["batteryimg","bottleimg","chipsimg","bagimg"]
main_item="paperimg"
selected_item=[]
level=1

def draw():
    screen.fill("orange")
    screen.blit("newbg",(0,0))

def setup():
    
    selected_item.append(main_item)
    for i in range (level):
        random_item=random.choice(ITEMS)
        selected_item.append(random_item)

pgzrun.go()