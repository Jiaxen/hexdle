import tkinter
from tkinter import *
from tkinter import ttk
import hexdle


def App():
    current_hexdle = hexdle.Hexdle()
    ans_colour = current_hexdle.answer_hex()

    window = Tk()
    window.title('Hexdle')

    def submit_guess():
        guess_entry = guess_text.get()
        try:
            warning['text'] = ''
            results = current_hexdle.guess_hex(guess_entry)
            guess_results.insert(END, '\n')
            for i, guess_char in enumerate(guess_entry):
                guess_results.insert(END, guess_char, results[i])
            guess_color_box['background'] = '#' + guess_entry
        except ValueError:
            warning['text'] = 'Not a valid colour'

    # Set up the window
    window.minsize(width=200, height=400)
    mainframe = ttk.Frame(window)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    padding_left = ttk.Label(width=10)
    padding_left.grid(column=0)
    padding_right = ttk.Label(width=10)
    padding_right.grid(column=3)
    padding_top = ttk.Label(width=10)
    padding_top.grid(row=0)
    padding_bottom = ttk.Label(width=10)
    padding_bottom.grid(row=15)

    # Set up titles and ui
    label = ttk.Label(text="Welcome to Hexdle", font=('Arial', 24, 'bold'))
    label.grid(column=1, row=0)
    label_color = ttk.Label(text='Today\'s colour:', font=('Arial', 18))
    label_color.grid(column=1, row=1)
    color_box = ttk.Label(width=100, background=ans_colour)
    color_box.grid(column=2, row=1)
    label_color = ttk.Label(text='Last guess:', font=('Arial', 18))
    label_color.grid(column=1, row=2)
    guess_color_box = ttk.Label(width=100, background='#FFFFFF')
    guess_color_box.grid(column=2, row=2)
    label_color = ttk.Label(text='Next guess:', font=('Arial', 18))
    label_color.grid(column=1, row=3)
    guess_text = StringVar()
    guess = ttk.Entry(textvariable=guess_text)
    guess.grid(column=2, row=3, sticky=W)
    enter_button = ttk.Button(text='Submit', command=submit_guess)
    enter_button.grid(column=2, row=4, sticky=W)
    warning = ttk.Label(text='', font=('Arial', 18), foreground='#FF1111')
    warning.grid(column=2, row=5)

    guess_results = tkinter.Text(window)
    guess_results.tag_configure("red", background="red")
    guess_results.tag_configure("green", background="green")
    guess_results.tag_configure("yellow", background="yellow")
    guess_results.grid(column=2, row=6)

    window.mainloop()


if __name__ == '__main__':
    App()
