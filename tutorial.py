from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class newApp(App):
    def build(self):
        layout = BoxLayout(padding=10)
        bouton= Button(text='Appuis', pos_hint={'x': 0.5, 'y': 0.5})
        bouton.size_hint = (0.1, 0.1)
        bouton.background_color = [1,0,0,1]

        layout.add_widget(Label(text='Hello world'))
        layout.add_widget(bouton)
        return layout
    

if __name__ == '__main__':
    newApp().run()