from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.slider import Slider


class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(
            text='Hello, world',
            color=(0.9, 1, 0, 1)
        )
        self.valeur_slider = Label()
        text_input = TextInput(multiline=False)
        self.mon_image= Image(source="sarubn.jpg")
        mon_button= Button(text= "Clique")
        mon_button.bind(on_press=self.cacher_image) 

        self.mon_slider= Slider(min=0, max=100, value=10)


        layout.add_widget(label)
        layout.add_widget(text_input)
        layout.add_widget(self.mon_image)
        layout.add_widget(mon_button)
        layout.add_widget(self.mon_slider)
        self.mon_slider.bind(value=self.afficher_valeur)
        layout.add_widget(self.valeur_slider)
        return layout
    
    def cacher_image(self, instance):
        if self.mon_image.opacity == 0:
            self.mon_image.opacity = 1
        elif self.mon_image.opacity == 1:
            self.mon_image.opacity = 0

    def afficher_valeur(self, instance, valeur):
        self.valeur_slider.text= str(valeur)

TestApp().run()
