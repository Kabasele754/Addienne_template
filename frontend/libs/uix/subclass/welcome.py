from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Welcome(MDScreen):
    def __init__(self, **kw):
        Builder.load_file('libs/uix/kv/welcome.kv')
        super().__init__(**kw)