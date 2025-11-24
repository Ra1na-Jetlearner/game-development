import pgzrun

WIDTH = 500
HEIGHT = 500

flo=Actor("flower")
flo.pos=(200,300)

text = ""
click=0

def draw():
    screen.fill("purple")
    # screen.blit("nature",(0,0))
    screen.draw.text("Raina", color="pink",center=(250,300))
    flo.draw()
    screen.draw.text(text, color = "orange", center = (100,150))

def on_mouse_down(pos):
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

def update():
    if keyboard.left:
        flo.x-=10
    if keyboard.right:
        flo.x+=10
    if keyboard.up:
        flo.y-=10
    if keyboard.down:
        flo.y+=10

pgzrun.go()