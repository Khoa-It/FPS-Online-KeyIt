from ursina import *
class OtherBullet:
    def __init__(self, pos, direction):
        self.pos = pos
        self.bullet = Entity(model='sphere', scale = 10, color = color.black, position = self.pos)
        self.direction = direction
        self.alive = True
        self.start_time = time.time()
    def update(self):
        if not self.alive:
            return
        self.bullet.position += self.direction * 50
        if time.time() - self.start_time >= 5:
            self.destroy()
    
    def destroy(self):
        destroy(self.bullet)
        self.alive = False
        
        
        