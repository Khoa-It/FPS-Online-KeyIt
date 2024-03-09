from ursina import *
from CustomLib import *
# create a new class for Map


class Map:
    listWallCube = []
    listCubePosition = [
        {'x':0, 'height':20, 'z':105, 'color':color.rgb(115, 89, 18)},
        {'x':120.0, 'height':20, 'z':120.0, 'color':color.rgb(115, 89, 18)},
        {'x':220.0, 'height':20, 'z':220.0, 'color':color.rgb(115, 89, 18)},
        {'x':-140.0, 'height':20, 'z':-140.0, 'color':color.rgb(115, 89, 18)},
        {'x':-100.0, 'height':20, 'z':-100.0, 'color':color.rgb(115, 89, 18)},
        {'x':180.0, 'height':20, 'z':180.0, 'color':color.rgb(115, 89, 18)},
        {'x': -160.0, 'height': 20, 'z': 180.0, 'color': color.rgb(115, 89, 18)},
        {'x': -60.0, 'height': 20, 'z': 400.0, 'color': color.rgb(115, 89, 18)},
        {'x': -380.0, 'height': 20, 'z': 400.0, 'color': color.rgb(115, 89, 18)},
        {'x': -320.0, 'height': 20, 'z': 100.0, 'color': color.rgb(115, 89, 18)},
        {'x': -360.0, 'height': 20, 'z': -40.0, 'color': color.rgb(115, 89, 18)},
        {'x': 100.0, 'height': 20, 'z': -40.0, 'color': color.rgb(115, 89, 18)},
        {'x': 100.0, 'height': 20, 'z': 340.0, 'color': color.rgb(115, 89, 18)},
        {'x': 320.0, 'height': 20, 'z': 440.0, 'color': color.rgb(115, 89, 18)},
        {'x': 400.0, 'height': 20, 'z': 160.0, 'color': color.rgb(115, 89, 18)},
        {'x': 460.0, 'height': 20, 'z': -40.0, 'color': color.rgb(115, 89, 18)},
        {'x': 280.0, 'height': 20, 'z': -140.0, 'color': color.rgb(115, 89, 18)},
        {'x': 380.0, 'height': 20, 'z': -320.0, 'color': color.rgb(115, 89, 18)},
        {'x': 220.0, 'height': 20, 'z': -300.0, 'color': color.rgb(115, 89, 18)},
        {'x': 40.0, 'height': 20, 'z': -400.0, 'color': color.rgb(115, 89, 18)},
        {'x': -120.0, 'height': 20, 'z': -300.0, 'color': color.rgb(115, 89, 18)},
        {'x': -280.0, 'height': 20, 'z': -300.0, 'color': color.rgb(115, 89, 18)},
        {'x': -440.0, 'height': 20, 'z': -380.0, 'color': color.rgb(115, 89, 18)},
    ]
    listWallPosition = [
        {'x': -240.0, 'height': 80, 'width': 150, 'z': -100.0, 'color': color.rgb(128, 49, 4), 'corner': 90},
        {'x': 40.0, 'height': 80, 'width': 150, 'z': 140.0, 'color': color.rgb(128, 49, 4), 'corner': 90},
        {'x': 180.0, 'height': 80, 'width': 150, 'z': -80.0, 'color': color.rgb(128, 49, 4), 'corner': 0},
        {'x': 0.0, 'height': 80, 'width': 150, 'z': -240.0, 'color': color.rgb(128, 49, 4), 'corner': 90},
        {'x': 160.0, 'height': 80, 'width': 150, 'z': 440.0, 'color': color.rgb(128, 49, 4), 'corner': 0},
        {'x': -240.0, 'height': 80, 'width': 150, 'z': 240.0, 'color': color.rgb(128, 49, 4), 'corner': 0},
        {'x': 320.0, 'height': 80, 'width': 150, 'z': -220.0, 'color': color.rgb(128, 49, 4), 'corner': 0},
    ]

    def __init__(self):
        Entity(model='cube', position=(0,0,0), collider='box', scale=(1500,1,1500), texture='brick', color = color.gray)
        self.listWallCube.append(createMyCube(0,0,20,color.red))
        for pos in self.listCubePosition:
            cube = createMyCube(pos['x'], pos['z'], pos['height'], pos['color'])
            self.listWallCube.append(cube)
        for pos in self.listWallPosition:
            wall = createWall(pos['x'], pos['z'], pos['width'], pos['height'], pos['color'], pos['corner'])
            self.listWallCube.append(wall)