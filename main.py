"""

Portfolio: LongWrite
#100DaysOfCode with Python
Day: 89
Date: 2023-07-21
Author: MC

"""


from tkinter import *
from time import strftime, gmtime
from tkinter.messagebox import showinfo


# ---------------------------- constance ------------------------------------ #
FONT_48 = ("NewYork", 48)
FONT_36 = ("NewYork", 36)
FONT_32 = ("NewYork", 32)
FONT_24 = ("NewYork", 24)
FONT_20 = ("NewYork", 20)
FONT_16 = ("NewYork", 16)

# ---------------------------- some func ------------------------------------ #


def clear_text():
    text_input.delete('0', END)


def save_work():
    # todo: some functionality
    pass


# ---------------------------- UI ------------------------------------ #

# window ini
window = Tk()
window.title("Long Write Project by MC")
window.config(
    padx=50,
    pady=25,
    bg="#323232"
)
window.minsize(
    width=800,
    height=600
)

# some controls
long_time_text_label = Label(
    text="Long time",
    font=FONT_20,
    fg="white",
    pady=15,
)
long_time_text_label.grid(
    row=0,
    column=0
)

long_time_clock = Label(
    text="00:00",
    font=FONT_24,
    fg='white',
    pady=15
)
long_time_clock.grid(
    row=1,
    column=0
)

short_time_text_label = Label(
    text="Short time",
    font=FONT_20,
    fg='white',
    pady=15
)
short_time_text_label.grid(
    row=0,
    column=1
)

short_time_clock = Label(
    text="00:00",
    font=FONT_24,
    fg='red',
    pady=15
)
short_time_clock.grid(
    row=1,
    column=1
)

v = Scrollbar(
    window,
    orient='vertical'
)

# text
text_input = Text(
    window,
    yscrollcommand=v.set
)
text_input.grid(
    row=2,
    columnspan=2
)

# some buttons

# clear button
clear_btn = Button(
    text="Clear text",
    highlightthickness=0,
    command=clear_text
)
clear_btn.grid(
    row=3,
    column=0
)

# save button
save_btn = Button(
    text="Save work",
    highlightthickness=0,
    command=save_work
)
save_btn.grid(
    row=3,
    column=1
)


# ---------------------------- start window ------------------------------------ #

# on key event

window.mainloop()
