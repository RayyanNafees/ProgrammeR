from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex as hexColor
from kivy.clock import Clock

Window.clearcolor = hexColor('#154050') # Background Color

class ClockApp(App):
    """ Initialize the app """

    sw_seconds = 0
    started = False

    def update_clock(self, nap):
        """ change the text in the time label """
        
        import time 
        self.root.ids.time.text = time.strftime('[b]%H[/b]:%M:%S')


    def update_stopwatch(self, nap):
        """ change the text in the stopwatch label """

        if self.started: # check if the stopwatch has started
            self.sw_seconds += nap
            minutes, seconds = divmod(self.sw_seconds, 60)
            self.root.ids.stopwatch.text = f"{int(minutes)}:{int(seconds)}.[size=40]{int(seconds * 100 % 100)}[/size]" # change the text


    def start_stop(self):
        """ start or stop the stopwatch """
        self.root.ids.startstop_btn.text = 'start' if self.started else 'stop'
        self.started = not self.started


    def reset(self):
        """ reset the stopwatch """

        if self.started: self.root.ids.startstop_btn.text = 'start'

        self.root.ids.stopwatch.text = '0:0.[size=40]00[/size]'
        self.sw_seconds = 0
        self.started = False


    def on_start(self):
        """ start the clock and stopwatch immediately the app starts """
        Clock.schedule_interval(self.update_clock, 1)
        Clock.schedule_interval(self.update_stopwatch, 0)

if __name__ == '_main_':
    ClockApp().run()