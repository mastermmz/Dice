from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from random import randint


#Adjust the page size
Window.size = (150, 200)


# User interface design
Dice_helper = """
Screen:

    ScreenManager:
        MenuScreen:

<MenuScreen>:
    name:'menu'        

    MDLabel:
        id : number
        text: "Select the Start"
        pos_hint: {"center_x":0.68, "center_y":0.6}
    MDRaisedButton:
        text: "start"
        pos_hint: {"center_x":0.5, "center_y":0.35}
        on_release : root.random_number()

"""


# make class screen
class MenuScreen(Screen):
    def random_number(self):
        new_number = randint(1, 6)
        print(new_number)
        old_number = self.ids.number.text
        while new_number == old_number:
            print("Duplicate number")
            new_number = randint(1, 6)
        if new_number != old_number:
            number = str(new_number)
            self.ids.number.text = f"           {number}"


# add Menuscreen to app
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))


# make Basic App class
class DiceApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"  # ['Light', 'Dark']
        self.theme_cls.primary_palette = 'LightBlue'
        self.theme_cls.primary_hue = "A700"
        screen = Builder.load_string(Dice_helper)
        return screen


# run App
DiceApp().run()
