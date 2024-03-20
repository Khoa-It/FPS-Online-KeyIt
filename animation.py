from direct.actor.Actor import Actor
from ursina import *


def my_actor(myactor,myentity,name='stand'):
    myactor = Actor(f'asset/animation/cutegirl/{name}.gltf')
    myactor.reparent_to(myentity)
    myactor.loop(name)
    entity.scale =.02

app = Ursina()


my_entity = Entity()
actor = Actor()
my_actor(actor,entity)
entity.scale = .02
EditorCamera()




def input(key):
    global actor,my_entity
    if key == 'w':
        actor.cleanup()
        my_actor(actor,my_entity,'running')
    if key == 'space':
        actor.cleanup()
        my_actor(actor,my_entity)




app.run()