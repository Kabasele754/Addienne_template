import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivymd.tools.hotreload.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from libs.screens.screens import *

Window.size = (375,625)

class WindowManager(ScreenManager):
    pass

class OfficReportAPP(MDApp):
    
    CLASSES = {
        'Welcome':'libs.uix.subclass.welcome',
        'Home':'libs.uix.subclass.home',
    }
    AUTORELOADER_PATHS = [
        ('.', {'recursive':True})
    ]
    KV_FILES = [
        'libs/uix/kv/welcome.kv',
        'libs/uix/kv/home.kv',
    ]
    def build_app(self):
        self.title = "5BSS"
        self.theme_cls_style = "Light"
        self.theme_primary_palette = "LightGreen"
        self.wm = WindowManager()
        screens = [
            Welcome(name="welcome"),
            Login(name="login"),
            Home(name="home"),
            
        ]
        
        for sceen in screens:
            self.wm.add_widget(sceen)
        return self.wm
    
if __name__ == '__main__':
    LabelBase.register(name="MPoppins", fn_regular="assets/fonts/Poppins-Medium.ttf",
                       )
    LabelBase.register(name="BPoppins", fn_regular="assets/fonts/Poppins-SemiBold.ttf",
                       )
    OfficReportAPP().run()