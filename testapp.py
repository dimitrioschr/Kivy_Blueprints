__author__ = 'operation3'

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class TestApp(App):
    pass

    def presser(self):
        popup_button = Button(text='You pressed button 11',
                              font='Roboto',
                              font_size=20)
        popup = Popup(title='Warning',
                      title_font='Roboto',
                      title_size=40,
                      separator_color = [0, 0.66, 0, 0.66],
                      content=popup_button,
                      size_hint=(0.5, 0.5),
                      auto_dismiss = False
                      )
        popup_button.bind(on_press=popup.dismiss)
        popup.open()


if __name__ == '__main__':
    LabelBase.register(name = 'Roboto',
                       fn_regular = 'Roboto-Thin.ttf',
                       fn_bold = 'Roboto-Medium.ttf')
    Window.clearcolor = get_color_from_hex('#000000')
    TestApp().run()
