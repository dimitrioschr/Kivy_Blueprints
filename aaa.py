from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

import random


class kkkApp(App):


    def ButtonLeftImage(self):
        box = BoxLayout(size_hint = (1, None), height = 50)
        but0 = Button(text = 'img',
                      size_hint = [0.15, 1])
        but1 = Button(text = str(int(100000 * random.random())),
                      size_hint = [0.7, 1])
        but2 = Button(text = 'X',
                      size_hint = [0.15, 1],
                      id = 'id1')
        box.add_widget(but0)
        box.add_widget(but1)
        box.add_widget(but2)
        return box, but2

    def do_popup(self):
        pu = Popup(title = 'title', size_hint = (0.5, 0.5))
        box = BoxLayout(orientation = 'vertical')
        lab = Label(text = 'text', size_hint = (1, 5))
        but = Button(text = 'Close', size_hint = (1, 1))
        box.add_widget(lab)
        box.add_widget(but)
        pu.add_widget(box)
        pu.open()
        but.bind(on_release = pu.dismiss)

    def do(self):
        element, clear = self.ButtonLeftImage()
        self.root.add_widget(element)
        self.root.add_widget(Widget())
        # add empty Widget() at the end to pad, remove before going
        # on to add another element, re-add to pad and so on...
        # So, maybe add one at creation...
        clear.bind(on_release = lambda x: element.parent.remove_widget(element))
        # lambda used to create callback function,
        # x is the clear Button (auto-returned from on_release)
        # element is to be removed (what we want to remove)


kkkApp().run()