from ursina import *


class Bullet(Entity):
    def __init__(self, position, direction):
        super().__init__(
            model='sphere',
            texture='white_cube',
            color=color.black,
            scale=3,
            position=position
        )
        self.direction = direction
        self.speed = 5000
        self.trail = Entity(parent=self, model='sphere', color=color.red, scale=0.3)  # Thêm một trail
        self.gun_sound = Audio('asset/static/sound_effect/shotgun-firing-4-6746.mp3', loop=False, autoplay=False)

    def update(self):
        self.move_bullet()
    def move_bullet(self):
        if self.y_getter() > 2000 or self.z_getter() > 2000 or self.x_getter() > 2000:
            self.disable()
        self.position += self.direction * self.speed * time.dt
        self.rotation_y += 5  
        self.animate_trail()  
        hit_info = raycast(self.position, self.direction, distance=self.speed * time.dt, ignore=[self])
        if hit_info.hit:
            self.position = hit_info.world_point  
            self.speed = 0 
            self.disable()
            
    def animate_trail(self):
        self.trail.position = self.position  
        self.trail.scale_y *= 0.9  

    def shoot(self):
        self.gun_sound.play()
        self.move_bullet()

