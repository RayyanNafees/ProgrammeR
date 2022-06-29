
from tkinter import *
from tkinter.messagebox import showinfo
from encrypt import *

# setting up:

win = Tk(className = 'Ncrypt')

total_frames = 11

for i in range(1,total_frames +1):      # making frames
    exec(f'frame{str(i)} = Frame(win)')


# Formatting:

label1 = Label(frame1, text = 'Text to Encrypt: \n')
enter_text = Entry(frame1, width = 20)

label2 = Label(frame2, text = 'KEY: ')
enter_key = Entry(frame2, width = 5)

blank = Label(frame3, text = ' ')

label3 = Label(frame4, text = 'Mode of encryption: ')

Ncr = StringVar()
show_text = Entry(frame11, width = 40,textvariable = Ncr)

func_dict = {1: vigenere,
             2: caeser_cipher,
             3: Hash,
             4: morse,
             5: binary}

enc = IntVar()
enc.set(3)

rb1 = Radiobutton(frame5, text = 'vigenere_cipher', variable = enc, value = 1)
rb2 = Radiobutton(frame5, text = 'caeser_cipher', variable = enc, value = 2)
rb3 = Radiobutton(frame6, text = 'Hash', variable = enc, value = 3)
rb4 = Radiobutton(frame6, text = 'morse', variable = enc, value = 4)
rb5 = Radiobutton(frame6, text = 'binary', variable = enc, value = 5)


# Callback functioning:    (event_handlers)

def show():
    text = enter_text.get()
    key = enter_key.get()
    mode = enc.get()

    showinfo('Ncrypt',
             func_dict[mode](text,key))

def ncr():
    text = enter_text.get()
    key = enter_key.get()
    mode = enc.get()

    Ncr.set(func_dict[mode](text,key))

show_btn = Button(frame10, text = 'Show', command = show)
enc_btn = Button(frame10, text = 'Ncrypt', command = ncr)
quit_btn = Button(frame10, text = 'Quit', command = win.destroy)


# Packing:

label1.pack(side = 'left')
label2.pack(side = 'left')
label3.pack(side = 'left')
show_text.pack(side = 'top')
enter_text.pack(side = 'left')
enter_key.pack(side = 'left')
blank.pack(side = 'left')

for i in range(1,6):
    exec(f'rb{str(i)}.pack(side = "left")')

show_btn.pack(side = 'left')
enc_btn.pack(side = 'left')
quit_btn.pack(side = 'left')

for i in range(1,total_frames+1): exec(f'frame{i}.pack()')      # Packing frames

mainloop()
