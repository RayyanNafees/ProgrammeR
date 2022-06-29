from tkinter import Tk, StringVar, Button, Entry, Frame

root = Tk()
root.geometry('250x350')

text_input = StringVar()
operator =''

def equal():
	global operator
	sumup= str(eval(operator))
	text_input.set(sumup)
	operator=''

color = Frame(root,bg='grey')
color.place(relheight=1,relwidth=1)

#===========================Calculator Screen===============================================#
screen = Entry(color,bg='white',fg='black',justify='right',bd=3, textvariable=text_input).place(relx=0,rely=0,relwidth=1,relheight=.17)
#===========================================================================================#

clearone = lambda: screen.delete(0,1)
clearall = lambda: screen.delete(0,100)

def btn(numbers):
	if   numbers=='=':  equal()
	elif numbers=='del':clearone()
	elif numbers=='C':  clearall()
	elif numbers=='CE': clearall()
	else:
		global operator
		operator = operator + str(numbers)
		text_input.set(operator)

num = lambda s, y,x: Button(color,bg='white' ,fg='black', text=s, command=lambda: btn(s)).place(relx=x, rely=y, relwidth=.25 if s!='0' else .5, relheight=.17)
alt = lambda s, x  : Button(color,bg='grey'  ,fg='black', text=s, command=lambda: btn(s)).place(relx=x, rely=.17, relwidth=.25, relheight=.15)
sign= lambda s,y: Button(color,bg='orange',fg='white', text='X'if s=='*'else s,command=lambda: btn(s)).place(relx=.75, rely=y, relwidth=.25, relheight=.17 if s!='+'else .15)


#===========================Buttons on Calculator=========================================

for s,x in zip(('del','C','CE'), (0,.25,.5)): alt(s, x)
numplus= sign('+', .17)

num1 =    num('1', .32,   0)
num2 =    num('2', .32, .25)
num3 =    num('3', .32, .50)
numminus=sign('-', .32)

num4 =    num('4', .49,   0)
num5 =    num('5', .49, .25)
num6 =    num('6', .49, .50)
numdiv = sign('/', .49)

num7 =    num('7', .66,   0)
num8 =    num('8', .66, .25)
num9 =    num('9', .66, .50)
numtim = sign('*', .66)

num0 =    num('0', .83,   0)
numdot =  num('.', .83, .50)
numequ = sign('=', .83)


root.mainloop()
