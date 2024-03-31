from typing import Any
from ursina import *
class Userform:
    def __init__(self, callback):
        self.callback = callback
        self.wp = WindowPanel(
            title='Enter username',
            content=(
                Text('Name:'),
                InputField(),
                Button(text='Submit', color=color.azure),
                ),
            popup=True
            )
        self.wp.y = self.wp.panel.scale_y / 2 * self.wp.scale_y
        print('content',self.wp.content[2])
        # center the window panel
        self.wp.content[2].on_click = Func(lambda: self.setter_usname(self.wp.content[1].text))
    def setter_usname(self, name):
        self.wp.enabled = False
        self.callback[0](name)