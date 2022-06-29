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


color = Frame(root,bg='grey')
color.place(relheight=1,relwidth=1)

#===========================Calculator Screen===============================================#
screen = Entry(color,bg='white',fg='black',justify='right',bd=3, textvariable=text_input).place(relx=0,rely=0,relwidth=1,relheight=.17)
#===========================================================================================#

num = lambda s, x,y: Button(color,bg='white' ,fg='black', text=s, command=lambda: btn(s)).place(relx=x, rely=y, relwidth=.25 if s!='0' else .5, relheight=.17)
alt = lambda s, x: Button(color,bg='grey'  ,fg='black', text=s, command=lambda: btn(s)).place(relx=x, rely=.17, relwidth=.25, relheight=.15)
sign= lambda s, x,y: Button(color,bg='orange',fg='white', text='X'if s=='*'else s,command=lambda: btn(s)).place(relx=x, rely=y, relwidth=.25, relheight=.17 if s!='+'else .15)


#===========================Buttons on Calculator=========================================

numdel=   alt('del', 0)
numC =    alt('C', .25)
numCE =   alt('CE',.50)
numplus= sign('+', .75, .17)

num1 =    num('1',   0, .32)
num2 =    num('2', .25, .32)
num3 =    num('3', .50, .32)
numminus=sign('-', .75, .32)

num4 =    num('4',   0, .49)
num5 =    num('5', .25, .49)
num6 =    num('6', .50, .49)
numdiv = sign('/', .75, .49)

num7 =    num('7',   0, .66)
num8 =    num('8', .25, .66)
num9 =    num('9', .50, .66)
numtim = sign('*', .75, .66)

num0 =    num('0',   0, .83)
numdot =  num('.', .50, .83)
numequ = sign('=', .75, .83)


root.mainloop()
