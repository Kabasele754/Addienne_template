######## main.py ###########

from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineListItem
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import ThreeLineAvatarListItem


import webbrowser
import requests


class ListItemWithIcon(ThreeLineAvatarListItem):
    source =StringProperty('string')



class ContentNavigationDrawer(BoxLayout):
    pass

class HomeScreen(Screen):
    pass

class DetailScreen(Screen):
    pass

class AboutScreen(Screen):
    pass


class MainWidget(BoxLayout):
    pass



class Mainapp(MDApp):
        def build(self):
            return MainWidget()


        def on_start(self):
            home_list = self.root.ids.home_list
            response = requests.get('https://newsapi.org/v2/top-headlines?country=br&category=business&apiKey=YOURAPIKEY')
            jasonresponse = response.json()
            #array
            articles = jasonresponse['articles']

            for article in articles:
                title = article['title']
                publishedAt = article['publishedAt']
                news_source = article['source']['name']
                publishedAtnews_source = publishedAt + ' - ' + news_source
                urlToImage = article['urlToImage']
                url = article['url']
                
                item = ListItemWithIcon(text=title,secondary_text=url,
                                                                tertiary_text=publishedAtnews_source,
                                                                source='image.png')
                home_list.add_widget(item)


Mainapp().run()