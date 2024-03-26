
from direct.actor.Actor import Actor
from ursina import *


def input(key):
    global stand_entity, running_entity
    if held_keys['w']:
        stand_entity.visible = False
        running_entity.visible = True
    if not held_keys['w']:
        stand_entity.visible = True
        running_entity.visible = False

app = Ursina()

stand_entity = Entity()
stand_actor = Actor(f'asset/animation/cutegirl/stand.gltf')
stand_actor.reparent_to(stand_entity)
stand_actor.loop('stand')
stand_entity.scale =.04

running_entity = Entity()
running_actor = Actor(f'asset/animation/cutegirl/running.gltf')
running_actor.reparent_to(running_entity)
running_actor.loop('running')
running_entity.scale =.04
running_entity.visible = False

EditorCamera()
app.run()
