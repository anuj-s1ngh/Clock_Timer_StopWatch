from tkinter import *
import datetime as dt
from btn_classes import Timer_Btn, StopWatch_Btn


btn_color = "#152D35"
content_color = "#112031"
bg_color = "#D4ECDD"


def clear_all_frames(window):
    for child in window.winfo_children():
        if child.winfo_class() == "Frame":
            child.destroy()
        elif child.winfo_class() == "Button":
            if child["text"] not in ["Clock", "Timer", "Stop Watch"]:
                child.destroy()


def frames_exist(window):
    for child in window.winfo_children():
        if child.winfo_class() == "Frame":
            return True
    return False


def show_clock(window):
    if frames_exist(window):
        clear_all_frames(window)
    
    frame = Frame(
        window,
        bg=bg_color
    )
    frame.grid(
        row=1,
        column=0,
        columnspan=3,
        sticky="nsew"
    )

    def update_date():
        date_str = dt.datetime.now().strftime("%a, %d %b %Y")
        date_label_var.set(date_str)
        date_label.after(1 * 1000, update_date)
    
    def update_time():
        time_str = dt.datetime.now().strftime("%I:%M:%S %p")
        time_label_var.set(time_str)
        time_label.after(1 * 1000, update_time)

    date_label_var = StringVar()
    date_label_var.set(dt.datetime.now().strftime("%a, %d %b %Y"))
    date_label = Label(
        frame,
        textvariable=date_label_var,
        font=("helvetica", 28),
        bg=bg_color,
        fg=content_color,
        padx=20,
    )
    date_label.grid(
        row=0,
        column=0,
        pady=(20, 0)
    )

    time_label_var = StringVar()
    time_label_var.set(dt.datetime.now().strftime("%I:%M:%S %p"))
    time_label = Label(
        frame,
        textvariable=time_label_var,
        font=("helvetica", 48),
        bg=bg_color,
        fg=content_color,
        padx=20,
    )
    time_label.grid(
        row=1,
        column=0,
        pady=(0, 20)
    )

    date_label.after(1 * 1000, update_date)
    time_label.after(1 * 1000, update_time)


def show_timer(window, i=None, add_timer_btn=None):
    if frames_exist(window) and (i is None):
        clear_all_frames(window)
    
    if i is None:
        i = 1
    if add_timer_btn is not None:
        add_timer_btn.destroy()
    frame = Frame(window, bg=bg_color)
    frame.grid(row=i, column=0, columnspan=3, sticky="nsew")

    timer_btn = Timer_Btn(frame)

    add_timer_frame_btn = Button(window, text="Add Another Timer", fg="#ffffff", bg=btn_color, command=lambda: show_timer(window, i+1, add_timer_frame_btn))
    add_timer_frame_btn.grid(row=i+1, column=0, columnspan=3, pady=(10, 20))
    

def show_stopwatch(window, i=None, add_stopwatch_btn=None):
    if frames_exist(window) and (i is None):
        clear_all_frames(window)
    
    if i is None:
        i = 1
    if add_stopwatch_btn is not None:
        add_stopwatch_btn.destroy()
    frame = Frame(window, bg=bg_color)
    frame.grid(row=i, column=0, columnspan=3, sticky="nsew")

    stopwatch_btn = StopWatch_Btn(frame)

    add_stopwatch_frame_btn = Button(window, text="Add Another StopWatch", fg="#ffffff", bg=btn_color, command=lambda: show_stopwatch(window, i+1, add_stopwatch_frame_btn))
    add_stopwatch_frame_btn.grid(row=i+1, column=0, columnspan=3, pady=(10, 20))
    