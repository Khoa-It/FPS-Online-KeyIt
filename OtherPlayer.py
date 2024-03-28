from ursina import *
from Character import Character
class OtherPlayer:
    def __init__(self, position):
        self.position = position
        self.character = Character(position)
        
        