import requests
from kivy.lang.builder import Builder
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ObjectProperty

from kivy.lang import Builder


class Login(MDScreen):
    # variable pour permettre a etre lu sur le button password
    text = StringProperty()
    hint_text = StringProperty()
    # text_input_email et text_input_password permet juste de relié nos textInput dans le fichier KV 
    # que nous avons donné un id email et psw
    text_input_email = ObjectProperty(None)
    text_input_password = ObjectProperty(None)
    # les variables email et password permet just de stocker les valeurs de text_input_email et text_input_password
    email = StringProperty('')
    password = StringProperty('')
    
    def __init__(self, **kw):
        Builder.load_file('libs/uix/kv/login.kv')
        super().__init__(**kw)
        
    def sign_in(self):
        #email = self.ids.email.text
        #password = self.ids.psw.text
        
        self.email = self.text_input_email.text
        self.password = self.text_input_password.text
        # ici on recuper les donnéés du login Django rest_framework
        post = requests.post('http://127.0.0.1:8000/auth/login/',json={'email': self.email,'password': self.password})
        print("voir ",post)
        
        # cette condition permet de verifier si la valeur renvoyer dans la viable post de request egal == 200 
        # sinon 401 c'est une erreur 
        if post:
            toast(f"{self.email} Sucessful Login!")
            self.manager.transition.direction = "left" 
            self.manager.current = "home"
            self.ids.email.text = ""
            self.ids.psw.text = ""
        else:
            toast(f"Error Login check your {self.email} and password {self.password}!")
