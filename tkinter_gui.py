from tkinter import *
from tkinter import ttk
import hexdle

current_hexdle = hexdle.Hexdle()
ans_colour = current_hexdle.answer_hex()

window = Tk()
window.title('Hexdle')

window.minsize(width=500, height=500)
mainframe = ttk.Frame(window, padding=[10,10,10,10])
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

label = ttk.Label(text="Welcome to Hexdle", font=('Arial', 24, 'bold'))
label.grid(column=0, row=0)

label_color = ttk.Label(text='Today\'s colour:', font=('Arial', 18))
label_color.grid(column=0, row=1)

color_box = ttk.Label(width=100, background=ans_colour)
color_box.grid(column=1, row=1)

guess_1_text = StringVar()
guess_1 = ttk.Entry(textvariable=guess_1_text)
guess_1.grid(column=0, row=2)


window.mainloop()
