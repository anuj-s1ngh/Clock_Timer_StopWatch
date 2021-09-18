from tkinter import *
from btn_actions import show_clock, show_timer, show_stopwatch


def show_btns(window):
    # Define Buttons
    btn_color = "#152D35"
    btn_txt_list = ["Clock", "Timer", "Stop Watch"]
    btn_func_list = [
        lambda: show_clock(window),
        lambda: show_timer(window),
        lambda: show_stopwatch(window)
    ]

    for i in range(0, 3):

        clock_btn = Button(
            window,
            text=btn_txt_list[i],
            command=btn_func_list[i],
            font=("Arial", 12, "bold"),
            width=10,
            relief=RAISED,  # [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]
            borderwidth=1,
            fg="#ffffff",
            bg=btn_color
        )
        clock_btn.grid(
            row=0,
            column=i,
            padx=20,
            pady=20,
        )

