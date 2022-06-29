import re
import math
from kivy.app import App
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex as hexColor

Window.clearcolor = hexColor('#dddddd') #Changes the window color

# Register custom fonts
LabelBase.register(name = 'Roboto',
        fn_regular = 'fonts/Roboto-Thin.ttf',
        fn_bold = 'fonts/Roboto-Regular.ttf')

# trigonometric functions that return degrees instead of radians

sin = lambda num: math.sin(math.radians(num))

cos = lambda num: math.cos(math.radians(num))

tan = lambda num: math.tan(math.radians(num))


# The main app
class CalculatorApp(App):
    ''' This is a simple calculator app which is designed to work
    like a clone of the original android calculator'''

    # Colors used 
    colors = {
        'white': hexColor('#ffffff'),
        'red': hexColor('#ff0000'),
        'green': hexColor('#00ff00'),
        'grey': hexColor('#dddddd'),
        'black': hexColor('#000000')
    }

    # checks if the equal button is pressed
    equal_pressed = False

    def make_evaluable(self, exp):
        ''' converts the screen label string into an evaluable
        expression'''
        # using normal replace function to replace unrecognized symbols
        exp = exp.replace('÷', '/')
        exp = exp.replace('×', '*')
        exp = exp.replace('^', '**')
        exp = exp.replace('π', 'math.pi')  
        exp = exp.replace('e', 'math.e')

        # using regex for complex replacements
        exp = re.sub(r'√(\+)', r'math.sqrt(\)', exp)
        exp = re.sub(r'(\+)!', r'math.factorial(\)', exp)
        exp = re.sub(r'(\+)\(\+)\ ', r'\*(\) ', exp)
        exp = re.sub(r'(\+)\\', r'\)*(', exp)
        exp = re.sub(r'(\+)\(\+)', r'\*\ ', exp)
        exp = re.sub(r'(\+)math.pi', r'\*math.pi', exp)

        return exp

    def keypad_press(self, text):
        ''' display text on the screen label once a button is pressed'''
        scrn = self.root.ids.screen
        scrn.text = scrn.text + str(text)
        self.auto_solve()

    def delete_clear(self):
        ''' deletes text and clears the entire screen label'''
        rescrn, scrn = self.root.ids.res_screen, self.root.ids.screen

        if self.equal_pressed:
            scrn.text = ''
            rescrn.text = ''
            rescrn.color = (.3,.3,.3,.6)
            self.equal_pressed = False
            self.root.ids.del_clr_btn.text = 'DEL'

        else:
            exp = list(scrn.text)

            if ''.join(exp[len(exp) - 2:]) in ('n(', 's('):
                del exp[len(exp) - 4:]

            elif len(exp) > 0:
                exp.pop()

            scrn.text = ''.join(exp)
            self.auto_solve()


    def solve(self):
        '''solves the expression on the screen label'''
        rescrn, scrn = self.root.ids.res_screen, self.root.ids.screen
        
        if scrn.text:
            try:
                self.equal_pressed = True
                exp = scrn.text
                exp = self.make_evaluable(exp)
                solution = eval(exp)
                scrn.text = str(round(solution, 5))
                rescrn.text = ''

            except SyntaxError:
                rescrn.text = 'Syntax Error'
                rescrn.color = self.colors['red']

            except ZeroDivisionError:
                rescrn.text = 'Infinty'
                rescrn.color = self.colors['red']

            self.root.ids.del_clr_btn.text = 'CLR'


    def check_evaluable(self, exp):
        ''' checks if the expression text on the screen label can be evaluated without an error'''
        try:
            eval(exp)
            return True
        except (SyntaxError, ZeroDivisionError):
            return False


    def auto_solve(self):
        ''' automatically solves the expression only if it is evaluable'''
        rescrn,scrn = self.root.ids.res_screen, self.root.ids.screen
        exp = scrn.text
        exp = self.make_evaluable(exp)

        if self.check_evaluable(exp):
            rescrn.color = (.3, .3, .3, .6)
            rescrn.text = str(round(eval(exp), 5))
        else: rescrn.text = ''    


if __name__ == '__main__': CalculatorApp().run()