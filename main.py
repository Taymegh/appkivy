from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class QuizApp(App):
    def build(self):
        label = Label(text='Pundizz', align ='center')
        return label
    
QuizApp().run()
