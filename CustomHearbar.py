from ursina import *
from ursina.prefabs.health_bar import HealthBar


class CustomHealthBar(HealthBar):
    def __init__(self, mode, position):
        self.mode = mode
        super().__init__()
        if self.mode == 1:
            self.parent = camera.ui
            self.bar_color = color.blue
            self.value = 50
            self.text_entity.enable
            self.scale= (1.5, .05,0)
            self.position =  Vec3(-0.750326, 0.48, 0)
        if self.mode == 3:
            self.bar_color = color.pink
            self.value = 50
            self.text_entity.enable
            self.position = position
        
    def input(self,key):
        if key == '+' or key == '+ hold':
            self.value += 10
        if key == '-' or key == '- hold':
            self.value -= 10
            print('ow')
        if held_keys[ 'w']:
            self.y+= .01
        if held_keys['s']:
            self.y-= .01
        if held_keys[ 'a']:
            self.x-= .01
        if held_keys[ 'd']:
            self.x+= .01
        if key =='space':
            print('pos:',self.position)
        
    

        
