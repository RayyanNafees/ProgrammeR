
#* The Setup:

from tkinter import Tk, Frame, Button, Entry, Label, StringVar
from time import asctime
 
HEIGHT = 650
WIDTH = 1300
root = Tk()
# canvas = Canvas(root, height=HEIGHT, width=WIDTH)
# canvas.pack()
root.title("SOMETHING DAMN CRAZY")
i1,i2,i3,i4,i5,i6,i7,i8 = [StringVar() for i in range(8)]
ttl = StringVar()

StringVar = StringVar()
operator=""

#* Event Handlers____________________

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
    
nums= lambda txt: int(''.join( i for i in txt if i.isdigit() or (i=='-' and not txt.index(i)) )) if not txt.isnumeric() else int(txt)
add = lambda: ttl.set(sum(nums(i.get()) for i in (i1,i2,i3,i4,i5,i6,i7,i8)))
reset=lambda: ttl.set(bool([i.set('') for i in (i1,i2,i3,i4,i5,i6,i7,i8)][0]))

    
#* Makeup_____________________________

Label(root, font=('arial',30, 'bold'), text='SOMETHING DAMN CRAZY', fg="steelblue", bd=10, anchor='w').place(relx=0.1)

frame = Frame(root, bg='powderblue')
frame.place(relheight=0.82, relwidth=0.89, relx=0.06, rely=0.08)


#* Time Stamp__________________________

Label(root, fg='steelblue', font=('itlics',20, 'bold'), text=asctime() ).place(relx=0.7, rely=0.02)
 
 
#* Food List___________________________

entstyle = dict(bg='white', font=('arial',20, 'bold'), bd=10, justify='right')
btn = dict(bg='powderblue', font=('arial',20, 'bold'), bd=10, fg='black')

Label(frame, **btn, text='CHICKEN').place(relwidth=0.16, relx=0.03, rely=0.02, relheight=0.1)
Label(frame, **btn, text='FISH')   .place(relwidth=0.16, relx=0.03, rely=0.12, relheight=0.1)
Label(frame, **btn, text='BEEF')   .place(relwidth=0.16, relx=0.03, rely=0.22, relheight=0.1)
Label(frame, **btn, text='PIZZA')  .place(relwidth=0.16, relx=0.03, rely=0.32, relheight=0.1)
Label(frame, **btn, text='J.RICE') .place(relwidth=0.16, relx=0.03, rely=0.42, relheight=0.1)
Label(frame, **btn, text='RICE.S') .place(relwidth=0.16, relx=0.03, rely=0.52, relheight=0.1)
Label(frame, **btn, text='PEPSI')  .place(relwidth=0.16, relx=0.03, rely=0.62, relheight=0.1)
Label(frame, **btn, text='MIRINDA').place(relwidth=0.16, relx=0.03, rely=0.72, relheight=0.1)

Entry(frame, **entstyle, textvariable=i1).place(relwidth=0.2, relx=0.23, rely=0.02, relheight=0.1)
Entry(frame, **entstyle, textvariable=i2).place(relwidth=0.2, relx=0.23, rely=0.12, relheight=0.1)
Entry(frame, **entstyle, textvariable=i3).place(relwidth=0.2, relx=0.23, rely=0.22, relheight=0.1)
Entry(frame, **entstyle, textvariable=i4).place(relwidth=0.2, relx=0.23, rely=0.32, relheight=0.1)
Entry(frame, **entstyle, textvariable=i5).place(relwidth=0.2, relx=0.23, rely=0.42, relheight=0.1)
Entry(frame, **entstyle, textvariable=i6).place(relwidth=0.2, relx=0.23, rely=0.52, relheight=0.1)
Entry(frame, **entstyle, textvariable=i7).place(relwidth=0.2, relx=0.23, rely=0.62, relheight=0.1)
Entry(frame, **entstyle, textvariable=i8).place(relwidth=0.2, relx=0.23, rely=0.72, relheight=0.1)


#* Buttons____________________
btn.update(dict(bg='grey',  fg='black',font=('arial',20,'bold'),  bd=10,))

Button(root, **btn, text='QUIT' , command= root.destroy).place(relwidth=0.16, relx=0.46, rely=0.92, relheight=0.08)

Button(root, **btn, text='RESET', command=reset).place(relwidth=0.16, relx=0.3 , rely=0.92, relheight=0.08)
Button(frame,**btn, text='TOTAL', command= add ).place(relwidth=0.1, relx=0.25, rely=0.85, relheight=0.1)

Entry(frame, bg='white', font=('arial',20, 'bold'),  bd=10, textvariable = ttl ).place(relwidth=0.2, relx=0.38, rely=0.85, relheight=0.1)


#*______________________Calculator_________________________*

entry9 = Entry(frame, font=('arial',20, 'bold'), textvariable=StringVar, bd=30, bg='white', justify='right')
entry9.place(relwidth=0.3, relx=0.6, rely=0.04)

Button(frame, text='1', **btn, command=lambda: btnClick('1')).place(relwidth=0.058, relx=0.6 , rely=0.24, relheight=0.15)
Button(frame, text='4', **btn, command=lambda: btnClick('4')).place(relwidth=0.058, relx=0.6 , rely=0.4 , relheight=0.15)
Button(frame, text='7', **btn, command=lambda: btnClick('7')).place(relwidth=0.058, relx=0.6 , rely=0.56, relheight=0.15)
Button(frame, text='C', **btn, command=btnclearDisplay      ).place(relwidth=0.058, relx=0.6 , rely=0.72, relheight=0.15)
Button(frame, text='2', **btn, command=lambda: btnClick('2')).place(relwidth=0.058, relx=0.68, rely=0.24, relheight=0.15)
Button(frame, text='5', **btn, command=lambda: btnClick('5')).place(relwidth=0.058, relx=0.68, rely=0.4 , relheight=0.15)
Button(frame, text='8', **btn, command=lambda: btnClick('8')).place(relwidth=0.058, relx=0.68, rely=0.56, relheight=0.15)
Button(frame, text='0', **btn, command=lambda: btnClick('0')).place(relwidth=0.058, relx=0.68, rely=0.72, relheight=0.15)
Button(frame, text='3', **btn, command=lambda: btnClick('3')).place(relwidth=0.058, relx=0.76, rely=0.24, relheight=0.15)
Button(frame, text='6', **btn, command=lambda: btnClick('6')).place(relwidth=0.058, relx=0.76, rely=0.4 , relheight=0.15)
Button(frame, text='9', **btn, command=lambda: btnClick('9')).place(relwidth=0.058, relx=0.76, rely=0.56, relheight=0.15)
Button(frame, text='=', **btn, command=btnEquals            ).place(relwidth=0.058, relx=0.76, rely=0.72, relheight=0.15)
Button(frame, text='+', **btn, command=lambda: btnClick("+")).place(relwidth=0.058, relx=0.84, rely=0.24, relheight=0.15)
Button(frame, text='-', **btn, command=lambda: btnClick("-")).place(relwidth=0.058, relx=0.84, rely=0.4 , relheight=0.15)
Button(frame, text='x', **btn, command=lambda: btnClick("*")).place(relwidth=0.058, relx=0.84, rely=0.56, relheight=0.15)
Button(frame, text='/', **btn, command=lambda: btnClick("/")).place(relwidth=0.058, relx=0.84, rely=0.72, relheight=0.15)
 

root.mainloop()