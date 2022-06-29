from tkinter import *
win = Tk()

total_frames = 3
for num in range(1, total_frames+1):
	exec(f'frame{num} = Frame(win)')
	
strv = StringVar()
intv = IntVar()

label = Label(frame1, text='Enter the  : ',bg="black", fg="white") 
enter = Entry(frame1, width = 10, bg="black", fg="white")

# functions:

def func():
	pass
	
exec(f'lastframe = frame{total_frames}')

# buttons:

dobtn = Button(lastframe, text = 'Do',command = func)

quit = Button(lastframe, text= 'Cancel',command = win.destroy)

# packing:

label.pack(side='left')
enter.pack(side='left')
dobtn.pack(side = 'left')
quit.pack(side = 'left')

for i in range(1, total_frames+1):
	exec(f'frame{i}.pack()')

# looping and error handling:

mainloop()