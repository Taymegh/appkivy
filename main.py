from kivymd.app import App 
from kivymd.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

from kivy.config import Config
Config.set('graphics', 'Resizeable', '0');
Config.set('graphics', 'width', '412');
Config.set('graphics', 'height', '732');

class HomePage(Screen):
    pass

class Q1(Screen):
    pass

class Q2(Screen):
    pass

class Q3(Screen):
    pass

class Q4(Screen):
    pass

class Q5(Screen):
    pass

class FinalPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

file = Builder.load_file("kivy.kv");

class QuizApp(App):
    def build(self):
        return file
    
QuizApp().run()