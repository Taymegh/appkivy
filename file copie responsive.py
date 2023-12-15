from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout

from kivy.core.text import LabelBase



class PundizzApp(App):
    def build(self):


        LabelBase.register(name="Superfont", fn_regular='superfont.ttf')
    
        label_layout= RelativeLayout(size=(Window.width, Window.height))

        Window.clearcolor= (0.9, 0.8, 0.1)
        myLabel= Label(
            text="[b]Pundi's[/b]", 
            markup=True, 
            font_name='Superfont', 
            font_size=50, 
            pos_hint= {'center_x': 1.125,'center_y': 0.9})
        myLabel.color = (0.5, 0.0, 0.2)

        label_layout.add_widget(myLabel)

        image_layout= RelativeLayout(size=(Window.width, Window.height))
        self.monImage = Image(
            source="image2.jpg",
            size=(200, 200), 
            size_hint=(None, None), 
            pos_hint= {'center_x': 0.1, 'center_y': 0.7})
        

        button_layout= RelativeLayout(size=(Window.width, Window.height))
        myButton = Button(
            text= "Jouer", 
            size= (150, 100), 
            size_hint=(None, None),  
            pos_hint= {'center_x': -0.9,'center_y': 0.5})
        button_layout.add_widget(myButton)
        myButton.bind(on_press=self.hide_image)
        image_layout.add_widget(self.monImage)

        fenetre= BoxLayout(size=(Window.width, Window.height))
        fenetre.add_widget(label_layout)
        fenetre.add_widget(image_layout)
        fenetre.add_widget(button_layout)


        return fenetre
    
    def hide_image(self, instance):
        if self.monImage.opacity == 0:
            self.monImage.opacity= 1
        elif self.monImage.opacity == 1:
            self.monImage.opacity= 0


PundizzApp().run()