from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from data.Map import Map
from helpers.CustomLib import moveObject

app = Ursina()
map = Map()
EditorCamera()
alert = Text(
    text='Victory', 
    style = 'bold', 
    parent = camera.ui,
    position = Vec3(0,0,0),
    scale = 5,
    color = color.rgb(231, 245, 32),
    )

def update():
    global alert
    moveObject(alert)
app.run()