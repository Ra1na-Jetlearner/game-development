import pgzrun
import random

WIDTH=675
HEIGHT=850

score=0

def draw():
    screen.blit("background",(0,0))
    pie.draw()
    pie2.draw()
    
pie = Actor("bee")
pie2 = Actor("flower")
pie2.pos = (random.randint(0,500)),(random.randint(0,500))

def update():
    if keyboard.left:
        pie.x-=5
    elif keyboard.right:
        pie.x+=5
    elif keyboard.up:
        pie.y-=5
    elif keyboard.down:
        pie.y+=5

    if pie.colliderect(pie2): 
        pie2.pos = (random.randint(0,500)),(random.randint(0,500))
        score+=1






pgzrun.go()