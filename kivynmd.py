from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivy.uix.button import Button
from kivy.core.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

KV = '''


<CommonComponentLabel>
    name: 'menu'
    id: menu
    name: "menu"
    halign: "center"
    md_bg_color: "grey"


<GameComponentLabel>
    name: 'jeu'
    id: jeu
    screen_name: 'jeux'
    opacity: 0
    halign: "center"
    md_bg_color: "grey"    



<MobileView>
    name: 'jeu_screen'
    CommonComponentLabel:
    #     text: "Mobile"
    # MDLabel:
    #     text: "Texte sur mobile ?"
        # size_hint: None, None
        # pos_hint: {'center_x': 0.5,'center_y': 0.5}
    Image:
        id: mon_image
        source: "logo.png"
        size_hint: .5, .5
        # size: (300, 300)
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


    MDFlatButton:
        id: quitter_button
        text: "Quitter"
        size_hint: None, None
        pos_hint: {'center_x': 0.5,'center_y': 0.1}
        size_hint: .5, .1
        md_bg_color: "orange"
        on_press: app.stop()

    GameComponentLabel:
        name: 'game'
        MDLabel:
            text: "EZ"

    
   


<TabletView>
    CommonComponentLabel:
        text: "Table"
    

<DestopView>
    CommonComponentLabel:
        text: "Desktop"
    
ResponsiveView:
'''




class CommonComponentLabel(MDLabel):
    pass

class GameComponentLabel(MDLabel):
    pass



class MobileView(MDScreen):
    pass

class TabletView(MDScreen):
    pass

class DestopView(MDScreen):
    pass



class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DestopView()
        self.jeu_screen = MobileView(name='jeu_screen')
    def cacher_image(self, **kw):
        if self.mobile_view.ids.mon_image.opacity == 1:
            self.mobile_view.ids.mon_image.opacity = 0
        elif self.mobile_view.ids.mon_image.opacity == 0:
            self.mobile_view.ids.mon_image.opacity = 1

    # def jouer_jeu(self, **kw):
    #     self.mobile_view.ids.mon_image.opacity = 0
    #     self.mobile_view.ids.mon_button.opacity = 0
    #     self.mobile_view.ids.mon_button.disabled = True
    #     self.mobile_view.ids.GameComponentLabel.ids.jeu.opacity = 1


    def jouer_jeu(self, **kw):
        self.manager.current = self.jeu_screen.name
        # try:
        #     self.mobile_view.ids.mon_image.opacity = 0
        #     self.mobile_view.ids.mon_button.opacity = 0
        #     self.mobile_view.ids.mon_button.disabled = True
        #     self.mobile_view.ids.settings_button.opacity = 0
        #     self.mobile_view.ids.settings_button.disabled = True
        #     self.mobile_view.ids.quitter_button.opacity = 0
        #     self.mobile_view.ids.quitter_button.disabled = True
        #     self.mobile_view.ids.GameComponentLabel.ids.jeu.opacity = 1
        # except AttributeError as e:
        #     print(f"Erreur d'attribut : {e}")


sm = ScreenManager()
sm.add_widget(MobileView(name='menu'))
sm.add_widget(MobileView(name='jeu_screen'))
class MyApp(MDApp):
    def build(self):
        screen= Builder.load_string(KV)
        return screen


if __name__=="__main__":
    MyApp().run()