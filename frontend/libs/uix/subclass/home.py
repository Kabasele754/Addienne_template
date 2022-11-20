import requests
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivy.lang import Builder

class Home(MDScreen):
    #text_lo = StringProperty()
    def __init__(self, **kw):
        Builder.load_file('libs/uix/kv/home.kv')
        super().__init__(**kw)
    def logout(self):
        post = requests.post('http://127.0.0.1:8000/auth/logout/',json={'refresh':'string' })
        print(post)
        #toast(f"Sucessful Logout!")
        
        self.manager.transition.direction = "right" 
        self.manager.current = "login"
        toast(f"Sucessful Logout!")
            