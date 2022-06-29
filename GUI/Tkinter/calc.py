from tkinter import Tk, StringVar, Button, Entry, Frame

root = Tk()
root.geometry("250x350")

text_input = StringVar()
operator =""

def equal():
	global operator
	sumup= str(eval(operator))
	text_input.set(sumup)
	operator=""


def clearone():
	screen.delete(0,1)


def clearall():
	screen.delete(0,100)


def btn(numbers):
	if   numbers=='=':  equal()
	elif numbers=='del':clearone()
	elif numbers=='C':  clearall()
	elif numbers=='CE': clearall()
	else:
		global operator
		operator = operator + str(numbers)
		text_input.set(operator)



color = Frame(root,bg="grey")
color.place(relheight=1,relwidth=1)

#===========================Calculator Screen===============================================#
screen = Entry(color,bg="white",fg="black",justify="right",bd=3, textvariable=text_input)#
screen.place(relx=0,rely=0,relwidth=1,relheight=0.17)
#===========================================================================================#

num = lambda s: Button(color,bg="white" ,fg="black", text=s, command=lambda: btn(s))
alt = lambda s: Button(color,bg="grey"  ,fg="black", text=s, command=lambda: btn(s))
sign= lambda s: Button(color,bg="orange",fg="white", text='X' if s == '*' else s,command=lambda: btn(s))


#===========================Buttons on Calculator=========================================

numdel= alt("del").place(relx=0,   rely=0.17,relwidth=0.25,relheight=0.15)

numC = alt("C")   .place(relx=0.25,rely=0.17,relwidth=0.25,relheight=0.15)

numCE = alt("CE") .place(relx=0.50,rely=0.17,relwidth=0.25,relheight=0.15)

numplus= sign("+").place(relx=0.75,rely=0.17,relwidth=0.25,relheight=0.15)

num1 = num('1')   .place(relx=0,   rely=0.32,relwidth=0.25,relheight=0.17)

num2 = num('2')   .place(relx=0.25,rely=0.32,relwidth=0.25,relheight=0.17)

num3 = num('3')   .place(relx=0.50,rely=0.32,relwidth=0.25,relheight=0.17)

numminus=sign("-").place(relx=0.75,rely=0.32,relwidth=0.25,relheight=0.17)

num4 = num("4")   .place(relx=0,   rely=0.49,relwidth=0.25,relheight=0.17)

num5 = num("5")   .place(relx=0.25,rely=0.49,relwidth=0.25,relheight=0.17)

num6 = num("6")   .place(relx=0.50,rely=0.49,relwidth=0.25,relheight=0.17)

numdiv = sign("/").place(relx=0.75,rely=0.49,relwidth=0.25,relheight=0.17)

num7 = num("7")   .place(relx=0,   rely=0.66,relwidth=0.25,relheight=0.17)

num8 = num("8")   .place(relx=0.25,rely=0.66,relwidth=0.25,relheight=0.17)

num9 = num("9")   .place(relx=0.50,rely=0.66,relwidth=0.25,relheight=0.17)

numtim = sign("*").place(relx=0.75,rely=0.66,relwidth=0.25,relheight=0.17)

num0 = num("0")   .place(relx=0   ,rely=0.83,relwidth=0.50,relheight=0.17)

numdot = num(".") .place(relx=0.50,rely=0.83,relwidth=0.25,relheight=0.17)

numequ = sign('=').place(relx=0.75,rely=0.83,relwidth=0.25,relheight=0.17)


root.mainloop()
