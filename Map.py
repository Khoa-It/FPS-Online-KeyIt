from ursina import *
from CustomLib import *
# create a new class for Map


class Map:
    listWallCube = []

    def __init__(self):
        Entity(model='cube', position=(0,0,0), collider='box', scale=(1000,1,1000), texture='white_cube', color = color.gray)
        self.createBoundary(size=200, height=100)
        createWallCube((0,1,0),random.randint(10,80))
        createWallCube((20, 1, 0),random.randint(10,80))

        createWallCube((0, 1, -20*4), random.randint(10,80))
        createWallCube((20, 1, -20*4), random.randint(10,80))

        createWallCube((0, 1, 20*4), random.randint(10,80))
        createWallCube((20, 1, 20*4), random.randint(10,80))

        createWallCube((0-(20*7), 1, 0), random.randint(10,80))
        createWallCube((20-(20*7), 1, 0), random.randint(10,80))

        createWallCube((0-(20*7), 1, -20 * 4), random.randint(10,80))
        createWallCube((20-(20*7), 1, -20 * 4), random.randint(10,80))

        createWallCube((0-(20*7), 1, 20 * 4), random.randint(10,80))
        createWallCube((20-(20*7), 1, 20 * 4), random.randint(10,80))
        
        createWallCube((0+(20*7), 1, 0), random.randint(10,80))
        createWallCube((20+(20*7), 1, 0), random.randint(10,80))

        createWallCube((0+(20*7), 1, -20 * 4), random.randint(10,80))
        createWallCube((20+(20*7), 1, -20 * 4), random.randint(10,80))

        createWallCube((0+(20*7), 1, 20 * 4), random.randint(10,80))
        createWallCube((20+(20*7), 1, 20 * 4), random.randint(10,80))

    def createBoundary(self,size=200, height=100):
        Entity(model='cube',position=(0,1,-(size-1)), scale=(size*2,height,1), collider='box',texture='brick')
        Entity(model='cube', position=(size-1, 1, 0), scale=(1, height, size*2), collider='box',texture='brick')
        Entity(model='cube', position=(0,1,size-1), scale=(size*2,height, 1), collider='box',texture='brick')
        Entity(model='cube', position=(-(size-1), 1, 0), scale=(1, height,size*2), collider='box',texture='brick')
