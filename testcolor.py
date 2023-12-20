from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass

class ManagerScreen(ScreenManager):
    pass





class colorApp(App):
    def build(self):
        kv= Builder.load_file("testcolor.kv")
        return kv
    


if __name__ == '__main__':
    colorApp().run()