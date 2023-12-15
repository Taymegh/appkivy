from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.checkbox import CheckBox
from kivy.uix.carousel import Carousel
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.spinner import Spinner
# from kivy.uix.progressbar import ProgressBar




class TestApp(App):
    def build(self):
        Window.clearcolor = (0.4, 0.7, 0.9, 0.8)
        layout = BoxLayout(orientation='vertical', size=(Window.width, Window.height))
        

        label = Label(
            text='Hello, world',
            color=(0.9, 1, 0, 1)
        )
        mon_spinner = Spinner(
            text= 'Lavisan',
            values=('Lavisan', 'Sarubn', 'Taysir'),
            size_hint=(None, None),
            size= (100, 44),
            pos_hint={'center_x': .5, 'center_y': .5})
        

        # ma_barre= ProgressBar(max=1000)
        # ma_barre.value = 750
        self.valeur_slider = Label()
        text_input = TextInput(multiline=False)
        self.mon_image= Image(source="image2.jpg",size_hint=(None, None), size=(400, 500))
        mon_button= Button(text= "Clique")
        mon_button.bind(on_press=self.cacher_image) 
        button2 = Button(text="karuppu")

        ma_checkbox= CheckBox()

        self.mon_slider= Slider(min=0, max=100, value=10)



        # mon_carousel = Carousel(direction='right', size=(200, 300), pos_hint={'center_x': 0.2, 'center_y': 0.4})
        # for i in range(1, 3, 1):
        #     src = f"image{i}.jpg"
        #     image_carousel = Image(source=src, size=(300, 200), size_hint=(None, None), x=(mon_carousel.width - 300) / 2)
        #     mon_carousel.add_widget(image_carousel)
        # mon_carousel.load_next()

        layout.add_widget(label)
        layout.add_widget(text_input)
        layout.add_widget(self.mon_image)
        layout.add_widget(mon_button)
        layout.add_widget(self.mon_slider)
        self.mon_slider.bind(value=self.afficher_valeur)
        layout.add_widget(self.valeur_slider)
        layout.add_widget(ma_checkbox)
        layout.add_widget(mon_spinner)
        layout.add_widget(button2)
        # layout.add_widget(mon_carousel)
        # layout.add_widget(ma_barre)

        return layout
    
    def cacher_image(self, instance):
        if self.mon_image.opacity == 0:
            self.mon_image.opacity = 1
        elif self.mon_image.opacity == 1:
            self.mon_image.opacity = 0

    def afficher_valeur(self, instance, valeur):
        self.valeur_slider.text= str(valeur)

    # def montrer_valeur(mon_spinner, text):
    #     print()

class fullImage(Image):
        pass


TestApp().run()
