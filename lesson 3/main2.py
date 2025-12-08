import pgzrun
import random

WIDTH=500
HEIGHT=500

idx=1
start=[]
end=[]

satellite = []
for i in range(8):
    s=Actor("satellite")
    s.pos = random.randint(50,450),random.randint(50,450)
    satellite.append(s)
def draw():
    screen.blit("galaxy",(0,0))
    numb=1
    for s in satellite:
        s.draw()
        screen.draw.text(str(numb),color="white",center=(s.x,s.y-20))
        numb+=1

    for i in range(len(start)):
        screen.draw.line(start[i],end[i],color="white")

def on_mouse_down(pos):
    global idx
    global text,click
    if flo.collidepoint(pos):
        click+=1
        text="flower collided"
    if click>=3:
        text="click 3 times"
    if click>=6:
        text="stop it!!!!!!"
    if click>=9:
        text="STOP BOTHERING ME IM JUST A SMALL FLOWER"
    if satellite[idx].collidepoint(pos):
        prev=satellite[idx-1]
        curr=satellite[idx]
        start.append(prev.pos)
        end.append(curr.pos)
        idx+=1

pgzrun.go()