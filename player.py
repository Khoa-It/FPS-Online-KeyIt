from random import random, randint
from direct.actor.Actor import Actor
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from Bullet import Bullet
from Character import Character
from SharePostition import modePosition



# gun_model_path = 'asset/static/gun/Mark23.fbx'
# gun_texture_path = 'asset/static/gun/Mark23_D.png'
# glove_texture_path = 'asset/static/gun/Glove_D.png'
# arm_texture_path = 'asset/static/gun/Hand_D.png'
class Player(FirstPersonController):
    def __init__(self, position):
        self.character = Character(position)
        self.modController = 1
        super().__init__(
            position=position,
            model=self.character.stand_entity,
            jump_height=20.5,
            jump_duration=0.05,
            gravity=10,
            origin_y=2,
            collider="box",
            speed=100
        )
        self.walksound = Audio('asset/static/sound_effect/running-sounds.mp3', loop = True)
        self.walksound.volume = 0
        self.walksound.autoplay = True
        self.bullet = None
        self.cursor.color = color.rgb(255, 0, 0, 122)
        self.ak47 = Entity(parent=camera,
                           model='asset/static/gun/G32SMGModel.fbx',
                           texture='asset/static/gun/gun_blue_violet_texture.png',
                           scale=.18,
                           position=(1, -6, 0),
                           damage=randint(70, 100),
                           collider = 'box',
                           visible=False)
        self.pistol = Entity(parent=camera,
                                    model='asset/static/gun/Beretta Pistol.fbx',
                                    texture='asset/static/gun/RenderResult.png',
                                    scale=0.03,  # Chỉnh sửa kích thước
                                    position=(8, -10, 24),
                                    damage=randint(40, 90),
                                    visible=False
                                    )

        self.gun = [self.ak47, self.pistol]
        self.curr_weapon = 0
        self.switch_weapon()
        self.healthbar_pos = Vec2(0, 0.45)
        self.healthbar_size = Vec2(0.8, 0.04)
        self.healthbar_bg = Entity(
            parent=camera.ui,
            model="quad",
            color=color.rgb(255, 0, 0),
            position=self.healthbar_pos,
            scale=self.healthbar_size
        )
        self.healthbar = Entity(
            parent=camera.ui,
            model="quad",
            color=color.rgb(0, 255, 0),
            position=self.healthbar_pos,
            scale=self.healthbar_size
        )
        self.health = 100
        self.death_message_shown = False
        # difine for camera position
        camera.y = 50
        camera.z = -60
        # switch to third controller
        self.ndk_switch_mode(1)

    def switch_weapon(self):
        for i,v in enumerate(self.gun):
            if i == self.curr_weapon:
                v.visible = True
            else:
                v.visible = False
    def input(self, key):
        # first controller
        try:
            weapon_index = int(key) - 1
            if 0 <= weapon_index < len(self.gun):
                self.curr_weapon = weapon_index
                self.switch_weapon()
        except ValueError:
            pass
        if key == '1' and self.modController == 1:
            self.curr_weapon = self.gun.index(self.ak47)
            self.switch_weapon()
        if key == '2' and self.modController == 1:
            self.curr_weapon = self.gun.index(self.pistol)
            self.switch_weapon()
        if key == 'left mouse down' and self.modController == 1:
            self.shootBullet()
        if key == 'space':
            self.jump()
        if key == 'r':
            self.modController = 1
            self.ndk_switch_mode(self.modController)
        if key == 't':
            self.modController = 3
            self.ndk_switch_mode(self.modController)
        # third controller 
        if held_keys['w'] and self.modController == 3:
            self.character.running_entity.visible = True
            self.model = self.character.running_entity
        if not held_keys['w'] and not held_keys['s'] and not held_keys['a'] and not held_keys['d'] and self.modController == 3:
            self.character.running_entity.visible = False
            self.model = self.character.stand_entity
            self.character.running_entity.rotation_y = 180
        if held_keys['s'] and self.modController == 3:
            self.character.running_entity.visible = True
            self.model = self.character.running_entity
            self.character.running_entity.rotation_y = 0
        if held_keys['a'] and self.modController == 3:
            self.character.running_entity.visible = True
            self.model = self.character.running_entity
            self.character.running_entity.rotation_y = 90
        if held_keys['d'] and self.modController == 3:
            self.character.running_entity.visible = True
            self.model = self.character.running_entity
            self.character.running_entity.rotation_y = 270
        if key == Keys.enter:
            print('vi tri nguoi choi:', self.world_position)


    def ndk_death(self):
        self.death_message_shown = True
        self.cursor.color = color.rgb(0, 0, 0, a=0)  # Ẩn con trỏ
        for gun in self.gun:
            gun.disable()  # Ẩn súng
        self.healthbar.enabled = False  # Ẩn thanh máu
        self.healthbar_bg.enabled = False  # Ẩn nền thanh máu
        self.disable()  # Tắt bộ điều khiển
        Text(text="You are dead!", origin=Vec2(0, 0), scale=3)  # Hiển thị thông báo
    
    def ndk_switch_mode(self, controllerMode):
        if controllerMode == 3:
            for gun in self.gun:
                gun.disable()  # Ẩn súng
            self.healthbar.enabled = False  # Ẩn thanh máu
            self.healthbar_bg.enabled = False  # Ẩn nền thanh máu
            self.character.stand_entity.visible = True
            self.character.running_entity.visible = False
        else:
            self.character.stand_entity.visible = False
            self.character.running_entity.visible = False
            for gun in self.gun:
                gun.enable()  # Bật súng
            self.curr_weapon = 0
            self.gun[self.curr_weapon].visible = True
            self.healthbar.enabled = True  # Bật thanh máu
            # self.healthbar_bg.enabled = True  # Bật nền thanh máu
            

    def death(self):
            self.death_message_shown = True
            destroy(self.gun)
            self.rotation = 0
            self.camera_pivot.world_rotation_x = -45
            self.world_position = Vec3(0, 7, -35)
            self.cursor.color = color.rgb(0, 0, 0, a=0)

            Text(
                text="You are dead!",
                origin=Vec2(0, 0),
                scale=3
            )

    def update(self):
        if self.bullet:
            self.bullet.update()  # Cập nhật vị trí của viên đạn
        self.healthbar.scale_x = self.health / 100 * self.healthbar_size.x
        if self.health <= 0:
            if not self.death_message_shown:
                self.death()
        else:
            super().update()
        if held_keys['w'] or held_keys['a'] or held_keys['d'] or held_keys['s']:
            if self.walksound.volume != 1:
                self.walksound.volume += .1
            
        if not held_keys['w'] and not held_keys['a'] and not held_keys['d'] and not held_keys['s']:
            self.walksound.volume = 0

    def shootBullet(self):
        self.bullet = Bullet(Vec3(self.world_position.x, 50,self.world_position.z), direction=self.gun[self.curr_weapon].forward)
        self.bullet.shoot()