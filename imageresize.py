from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.uix.button import MDFlatButton
from kivy.uix.image import Image


class PundizzApp(App):
    def build(self):
        layout= BoxLayout(orientation= 'vertical')
        monImage= Image(
            source= 'logo.png',
            size_hint= (None, .5),
            pos_hint= {'center_x': 0.5,'center_y': 0.5}
            )
        monImage.height = 250
        monImage.width = 300
        layout.add_widget(monImage)
        return layout
    
if __name__ == "__main__":
    PundizzApp().run()