import pyglet 
from pyglet.gl import *


window  = pyglet.window.Window()
window.config.alpha_size=8

pao_baixo = pyglet.resource.image('imgs/pao_baixo.png')
alface = pyglet.resource.image("imgs/alface.png")
tomate = pyglet.resource.image("imgs/tomates.png")
hamburguer = pyglet.resource.image("imgs/hamburguer.png")
queijo = pyglet.resource.image("imgs/queijo.png")
cebola = pyglet.resource.image("imgs/cebola.png")
pao_cima = pyglet.resource.image("imgs/pao_cima.png")

ypos = 200

def update_frames(dt):
    global ypos
    if ypos>80:
        ypos = ypos-30*dt

@window.event
def on_draw():
    window.clear()
    ypos = globals().get("ypos")
    glEnable(GL_BLEND)

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    pao_baixo.blit(20,0)

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    alface.blit(0,30)

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    tomate.blit(20,40)

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    hamburguer.blit(20,50)

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    queijo.blit(10,60)

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    cebola.blit(30,70)

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    pao_cima.blit(20,ypos)

pyglet.clock.schedule_interval(update_frames,1/10.0)
pyglet.app.run()