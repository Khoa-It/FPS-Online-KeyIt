from ursina import *
from Character import Character
from CustomHearbar import CustomHealthBar
class OtherPlayer:
    def __init__(self, position):
        self.position = position
        self.id = 1
        self.character = Character(position)
        self.character.stand_entity.visible = True
        self.healthbar = CustomHealthBar(3,(0,1,0))
    def logout(self):
        self.character.log_out()
        