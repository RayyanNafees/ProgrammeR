#===========================beginings=====================================================================================

from tkinter import*
import random
import time 
 
HEIGHT = 650
WIDTH = 1300
root = Tk()
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
root.title("SOMETHING DAMN CRAZY")
StringVar = StringVar()
operator=""

#=================definition buttons=====================================================================================    
def btnclearDisplay():
    global operator
    operator=operator + str()
    entry9.delete(0,9)
    
    
def btnClick(numbers):
    global operator
    operator= operator + str(numbers)
    StringVar.set(operator)
    
    
def btnEquals():
    global operator
    sumup = str(eval(operator))
    StringVar.set(sumup)
    operator=""
    
#================================makeup==================================================================================

lblInfo = Label(root, font=('arial',30, 'bold'), text='SOMETHING DAMN CRAZY', fg="steelblue", bd=10, anchor='w')
lblInfo.place(relx=0.1)

frame = Frame(root, bg='powderblue')
frame.place(relheight=0.82, relwidth=0.89, relx=0.06, rely=0.08)


#=====================================time===============================================================================
localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(root, fg='steelblue', font=('itlics',20, 'bold'), text=localtime)
lblInfo.place(relx=0.7, rely=0.02)

 
#=====================================food===============================================================================

button = Label(frame, bg='powderblue', fg='black', text='CHICKEN',font=('arial',20, 'bold'), bd=10)
button.place(relwidth=0.16, relx=0.03, rely=0.02, relheight=0.1)

entry1 = Entry(frame, bg='white', font=('arial',20, 'bold'), bd=10, justify='right')
entry1.place(relwidth=0.2, relx=0.23, rely=0.02, relheight=0.1)

button = Label(frame, bg='powderblue', fg='black', text='FISH',font=('arial',20, 'bold'), bd=10) 
button.place(relwidth=0.16, relx=0.03, rely=0.12, relheight=0.1)

entry2 = Entry(frame, bg='white', font=('arial',20, 'bold'), bd=10, justify='right')
entry2.place(relwidth=0.2, relx=0.23, rely=0.12, relheight=0.1)

button = Label(frame, bg='powderblue', fg='black', text='BEEF',font=('arial',20, 'bold'), bd=10)
button.place(relwidth=0.16, relx=0.03, rely=0.22, relheight=0.1)

entry3 = Entry(frame, bg='white', font=('arial',20, 'bold'), bd=10, justify='right')
entry3.place(relwidth=0.2, relx=0.23, rely=0.22, relheight=0.1)

button = Label(frame, bg='powderblue', fg='black', text='PIZZA',font=('arial',20, 'bold'),bd=10)
button.place(relwidth=0.16, relx=0.03, rely=0.32, relheight=0.1)

entry4 = Entry(frame, bg='white', font=('arial',20, 'bold'), bd=10, justify='right')
entry4.place(relwidth=0.2, relx=0.23, rely=0.32, relheight=0.1)

button = Label(frame, bg='powderblue', fg='black', text='J.RICE',font=('arial',20, 'bold'), bd=10)
button.place(relwidth=0.16, relx=0.03, rely=0.42, relheight=0.1)

entry5 = Entry(frame, bg='white', font=('arial',20, 'bold'), bd=10, justify='right')
entry5.place(relwidth=0.2, relx=0.23, rely=0.42, relheight=0.1)

button = Label(frame, bg='powderblue', fg='black', text='RICE.S',font=('arial',20, 'bold'), bd=10)
button.place(relwidth=0.16, relx=0.03, rely=0.52, relheight=0.1)

entry6 = Entry(frame, bg='white', font=('arial',20, 'bold'), bd=10, justify='right')
entry6.place(relwidth=0.2, relx=0.23, rely=0.52, relheight=0.1)

button = Label(frame, bg='powderblue', fg='black', text='PEPSI',font=('arial',20, 'bold'), bd=10)
button.place(relwidth=0.16, relx=0.03, rely=0.62, relheight=0.1)

entry7 = Entry(frame, bg='white', font=('arial',20, 'bold'), bd=10, justify='right')
entry7.place(relwidth=0.2, relx=0.23, rely=0.62, relheight=0.1)

button = Label(frame, bg='powderblue', fg='black', text='MIRINDA', bd=10, font=('arial',20, 'bold'))
button.place(relwidth=0.16, relx=0.03, rely=0.72, relheight=0.1)

entry8 = Entry(frame, bg='white', font=('arial',20, 'bold'), bd=10, justify='right')
entry8.place(relwidth=0.2, relx=0.23, rely=0.72, relheight=0.1)


# other buttons:

