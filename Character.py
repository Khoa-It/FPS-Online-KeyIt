from ursina import *
from direct.actor.Actor import Actor
class Character:
    def __init__(self, myPosition):
        self.stand_entity = Entity()
        self.stand_actor = Actor(f'asset/animation/cutegirl/stand.gltf')
        self.stand_actor.reparent_to(self.stand_entity)
        self.stand_actor.loop('stand')
        self.stand_entity.scale = .7
        self.stand_entity.position = myPosition
        self.stand_entity.rotation_y  = 180
        self.stand_entity.collider = 'box'
        self.stand_entity.visible = False
        
        self.running_entity = Entity()
        self.running_entity.position = myPosition
        self.running_actor = Actor(f'asset/animation/cutegirl/running.gltf')
        self.running_actor.reparent_to(self.running_entity)
        self.running_actor.loop('running')
        self.running_entity.scale =.7
        self.running_entity.rotation_y = 180
        self.running_entity.visible = False
        self.running_entity.collider = 'box'