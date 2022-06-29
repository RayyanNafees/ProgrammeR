# FizzBuzz with Kivy GUI
# Author: Franklin Ikeh
import time
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import get_color_from_hex as hexColor

Window.clearcolor = hexColor('#DDDDFF') # change window color

class FizzBuzzApp(App):
    # some useful variables
    started = False
    finished = False
    number = 1

    def update_fb(self, nap):
        '''
        This method updates the numbers,
         shown on the screen each time it is called
        '''

        if self.started:

            def current_num(number, show_num=False):
                '''
                This function determines whether the current number is
                fizz, buzz or fizzbuzz
                '''

                if not (number % 3 and number % 5):
                    return f'[color=#FF00AA]Fizz[/color][color=#DD00DD]Buzz[/color]'

                elif not number % 3:
                    return f'[color=#00BB00]Fizz[/color]'

                elif not number % 5:
                    return f'[color=#EE0000]Buzz[/color]'

                else: # whether to show the current number or not
                    return number if show_num else ''


            self.root.ids.fb_scr.text = str(current_num(self.number))
            self.root.ids.num_scr.text = str(self.number)
            self.root.ids.fb_num_scr.text = (
                self.root.ids.fb_num_scr.text + '    ' + str(current_num(self.number, True))
            )

            if self.number < 100:  # increment the number after each function call
                self.number += 1

            elif self.number == 100:
                self.started = not self.started # stop the loop
                self.root.ids.start_btn.text = 'Start'
                self.number = 1 # reset the number
                self.finished = True


    def start_stop(self):
        ''' This method starts, stop, pause or continues the program'''
        start, fbscr = self.root.ids.start_btn, self.root.ids.fb_num_scr
        if self.finished:
            fbscr.text = '' # clear the label
            self.started, self.finished = True, False
        else:
            self.started = not self.started

        if not self.started and self.number < 100:
            start.text = 'Continue'
        elif self.started:
            start.text = 'Pause'


    on_start = lambda self: Clock.schedule_interval(self.update_fb, .35)


if __name__ == '__main__': FizzBuzzApp().run()