button = Button(root, bg='grey', fg='black',font=('arial',20, 'bold'), bd=10, text='RESET')
button.place(relwidth=0.16, relx=0.3, rely=0.92, relheight=0.08)

button = Button(root, bg='grey', fg='black',text='QUIT', bd=10, font=('arial',20, 'bold'), command=root.destroy)
button.place(relwidth=0.16, relx=0.46, rely=0.92, relheight=0.08)

button = Button(frame, bg='grey', fg='black',font=('arial',20, 'bold'), bd=10, text='TOTAL')
button.place(relwidth=0.1, relx=0.25, rely=0.85, relheight=0.1)

entry = Entry(frame, bg='white', font=('arial',20, 'bold'), bd=10 )
entry.place(relwidth=0.2, relx=0.38, rely=0.85, relheight=0.1)


# calculator:

entry9 = Entry(frame, font=('arial',20, 'bold'), textvariable=StringVar, bd=30, bg='white', justify='right')
entry9.place(relwidth=0.3, relx=0.6, rely=0.04)

button = Button(frame, bg='grey', fg='black', text='1', font=('arial',20, 'bold'), bd=10, command=lambda: btnClick('1'))
button.place(relwidth=0.058, relx=0.6, rely=0.24, relheight=0.15)

button = Button(frame, bg='grey', fg='black', text='4', font=('arial',20, 'bold'), bd=10, command=lambda: btnClick('4'))
button.place(relwidth=0.058, relx=0.6, rely=0.4, relheight=0.15)

button = Button(frame, bg='grey', fg='black', text='7', font=('arial',20, 'bold'), bd=10, command=lambda: btnClick('7'))
button.place(relwidth=0.058, relx=0.6, rely=0.56, relheight=0.15)

button = Button(frame, bg='grey', fg='black', text='C', font=('arial',20, 'bold'), bd=10, command=btnclearDisplay)
button.place(relwidth=0.058, relx=0.6, rely=0.72, relheight=0.15)

button = Button(frame, bg='grey', fg='black', text='2', font=('arial',20, 'bold'), bd=10, command=lambda: btnClick('2'))
button.place(relwidth=0.058, relx=0.68, rely=0.24, relheight=0.15)

button = Button(frame, bg='grey', fg='black', text='5', font=('arial',20, 'bold'), bd=10, command=lambda: btnClick('5'))
button.place(relwidth=0.058, relx=0.68, rely=0.4, relheight=0.15)

button = Button(frame, bg='grey', fg='black', text='8', font=('arial',20, 'bold'), bd=10, command=lambda: btnClick('8'))
button.place(relwidth=0.058, relx=0.68, rely=0.56, relheight=0.15)

button = Button(frame, bg='grey', fg='black', text='0', font=('arial',20, 'bold'), bd=10, command=lambda: btnClick('0'))
button.place(relwidth=0.058, relx=0.68, rely=0.72, relheight=0.15)

button = Button(frame, bg='grey', fg='black', text='3', font=('arial',20, 'bold'), bd=10, command=lambda: btnClick('3'))
button.place(relwidth=0.058, relx=0.76, rely=0.24, relheight=0.15)

button = Button(frame, bg='grey', fg='black', text='6', font=('arial',20, 'bold'), bd=10, command=lambda: btnClick('6'))
button.place(relwidth=0.058, relx=0.76, rely=0.4, relheight=0.15)

button = Button(frame, bg='grey', fg='black', text='9', font=('arial',20, 'bold'), bd=10, command=lambda: btnClick('9'))
button.place(relwidth=0.058, relx=0.76, rely=0.56, relheight=0.15)

button = Button(frame, bg='grey', fg='black', text='=', font=('arial',20, 'bold'), bd=10, command=btnEquals)
button.place(relwidth=0.058, relx=0.76, rely=0.72, relheight=0.15)

button = Button(frame, bg='grey', fg='black', text='+', font=('arial',20, 'bold'), bd=10, command=lambda: btnClick("+"))
button.place(relwidth=0.058, relx=0.84, rely=0.24, relheight=0.15)

button = Button(frame, bg='grey', fg='black', text='-', font=('arial',20, 'bold'), bd=10, command=lambda: btnClick("-"))
button.place(relwidth=0.058, relx=0.84, rely=0.4, relheight=0.15)

button = Button(frame, bg='grey', fg='black', text='x', font=('arial',20, 'bold'), bd=10, command=lambda: btnClick("*"))
button.place(relwidth=0.058, relx=0.84, rely=0.56, relheight=0.15)

button = Button(frame, bg='grey', fg='black', text='/', font=('arial',20, 'bold'), bd=10, command=lambda: btnClick("/"))
button.place(relwidth=0.058, relx=0.84, rely=0.72, relheight=0.15)

# finisher: 

root.mainloop()