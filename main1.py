from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel

KV = '''
Screen:
    MDLabel:
        text: 'Hello'
        pos_hint: {'center_x': .5, 'center_y': .5}
        halign: 'center'
        font_style: 'H3'
'''

class LoginApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

LoginApp().run()
