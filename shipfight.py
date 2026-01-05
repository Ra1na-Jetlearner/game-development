import pgzrun
import random

HEIGHT=600
WIDTH=1000 

ship=Actor("starship")

ship.pos=(WIDTH//2,HEIGHT-100)

speed=10

bullets=[] 
enemies=[]
enemies.append(Actor("bug"))
enemies[-1].x=random.randint(50,WIDTH-50)
enemies[-1].y=-100

score=0

#function will update the score
def scoredisplay():
    screen.draw.text(str(score),(600,300),color="white")

def draw():
    screen.clear()
    screen.fill("Purple")
    ship.draw()
    for i in bullets:
        i.draw()
    for r in enemies:
        r.draw()
    scoredisplay()

def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y-50

def update():
    global score
    if keyboard.left:
        ship.x-=speed
        if ship.x<=0:
            ship.x=0
    if keyboard.right:
        ship.x+=speed
        if ship.x>=WIDTH:
            ship.x=WIDTH
    for i in bullets:
        if i.y<=0:
            bullets.remove(i)
        else:
            i.y-=10
    for r in enemies:
        r.y+=5
        if r.y>=HEIGHT:
          r.y=-100
          r.x=random.randint(50,WIDTH-50)
        for i in bullets:
            if r.colliderect(i):
                score+=1
                bullets.remove(i)
                enemies.remove(r)
                enemies.append(Actor("bug"))
                enemies[-1].x=random.randint(50,WIDTH-50)
                enemies[-1].y=-100
    pass



pgzrun.go()