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
FONT_16 = ("NewYork", 16)




# ---------------------------- UI ------------------------------------ #

# window ini
window = Tk()
window.title("Long Write Project by MC")
window.config(
    padx=100,
    pady=50,
    bg="#323232"
)
window.minsize(
    width=800,
    height=600
)

