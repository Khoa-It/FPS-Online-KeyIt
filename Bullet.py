from ursina import *



class Bullet(Entity):
    def __init__(self, position, direction, listObjectIgnore:list, listCallback:list):
        super().__init__(
            model='sphere',
            texture='white_cube',
            color=color.black,
            scale=10,
            position=position,
            collider = 'sphere'
        )
        self.time_start = time.time()
        self.alive = True
        self.listCallback = listCallback
        self.listObjectIgnore = listObjectIgnore
        self.direction = direction
        self.trail = Entity(parent=self, model='sphere', color=color.red, scale=0.3)  # Thêm một trail
        self.gun_sound = Audio('asset/static/sound_effect/shotgun-firing-4-6746.mp3', loop=False, autoplay=False)

    def update(self):
        if time.time() - self.time_start >= 5:
            self.alive = False
        self.move_bullet()
    def move_bullet(self):
        if not self.alive:
            self.deleteBullet()
            return
        if self.y_getter() > 2000 or self.z_getter() > 2000 or self.x_getter() > 2000:
            self.deleteBullet()
            return
        self.position += self.direction  * 50
        self.rotation_y += 5  
        self.animate_trail()  
        hitinfo = self.intersects(ignore=self.listObjectIgnore)
        if hitinfo.hit and not isinstance(hitinfo.entity, self.listCallback[0]()):
            print("-----------------bullet.py notification---------------------------------")
            print('ban trung vat the', hitinfo.entity.__class__)
            print('vi tri vat the bi ban trung', hitinfo.entity.position)
            print("-----------------bullet.py---------------------------------")
            self.deleteBullet()
            
    def animate_trail(self):
        self.trail.position = self.position  
        self.trail.scale_y *= 0.9  

    def shoot(self):
        self.gun_sound.play()
        self.move_bullet()

    def deleteBullet(self):
        self.trail.enable = False
        destroy(self.trail)
        destroy(self)
