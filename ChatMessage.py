from ursina import *

from CustomLib import moveObject


class ChatMessage:
    inputText = None
    messages = []
    y_mess = 0.2
    username = ''
    prevLenMessages = 0
    def __init__(self,username='player'):
        # self.inputText = InputField(scale=(1.24, 0.08, 1),position=(0, -0.43, 0),character_limit=60)
        self.inputText = InputField(scale=(1.24, 0.08, 1),position=(0, -1, 0),character_limit=20)
        self.username = username
        self.textPanel = Entity(model='quad', parent= camera.ui, color = color.rgba(0,0,0,60))
        self.textPanel.position = Vec3(-0.69, -0.04, 0)
        self.textPanel.scale = Vec3(0.460001, 0.53, 1)
        

           
    def addNewMessage(self, contentMessage, usermes):
        mesItem = Text(parent = camera.ui,position=(-0.869999, self.y_mess, 0))
        mesItem.text = f'<blue>{usermes}: <white>{contentMessage}'
        self.messages.append(mesItem)
        self.y_mess-=.04
        self.y_mess = round(self.y_mess,2)
        # print(self.y_mess)
        self.inputText.text = ''
      
    def handleEvent(self, key):
        if key == Keys.enter:
            self.addNewMessage()
            
    def scrollcustom(self):
        if len(self.messages) > 10 and len(self.messages) != self.prevLenMessages:
            self.messages[-11].y = 1
            for message in self.messages:
                message.y +=.04
            self.y_mess = -.2
            self.prevLenMessages = len(self.messages)
            
    # def update(self):
    #     moveObject(self.textPanel)
            
            
            