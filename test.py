from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout

class MyApp(App):
    def build(self):
        # Creating a layout
        main_layout = RelativeLayout()#orientation='horizontal')
        # layout = BoxLayout(size_hint=(None,None) , size=(100,100))


        # Creating a button
        button = Button(text='Press me', size_hint=(None,None), size=(200, 200), pos_hint= {'center_x': 0.5,'center_y': 0.5})

        # Binding the button to a function
        button.bind(on_press=self.on_button_press)

        # Adding the button to the layout
        # layout.add_widget(button)

        main_layout.add_widget(button)

        return main_layout

    def on_button_press(self, instance):
        # Define what happens when the button is pressed
        print("Button pressed!")

if __name__ == '__main__':
    MyApp().run()