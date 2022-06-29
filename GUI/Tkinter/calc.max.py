from tkinter import*

root = Tk()
root.geometry("250x350")

text_input = StringVar()
operator =""

def btn(numbers):
	global operator
	operator = operator + str(numbers)
	text_input.set(operator)
	pass
def clearone():
	screen.delete(0,1)
	pass
def clearall():
	screen.delete(0,100)
	pass
def equal():
	global operator
	sumup= str(eval(operator))
	text_input.set(sumup)
	operator=""
	pass

#=======================Background color====================================================#
color = Frame(root,bg="grey")																#
color.place(relheight=1,relwidth=1)															#
#===========================================================================================#

#===========================Calculator Screen===============================================#
screen = Entry(color,bg="white",fg="black",justify="right",bd=3, textvariable=text_input)							#
screen.place(relx=0,rely=0,relwidth=1,relheight=0.17)										#
#===========================================================================================#

#===========================Buttons on Calculator===========================================#
numdel = 	Button(color,bg="grey",fg="black",text="del",command=clearone)									#
numdel.place(relx=0,rely=0.17,relwidth=0.25,relheight=0.15)									#
																							#
numC = 	Button(color,bg="grey",fg="black",text="C",command=clearall)											#
numC.place(relx=0.25,rely=0.17,relwidth=0.25,relheight=0.15)								#
																							#
numCE = 	Button(color,bg="grey",fg="black",text="CE",command=clearall)										#
numCE.place(relx=0.50,rely=0.17,relwidth=0.25,relheight=0.15)								#
																							#
numplus = 	Button(color,bg="orange",fg="white",text="+",command=lambda:btn("+"))									#
numplus.place(relx=0.75,rely=0.17,relwidth=0.25,relheight=0.15)								#
																							#
num1 = 	Button(color,bg="white",fg="black",text="1",command=lambda: btn("1"))										#
num1.place(relx=0,rely=0.32,relwidth=0.25,relheight=0.17)									#
																							#
num2 = 	Button(color,bg="white",fg="black",text="2",command=lambda:btn("2"))										#
num2.place(relx=0.25,rely=0.32,relwidth=0.25,relheight=0.17)								#
																							#
num3 = 	Button(color,bg="white",fg="black",text="3",command=lambda:btn("3"))										#
num3.place(relx=0.50,rely=0.32,relwidth=0.25,relheight=0.17)								#
																							#
numminus = 	Button(color,bg="orange",fg="white",text="-",command=lambda:btn("-"))									#
numminus.place(relx=0.75,rely=0.32,relwidth=0.25,relheight=0.17)							#
																							#
num4 = 	Button(color,bg="white",fg="black",text="4",command=lambda:btn("4"))										#
num4.place(relx=0,rely=0.49,relwidth=0.25,relheight=0.17)									#
																							#
num5 = 	Button(color,bg="white",fg="black",text="5",command=lambda:btn("5"))										#
num5.place(relx=0.25,rely=0.49,relwidth=0.25,relheight=0.17)								#
																							#
num6 = 	Button(color,bg="white",fg="black",text="6",command=lambda:btn("6"))										#
num6.place(relx=0.50,rely=0.49,relwidth=0.25,relheight=0.17)								#
																							#
numdiv = Button(color,bg="orange",fg="white",text="/",command=lambda:btn("/"))										#
numdiv.place(relx=0.75,rely=0.49,relwidth=0.25,relheight=0.17)								#
																							#
num7 = 	Button(color,bg="white",fg="black",text="7",command=lambda:btn("7"))										#
num7.place(relx=0,rely=0.66,relwidth=0.25,relheight=0.17)									#
																							#
num8 = 	Button(color,bg="white",fg="black",text="8",command=lambda:btn("8"))										#
num8.place(relx=0.25,rely=0.66,relwidth=0.25,relheight=0.17)								#
																							#
num9 = 	Button(color,bg="white",fg="black",text="9",command=lambda:btn("9"))										#
num9.place(relx=0.50,rely=0.66,relwidth=0.25,relheight=0.17)								#
																							#
numtim = Button(color,bg="orange",fg="white",text="X",command = lambda:btn("*"))										#
numtim.place(relx=0.75,rely=0.66,relwidth=0.25,relheight=0.17)								#
																							#
num0 = Button(color,bg="white",fg="black", text="0",command=lambda:btn("0"))										#
num0.place(relx=0,rely=0.83,relwidth=0.50,relheight=0.17)									#
																							#
numequ = Button(color,bg="orange",fg="white", text="=",command=equal)										#
numequ.place(relx=0.75,rely=0.83,relwidth=0.25,relheight=0.17)								#
																							#
numdot = Button(color,bg="white",fg="black", text=".",command=lambda:btn("."))										#
numdot.place(relx=0.50,rely=0.83,relwidth=0.25,relheight=0.17)								#
#===========================================================================================#

#===============================Ending it All===============================================#
root.mainloop()																				#
#===========================================================================================#