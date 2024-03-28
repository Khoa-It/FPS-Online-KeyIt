from email.mime import audio
from ursina import *
from ursina.prefabs.health_bar import HealthBar

from CustomHearbar import CustomHealthBar

app = Ursina()
audio=Audio('asset/static/sound_effect/running-sounds.mp3', loop = True)
audio.autoplay = True
app.run()