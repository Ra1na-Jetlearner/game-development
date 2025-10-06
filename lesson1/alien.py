import pgzrun
import random

message=" "

WIDTH=850
HEIGHT=550

ali=Actor("alien2")
ali.pos = (random.randint(0,750), random.randint(0,450))

def draw():
    screen.fill(color=(139,51,106))
    ali.draw()
    screen.draw.text(message, color="pink", center=(50,67))

def on_mouse_down(pos):

    global message
    if ali.collidepoint(pos):
        ali.pos=random.randint(0,800),(random.randint(0,500))
        message=("GOOD SHOT BIA")
    else:
        message=("U missed u skibid toilet ohio rizzler ballarina capponchina tung tung saher cocroidile boi")
        



pgzrun.go()