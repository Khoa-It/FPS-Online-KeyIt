from direct.actor.Actor import Actor
from ursina import *
app = Ursina()
Entity(model='asset/blenderobj/step/cube.obj')
Entity(model=f'asset/blenderobj/step/plane.obj')
for i in range(9):
    Entity(model=f'asset/blenderobj/step/plane{i}.obj')

EditorCamera()
        
app.run()