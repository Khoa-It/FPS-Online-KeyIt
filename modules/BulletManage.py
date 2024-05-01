from turtle import position
from ursina import *

from helpers.CustomLib import moveObject
class BulletManage :
    def __init__(self, max_bullets=5) -> None:
        self.max_bullets = max_bullets
        self.num = max_bullets
        self.showBullet = Text(
            f"{self.num}/{self.max_bullets}",  # Hiển thị số đạn hiện tại và tổng số đạn
            parent=camera.ui,
            position=Vec3(0.8, 0.3, 0),
            scale=Vec3(2, 2.1, 0.01)
        )
        self.bulletIcon = Sprite(
            texture='asset/static/gun/bullets.png',  # Đường dẫn tới tập tin hình ảnh của hình đạn (loại bỏ phần mở rộng file)
            parent=camera.ui,
            position=Vec3(0.77, 0.28, 0),  # Vị trí phía bên trái của số đạn
            scale=Vec3(0.05, 0.05, 0.05)  # Kích thước của biểu tượng hình đạn
        )

    def setnumOfBullet(self, value):
        self.num = value
        self.showBullet.text = f"{self.num}/{self.max_bullets}"

    def setBulletVisibility(self):
        if self.num <= 0:
            self.showBullet.enabled = False
            self.bulletIcon.enabled = False
        else:
            self.showBullet.enabled = True
            self.bulletIcon.enabled = True

    def update(self):
        pass  # Không cần cập nhật gì cho hình đạn nên pass

