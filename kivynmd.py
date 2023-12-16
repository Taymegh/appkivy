from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivy.uix.button import Button
from kivy.core.image import Image

KV = '''
<CommonComponentLabel>
    halign: "center"
    md_bg_color: "grey"

<MobileView>
    CommonComponentLabel:
    #     text: "Mobile"
    # MDLabel:
    #     text: "Texte sur mobile ?"
        # size_hint: None, None
        # pos_hint: {'center_x': 0.5,'center_y': 0.5}
    Image:
        id: mon_image
        source: "image2.jpg"
        size_hint: None, None
        size: (300, 300)
        pos_hint: {'center_x': 0.5,'center_y': 0.7}

    MDFlatButton:
        id: mon_button
        text: "Jouer"
        size_hint: None, None
        pos_hint: {'center_x': 0.5,'center_y': 0.4}
        # font_size: "21sp"
        size_hint: .5, .1
        md_bg_color: "orange"
        on_release: app.root.cacher_image()


<TabletView>
    CommonComponentLabel:
        text: "Table"
    

<DestopView>
    CommonComponentLabel
        text: "Desktop"
    
ResponsiveView:
'''


class CommonComponentLabel(MDLabel):
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
        self.mobile_view= MobileView()
        self.tablet_view= TabletView()
        self.desktop_view= DestopView()
    def cacher_image(self, **kw):
        if self.mobile_view.ids.mon_image.opacity == 1:
            self.mobile_view.ids.mon_image.opacity = 0
        elif self.mobile_view.ids.mon_image.opacity == 0:
            self.mobile_view.ids.mon_image.opacity = 1


        




class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)



if __name__=="__main__":
    MyApp().run()