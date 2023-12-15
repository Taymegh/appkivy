from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image


from kivy.core.text import LabelBase

class PundizzApp(App):
    def build(self):

        LabelBase.register(name="Superfont", fn_regular='superfont.ttf')
    
        Window.clearcolor= (0.9, 0.8, 0.1)
        myLabel= Label(text="[b]Pundi's[/b]", markup=True, font_name='Superfont', font_size=50, pos_hint= {'center_x':0.5,'center_y': 0.9})
        myLabel.color = (0.5, 0.0, 0.2)

        monImage = Image(source="image2.jpg",size_hint=(None, None), size=(200, 200), pos_hint= {'center_x': 0.5,'center_y': 0.5})
        # myButton = Button(text= "Jouer", size= (40, 40), size_hint=(0.5, 0.1), pos_hint= {'center_x':0.5,'center_y': 0.2})

        fenetre= BoxLayout(size=(Window.width, Window.height))
        fenetre.add_widget(myLabel)
        fenetre.add_widget(monImage)
        # fenetre.add_widget(myButton)


        return fenetre
    


PundizzApp().run()