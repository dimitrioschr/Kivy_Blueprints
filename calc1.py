__author__ = 'operation3'

from kivy.app import App
from kivy.uix.button import Button


class APSDOPCalculatorApp(App):

    line_number = 1

    def tester(self):
        if self.line_number < 10:
            self.root.ids.list.add_widget(Button(text = str(self.line_number),
                                                 size_hint = (1, None),
                                                 height = 50))
            self.line_number += 1


if __name__ == '__main__':
    APSDOPCalculatorApp().run()