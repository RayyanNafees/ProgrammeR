
from tkinter import *
win = Tk()

total_frames = 3
for num in range(1, total_frames+1):
	exec(f'frame{num} = Frame(win)')
	
strv = StringVar()
intv = IntVar()

label = Label(frame1, text='Enter the  : ')
enter = Entry(frame1, width = 10)

def func():
	pass
	
exec(f'lastframe = frame{total_frames}')

dobtn = Button(lastframe, text = 'Do',command = func)

quit = Button(lastframe, text= 'Cancel',command = win.destroy)

label.pack(side='left')
enter.pack(side='left')
dobtn.pack(side = 'left')
quit.pack(side = 'left')

for i in range(1, total_frames+1):
	exec(f'frame{i}.pack()')

mainloop()