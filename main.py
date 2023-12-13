from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Buttons

class Quiz_app(App):
    def __init__(self,questions,score):
        self