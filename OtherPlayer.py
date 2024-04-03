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
    def getPos(self):
        return self.character.stand_entity.position
    def setPos(self, position):
        self.character.stand_entity.position = position
        self.character.running_entity.position = position
    def setRot(self, rotation):
        self.character.stand_entity.rotation = rotation
        self.character.running_entity.rotation = rotation
    def logout(self):
        self.character.log_out()
        
    def running(self):
        self.character.running_entity.visible = True
        self.character.stand_entity.visible = False
    def stand(self):
        self.character.stand_entity.visible = True
        self.character.running_entity.visible = False