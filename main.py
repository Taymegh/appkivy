from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.config import Config

Config.set('graphics','resizable','0');
Config.set('graphics','width','412');
Config.set('graphics','height','712');

class main(Screen):
    pass

class Z1(Screen):
    pass

class Z2(Screen):
    pass

class Z3(Screen):
    pass

class Pagefinale(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

file = Builder.load_file("kyvi.kv");

class MyQuizzApp(App):
    def build(self):
        return file

MyQuizzApp().run()
