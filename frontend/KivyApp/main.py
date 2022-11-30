import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.app import MDApp
import requests
from kivy.clock import Clock
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.list import OneLineIconListItem
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen

Window.size = (375,625)



#recycle view for home screen

class BlogList(OneLineIconListItem):
    pass

class BlogListItem(BoxLayout):
    title = StringProperty("Titre")
    image = StringProperty("Image")
    description = StringProperty("Description")


class MyRecycleView(RecycleView):
    text_title = ObjectProperty(None)
    playlist_name = StringProperty("Titre")
    
    def __init__(self, **kwargs):
        super(MyRecycleView, self).__init__(**kwargs)
        
        self.load_data()
        Clock.schedule_interval(self.load_data, 1)

    def load_data(self, *args):
        #card_id = root.ids.card_id
        #store = requests.get('http://127.0.0.1:8000/api').json()
        store = requests.get('http://127.0.0.1:8000/blog').json()

        self.data.list_data = []
        for item in store:
            #self.data.list_data.append({'text': item['name']})
            print(f"http://127.0.0.1:8000/{item['image']}")
            
            if item:
                self.data.list_data.append(
                        {
                            'viewclass':"BlogListItem",
                            'markup': True,
                            'title':f" {item['title']}",
                            'description':item['description'],
                            'image': f"http://127.0.0.1:8000{item['image']}"
                        }
                        )
                print("Good")
                
            else:
                print("Aucune donnee")

        self.data = self.data.list_data
        #self.text_title = self.data
        #self.viewclass= str(self.data)
        #self.playlist_name = 
           
class AddMessage(Widget):
    text_input_email = ObjectProperty(None)
    text_input_password = ObjectProperty(None)
    email = StringProperty('')
    password = StringProperty('')

    def submit_input(self):
        self.email = self.text_input_email.text
        self.password = self.text_input_password.text
        post = requests.post('http://127.0.0.1:8000/auth/login/',json={'email': self.email,'password': self.password})
        print("voir ",post)

        self.input = ''



class HomeScreen(ThemableBehavior, MDScreen):
    pass


class Test(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_file("main.kv")


Test().run()
