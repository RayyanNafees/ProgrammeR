from kivy.app import App
from kivy.utils import get_color_from_hex as hexColor
from kivy.core.text import LabelBase
from randomchar import digit

class colorApp(App):
    def change_color(self):
        rnd_color = "#" + digit.hexadecimal(6).upper()
        self.root.ids.color_name.text = rnd_color
        self.root.ids.color_screen.background_color = hexColor(rnd_color)


if __name__ == "__main__": # Register custom fonts
    LabelBase.register(name = 'OpenSans',
        fn_regular = 'fonts/OpenSans-Regular.ttf',
        fn_bold = 'fonts/OpenSans-Bold.ttf')

    colorApp().run()