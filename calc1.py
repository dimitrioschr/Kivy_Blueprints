__author__ = 'operation3'

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class APSDOPCalculatorApp(App):

    line_number = 1

    def add_element(self):
        if self.line_number < 10:
            self.root.ids.list.add_widget(Button(text = str(self.line_number),
                                                 size_hint = (1, None),
                                                 height = 50))
            self.line_number += 1

    def input_cp(self):
        label = Label(text = 'replace with\ncustom widget\nhere',
                      size_hint = (1, 5))
        button = Button(text = 'Close',
                        size_hint = (1, 1))
        box = BoxLayout(orientation = 'vertical')
        box.add_widget(label)
        box.add_widget(button)
        popup = Popup(title = 'Input agreed APS and hire rates',
                      content = box)
        button.bind(on_press = popup.dismiss)
        popup.open()

    def input_vsl(self):
        pass

    def reset(self):
        self.root.ids.list.clear_widgets()
        self.line_number = 1

    def calculate(self):
        pass



if __name__ == '__main__':
    APSDOPCalculatorApp().run()