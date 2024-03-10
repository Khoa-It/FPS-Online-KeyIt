from ursina import *
from CustomLib import *
from CubePositionData import listCubePosition
from WallPositionData import listWallPosition
from TreePositionData import listTreePosition
from HousePositionData import listHousePosition
# create a new class for Map


class Map:
    creativeCube = 5

    def __init__(self):
        Entity(model='cube', position=(0,0,0), collider='box', scale=(3500,1,3500), texture='brick', color = color.gray)
        self.creativeCube = createMyCube(-800,0,20,color.red)
        for pos in listCubePosition:
            createMyCube(pos['x'], pos['z'], pos['height'], pos['color'])
        for pos in listWallPosition:
            createWall(pos['x'], pos['z'], pos['width'], pos['height'], pos['color'], pos['corner'])
        for tree in listTreePosition:
            createTree(tree['x'], tree['z'])
        for house in listHousePosition:
            createHouse(house['x'], house['z'], house['corner'])

