from ursina import Entity, color, time, Audio, raycast


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
        self.gun_sound = Audio('asset/static/sound_effect/lasergun.wav', loop=False, autoplay=False)

    def update(self):
        self.move_bullet()

    def move_bullet(self):
        self.position += self.direction * self.speed * time.dt
        self.rotation_y += 5  # Xoay viên đạn khi di chuyển
        self.animate_trail()  # Áp dụng hiệu ứng trail

        # Kiểm tra va chạm với vật thể
        hit_info = raycast(self.position, self.direction, distance=self.speed * time.dt, ignore=[self])
        if hit_info.hit:
            self.position = hit_info.world_point  # Di chuyển viên đạn đến điểm va chạm
            self.speed = 0  # Dừng chuyển động của viên đạn khi va chạm

            # Kiểm tra khoảng cách giữa viên đạn và vật thể
            distance_to_object = (hit_info.world_point - self.position).length()
            if distance_to_object > 1:  # Giả sử khoảng cách lớn hơn 1 đơn vị là "gần"
                self.gun_sound.stop()  # Dừng phát âm thanh súng
            else:
                self.gun_sound.volume = 0.5  # Giảm âm lượng của âm thanh
                # Nếu bạn muốn giảm âm lượng dựa trên khoảng cách cụ thể, bạn có thể điều chỉnh giá trị 0.5 ở đây.

    def animate_trail(self):
        self.trail.position = self.position  # Đặt vị trí của trail bằng vị trí của viên đạn
        self.trail.scale_y *= 0.9  # Giảm kích thước theo trục y để tạo hiệu ứng trail dần dần biến mất

    def shoot(self):
        self.gun_sound.play()
