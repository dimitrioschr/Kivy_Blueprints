import random

from kivy.app import App

from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class kkkApp(App):

    class MaPopup(Popup):
        pass

    class ListElement(BoxLayout):
        pass

    def random_label(self):
        return str(int(100000 * random.random()))

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

    def do2(self):
        element = self.ListElement()
        clear = element.children[0]
        self.root.add_widget(element)
        # clear.bind(on_release = lambda x: element.parent.remove_widget(element))


kkkApp().run()