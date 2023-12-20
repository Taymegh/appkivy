from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton



class Management(ScreenManager):
    pass



class Menu(Screen):
    pass


class Jeu(Screen):
    pass

class Ecran(Screen):
    pass





class quizzApp(MDApp):
    def build(self):
        file = Builder.load_file('testlawis.kv')
        return file
      
    



if __name__ == '__main__':
    quizzApp().run()