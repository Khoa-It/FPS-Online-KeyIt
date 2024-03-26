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
        self.step = 5
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

    def input(self,key):
        if key == 'w':
            self.creativeCube.z += self.step
        if key == 's':
            self.creativeCube.z -= self.step
        if key == 'a':
            self.creativeCube.x -= self.step
        if key == 'd':
            self.creativeCube.x += self.step
        if key =='space':
            print("cube:","{",f"'x':{self.creativeCube.x}, 'height':20, 'z':{self.creativeCube.z}, 'color':color.green","},")
            print("wall:","{",f"'x':{self.creativeCube.x}, 'height':80, 'width':150, 'z':{self.creativeCube.z}, 'color':color.rgb(128, 49, 4), 'corner':0 ", "},")
            print("tree:", "{",f"'x':{self.creativeCube.x}, 'z':{self.creativeCube.z}", "},")
            print("house:", "{", f"'x':{self.creativeCube.x}, 'z':{self.creativeCube.z}, 'corner':0", "},")
            print("building:",
                  "{",
                  f"'x':{self.creativeCube.x-60}, 'height':80*2, 'width':150*2, 'z':{self.creativeCube.z+200}, 'color':color.rgb(145, 117, 6), 'corner':0 ",
                  "},",
                  "{",
                  f"'x':{self.creativeCube.x+200},'height':80*2, 'width':150*3, 'z':{self.creativeCube.z-60}, 'color':color.rgb(145, 117, 6), 'corner':90 ",
                  "},",
                  "{",
                  f"'x':{self.creativeCube.x}, 'height':80*2, 'width':150*2+100, 'z':{self.creativeCube.z-260}, 'color':color.rgb(145, 117, 6), 'corner':0 ",
                  "},",
                  "{",
                  f"'x':{self.creativeCube.x-200}, 'height':80*2, 'width':150*2, 'z':{self.creativeCube.z+50}, 'color':color.rgb(145, 117, 6), 'corner':90 ",
                  "},",
                  )