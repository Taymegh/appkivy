from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.label import MDLabel
from kivy.uix.actionbar import ActionBar
from kivy.uix.boxlayout import BoxLayout

# from kivymd.uix.label import MDLabel


class mainApp(MDApp):
    def build(self):
        layout= BoxLayout(orientation= 'vertical')
        action= ActionBar()
        layout.add_widget(action)
        label= MDLabel(text="Lawis", halign= "center")
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