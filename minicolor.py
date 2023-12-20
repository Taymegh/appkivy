from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder

Builder.load_string('''
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: app.red_color           
        Label:
            text: "Menu"
''')

class MenuScreen(Screen):
    pass

class MiniColor(App):
    red_color = [1, 0, 0, 1]
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        return sm

if __name__ == "__main__":
    MiniColor().run()
