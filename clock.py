# __author__ = 'dimitrios'

from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
# from kivy.properties import ObjectProperty
# from kivy.uix.boxlayout import BoxLayout
from time import strftime


# class ClockLayout(BoxLayout):
#     time_prop = ObjectProperty(None)

class ClockApp(App):

    sw_started = False
    sw_seconds = 0

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)
        # schedule to run update_time() on every frame

    def update_time(self, dt):
        # dt is supplied by the caller (i.e. by Clock)
        time = strftime('[b]%H[/b]:%M:%S')
        if self.sw_started:
            self.sw_seconds += dt
        self.root.ids.time_label.text = time
        minutes = int(self.sw_seconds / 60)
        seconds = int(self.sw_seconds % 60)
        hundredths = int(self.sw_seconds * 100 % 100)
        self.root.ids.stopwatch_label.text = (
            '%02d:%02d.[size=40]%02d[/size]' %(minutes, seconds, hundredths)
        )

    def start_stop(self):
        if self.sw_started:
            self.root.ids.start_stop_button.text = 'Start'
        else:
            self.root.ids.start_stop_button.text = 'Stop'
        self.sw_started = not self.sw_started
        # on every click, reverse label text and sw_started state

    def reset(self):
        self.root.ids.start_stop_button.text = 'Start'
        self.sw_started = False
        self.sw_seconds = 0
        # revert everything to original states


if __name__ == '__main__':

    LabelBase.register(name='Roboto',
                       fn_regular='Roboto-Thin.ttf',
                       fn_bold='Roboto-Medium.ttf')

    Window.clearcolor = get_color_from_hex('#000000')

    ClockApp().run()