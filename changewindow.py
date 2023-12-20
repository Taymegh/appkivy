from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivy.core.window import Window

KV = '''
ScreenManager:
    MenuScreen:
    GameScreen:
    SettingsScreen:

    

<MenuScreen>:
    name: 'menu'
    id: 'menu'
    halign: "center"
    md_bg_color: "grey"
    Image:
        id: mon_image
        source: "logo.png"
        size_hint: .5, .5
        size: (100, 100)
        pos_hint: {'center_x': 0.5,'center_y': 0.7}

    MDFlatButton:
        id: mon_button
        text: "Jouer"
        size_hint: None, None
        pos_hint: {'center_x': 0.5,'center_y': 0.4}
        # font_size: "21sp"
        size_hint: .5, .1
        md_bg_color: "orange"
        # on_press: app.root.jouer_jeu()
        # on_press: app.root.current = 'blank'
        on_press: app.root.current = 'game'

    MDFlatButton:
        text: "Paramètres"
        id: settings_button
        size_hint: None, None
        pos_hint: {'center_x': 0.5,'center_y': 0.25}
        size_hint: .5, .1
        md_bg_color: "orange"
        on_press: app.root.current = 'settings'


    MDFlatButton:
        id: quitter_button
        text: "Quitter"
        size_hint: None, None
        pos_hint: {'center_x': 0.5,'center_y': 0.1}
        size_hint: .5, .1
        md_bg_color: "orange"
        on_press: app.stop()


<GameScreen>:
    md_bg_color: 'grey'
    name: 'game'
    MDLabel:
        text: 'Bienvenue dans le jeu Pundizz!'
        halign: 'center'
    MDFlatButton:
        id: retour
        text: "Retour"
        md_bg_color: "orange"
        on_press: app.root.current = 'menu'

<SettingsScreen>:
    md_bg_color: 'grey'
    name: 'settings'
    MDLabel:
        text: 'Paramètres du jeu'
        halign: 'center'
        pos_hint: {'center_x': 0.5,'center_y': 0.9}
        color: 'white'

    MDFlatButton:
        id: retour
        text: "Retour"
        md_bg_color: "orange"
        on_press: app.root.current = 'menu'   

    MDFlatButton:
        id: noir
        text: "noir"
        md_bg_color: "orange"
        pos_hint: {'center_x': 0.5,'center_y': 0.2}
        on_press: app.karrupu()
        
    
    MDFlatButton:
        id: gris
        text: "base"
        md_bg_color: "orange"
        pos_hint: {'center_x': 0.3,'center_y': 0.2}
        on_press: app.karrupu

'''


#Différents écrans
class MenuScreen(MDScreen):
    pass

class GameScreen(MDScreen):
    pass

class SettingsScreen(MDScreen):
    pass


#Layout responsive
# class MobileView(MDScreen):
#     pass

# class TabletView(MDScreen):
#     pass

# class DestopView(MDScreen):
#     pass



# class ResponsiveView(MDResponsiveLayout, MDScreen):
#     def __init__(self, **kw):
#         super().__init__(**kw)
#         self.mobile_view = MobileView()
#         self.tablet_view = TabletView()
#         self.desktop_view = DestopView()
#         self.jeu_screen = MobileView(name='jeu_screen')
    


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(GameScreen(name='game'))
sm.add_widget(SettingsScreen(name='settings'))

class TestApp(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        return screen

    def karrupu(self):
        print("Bouton appuyé")
        for screen in self.root.screens:
            print(screen.name)
        
if __name__ == "__main__":
    TestApp().run()