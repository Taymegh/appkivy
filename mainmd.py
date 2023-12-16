from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.label import MDLabel
from kivy.uix.actionbar import ActionBar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
# from kivy.uix.actionbar import ActionView
# from kivy.uix.actionbar import ActionItem

# from kivymd.uix.label import MDLabel


class mainApp(MDApp):
    def build(self):
        layout= BoxLayout(orientation= 'vertical')
        texte= MDLabel(text="Pundizz", size_hint=(None, None), pos_hint= {'center_x': 0.5,'center_y': 0.5})
        action= ActionBar(
            pos= (0,0),
            size_hint=(1, 0.1),
            background_color= (0, .02, .9, .5),
        )

        # action_view = ActionView()

        # button= MDFlatButton(text='Tompere')
        # action_view.add_widget(CustomActionItem(content=button))

        # action.add_widget(action_view)


        # layout.add_widget(action)
        layout.add_widget(texte)
        return layout
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Red"    

    # def on_start(self):
    #     # self.fps_monitor_start()
    #     pass
        # return (
        #     MDScreen(
        #         MDRectangleFlatButton(
        #             text= "Bonjour, Taysir.",
        #             pos_hint= {'center_x': 0.5,'center_y': 0.5},
        #         )
        #     )
        # )
        # return MDLabel(text="Bonjour, Taysir.", halign="center")




mainApp().run()