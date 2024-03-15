from random import random, randint

import ursina
from ursina import Entity, camera

from ursina.prefabs.first_person_controller import FirstPersonController

# gun_model_path = 'asset/static/gun/Mark23.fbx'
# gun_texture_path = 'asset/static/gun/Mark23_D.png'
# glove_texture_path = 'asset/static/gun/Glove_D.png'
# arm_texture_path = 'asset/static/gun/Hand_D.png'
class Player(FirstPersonController):
    def __init__(self, position: ursina.Vec3):
        super().__init__(
            position=position,
            model="cube",
            jump_height=20.5,
            jump_duration=0.05,
            gravity=10,
            origin_y=-2,
            collider="box",
            speed=100
        )
        # self.arm = ursina.Entity(
        #     parent=camera,
        #     model='asset/static/char/arms1.fbx',  # Thay 'your_arm_model.fbx' bằng model của cánh tay
        #     position=(0, -22, 3),  # Điều chỉnh vị trí của cánh tay để nó trông như là player đang cầm súng
        #     rotation=(0, 0, 0), # Điều chỉnh góc quay của cánh tay để nó trông như là player đang cầm súng
        #     scale=0.9,
        #     texture='asset/static/char/arm1Color.png'  # Thay 'your_arm_texture.png' bằng texture của cánh tay
        # )
        self.cursor.color = ursina.color.rgb(255, 0, 0, 122)

        self.ak47 = ursina.Entity(parent=camera,
                           model='asset/static/gun/G32SMGModel.fbx',
                           texture='asset/static/gun/gun_blue_violet_texture.png',
                           scale=.18,
                           position=(1, -6, 0),
                           damage=randint(70, 100),
                           visible=False)
        self.pistol = ursina.Entity(parent=camera,
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

        self.healthbar_pos = ursina.Vec2(0, 0.45)
        self.healthbar_size = ursina.Vec2(0.8, 0.04)
        self.healthbar_bg = ursina.Entity(
            parent=ursina.camera.ui,
            model="quad",
            color=ursina.color.rgb(255, 0, 0),
            position=self.healthbar_pos,
            scale=self.healthbar_size
        )
        self.healthbar = ursina.Entity(
            parent=ursina.camera.ui,
            model="quad",
            color=ursina.color.rgb(0, 255, 0),
            position=self.healthbar_pos,
            scale=self.healthbar_size
        )

        self.health = 100
        self.death_message_shown = False

    def switch_weapon(self):
        for i,v in enumerate(self.gun):
            if i == self.curr_weapon:
                v.visible = True
            else:
                v.visible = False
    def input(self, key):
        try:
            weapon_index = int(key) - 1
            if 0 <= weapon_index < len(self.gun):
                self.curr_weapon = weapon_index
                self.switch_weapon()
        except ValueError:
            pass
        if key == '1':
            self.curr_weapon = self.gun.index(self.ak47)
            self.switch_weapon()
        if key == '2':
            self.curr_weapon = self.gun.index(self.pistol)
            self.switch_weapon()
        if key == 'space':
            self.jump()
        # if key == 'left mouse down':
        #     self.shoot()
        # if key == 'r':
        #     self.reload()


    def death(self):
            self.death_message_shown = True

            ursina.destroy(self.gun)
            self.rotation = 0
            self.camera_pivot.world_rotation_x = -45
            self.world_position = ursina.Vec3(0, 7, -35)
            self.cursor.color = ursina.color.rgb(0, 0, 0, a=0)

            ursina.Text(
                text="You are dead!",
                origin=ursina.Vec2(0, 0),
                scale=3
            )

    def update(self):
            self.healthbar.scale_x = self.health / 100 * self.healthbar_size.x

            if self.health <= 0:
                if not self.death_message_shown:
                    self.death()
            else:
                super().update()

