from kivymd.app import MDApp
from kivy.lang import Builder







class textApp(MDApp):
    def build(self):
        file = Builder.load_file('singleline.kv')
        return file
    


if __name__ == '__main__':
    textApp().run()