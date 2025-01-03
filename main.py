"""

Portfolio: LongWrite
#100DaysOfCode with Python
Day: 89
Date: 2023-07-21
Author: MC

as in the example: https://www.squibler.io/dangerous-writing-prompt-app/write?limit=5&type=minutes

"""


from tkinter import *
from time import strftime, gmtime
from tkinter.messagebox import showinfo
from tkinter import filedialog


# ---------------------------- constance ------------------------------------ #
FONT_48 = ("NewYork", 48)
FONT_36 = ("NewYork", 36)
FONT_32 = ("NewYork", 32)
FONT_24 = ("NewYork", 24)
FONT_20 = ("NewYork", 20)
FONT_16 = ("NewYork", 16)

is_start_typing = False

is_long_timer_start = False
is_short_timer_start = False

my_timer = None

long_time_set = 60
short_time_set = 5

long_timer_curr_state = long_time_set
short_timer_curr_state = short_time_set

# ---------------------------- some func ------------------------------------ #


def text_input_key_enter(event):
    # key enter event

    global is_start_typing
    global is_long_timer_start
    global is_short_timer_start

    if is_start_typing is True and is_long_timer_start is True:
        reset_short_timer()

    if is_start_typing is False:
        is_start_typing = True
        is_long_timer_start = True
        is_short_timer_start = True

        start_timers()

    # start_short_timer(short_time_set)
    #
    # if is_start_typing is False:
    #     is_start_typing = True
    #     start_long_timer(long_time_set)


def refresh_timers(
        long_timer_state,
        short_timer_state
):
    # refresh timers func

    global long_timer_curr_state
    global short_timer_curr_state
    global my_timer
    global is_long_timer_start

    time_format = '%M:%S'

    long_time_clock.config(
        text=strftime(
            time_format,
            gmtime(long_timer_curr_state)
        )
    )

    short_time_clock.config(
        text=strftime(
            time_format,
            gmtime(short_timer_curr_state)
        )
    )

    if short_timer_curr_state <= 0:
        # cleaning text box
        clear_text()
        short_timer_curr_state = short_time_set

    if long_timer_curr_state <= 0:
        # active save btn
        save_btn_activator()
        is_long_timer_start = False

    if long_timer_curr_state > 0:

        long_timer_curr_state -= 1
        short_timer_curr_state -= 1
        print(f"{short_timer_curr_state}")

        my_timer = window.after(
            1000,
            refresh_timers,
            long_timer_curr_state,
            short_timer_curr_state
            # long_timer_curr_state - 0.001,
            # short_timer_curr_state - 0.001
        )


def start_timers():

    refresh_timers(
        long_timer_curr_state,
        short_timer_curr_state
    )


def reset_short_timer():
    # reset short timer current state -> to test
    global is_short_timer_start
    global short_timer_curr_state

    if is_short_timer_start is True:
        short_timer_curr_state = short_time_set


def save_btn_activator():
    # make save btn active
    save_btn.config(
        state='active'
    )


def clear_text():
    """
    clear text input field
    """
    text_input.delete("1.0", END)


def save_work():
    """
    save work :)
    """

    if len(text_input.get('1.0', END)) > 0:

        filetype = (
            ('txt file', '*.txt'),
        )

        try:
            file = filedialog.asksaveasfile(filetypes=filetype)

            if file is None:
                raise ValueError("The file name must be set")

            showinfo(
                title="Info",
                message="Your work was saved correctly ;)"
            )

            with open(file.name, 'w') as f:
                f.writelines(text_input.get('1.0', END))

        except Exception as e:
            showinfo(
                title="Error",
                message=e.__str__()
            )

        # print(text_input.get('1.0', END))


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

# text
v = Scrollbar(
    window,
    orient='vertical'
)

text_input = Text(
    window,
    yscrollcommand=v.set,
    font=FONT_20
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
    command=save_work,
    state='disabled',
)
save_btn.grid(
    row=3,
    column=1
)


# ---------------------------- start window ------------------------------------ #

# on key event
text_input.bind("<Key>", text_input_key_enter)

window.mainloop()
