from turtle import position
from ursina import *

from helpers.CustomLib import moveObject
class BulletManage :
    def __init__(self) -> None:
        self.num = 5
        self.showBullet = Text(
            str(self.num), 
            parent = camera.ui, 
            position = Vec3(0.8,0.25,0),
            scale = Vec3(2, 2.1, 0.01)
            )        
        self.circle = Entity(
            model = Circle(40, mode='line', thickness= 5), 
            color = color.rgb(219, 3, 252), 
            parent = camera.ui, 
            position = Vec3(0.814, 0.223, 0),
            scale = .15
        )
    
    def setnumOfBullet(self, value):
        self.num = value
        self.showBullet.text = str(value)
    def update(self):
        moveObject(self.circle)
        
        