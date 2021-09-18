from tkinter import *
import datetime as dt
import time


content_color = "#112031"
bg_color = "#D4ECDD"
btn_color = "#345B63"


class Timer_Btn(Button):
        def __init__(self, window=None) -> None:
            super().__init__(window)
            self.window = window

            self.timer_running = BooleanVar()
            self.timer_running.set(False)

            self.time_label_var = StringVar()

            self.title_entry_var = StringVar()
            self.title_entry_var.set("Title")
            self.title_entry_label = Label(self.window, text="Title : ", bg=bg_color)
            self.title_entry_label.grid(row=0, column=0, padx=(20, 0), pady=(20, 5))
            self.title_entry = Entry(self.window, textvariable=self.title_entry_var, width=20)
            self.title_entry.grid(row=0, column=1, columnspan=2, padx=(0, 20), pady=(20, 5))

            self.time_entry_var = StringVar()
            self.time_entry_var.set("00:00:00")
            self.time_entry_label = Label(self.window, text="Time : ", bg=bg_color)
            self.time_entry_label.grid(row=1, column=0, padx=(20, 0), pady=(5, 20))
            self.time_entry = Entry(self.window, textvariable=self.time_entry_var, width=20)
            self.time_entry.grid(row=1, column=1, columnspan=2, padx=(0, 20), pady=(5, 20))

            self.show_btns()


        def show_btns(self):
            btn_txt_list = ["Start", "Stop", "Reset", "Delete"]
            btn_func_list = [
                self.start_timer,
                self.stop_timer,
                self.reset_timer,
                self.delete_timer
            ]
            for i in range(0, 4):
                btn = Button(
                    self.window,
                    text=btn_txt_list[i],
                    bg=btn_color,
                    fg="#ffffff",
                    command=btn_func_list[i]
                )
                btn.grid(
                    row=0,
                    column=i+3,
                    rowspan=2,
                    padx=10,
                    pady=20
                )


        def start_timer(self):
            if not bool(self.timer_running.get()):

                self.hour, self.minute, self.second = self.time_entry_var.get().split(":")

                if (int(self.hour) != 0) or (int(self.minute) != 0) or (int(self.second) != 0):
                    time_str = self.hour + ":" + self.minute + ":" + self.second
                    self.time_label_var.set(time_str)

                    self.title_entry_label.destroy()
                    self.title_entry.destroy()
                    self.time_entry_label.destroy()
                    self.time_entry.destroy()

                    self.update_time()
                    
                    self.timer_running.set(True)

                    self.update_time()
                else:
                    help_text = Label(self.window, text="Please Enter A Valid Time Duration", bg=bg_color, fg="#444444")
                    help_text.grid(row=4, column=1, columnspan=3, pady=(0, 10))
                    help_text.after(3 * 1000, help_text.destroy)


        def stop_timer(self):
            if bool(self.timer_running.get()):
                self.timer_running.set(False)


        def reset_timer(self):
            for child in self.window.winfo_children():
                child.destroy()
            self.__init__(window=self.window)


        def delete_timer(self):
            self.window.destroy()


        def update_time(self):
            if bool(self.timer_running.get()):
                if(int(self.minute) == 0) & (int(self.hour) != 0):
                    self.minute = str(60)
                    self.hour = str(int(self.hour) - 1)
                if(int(self.second) == 0) & (int(self.minute) != 0):
                    self.second = str(59)
                    self.minute = str(int(self.minute) - 1)
                

                time_str = self.hour + ":" + self.minute + ":" + self.second
                self.time_label_var.set(time_str)

                self.show_time()

                self.second = str(int(self.second) - 1)

                self.time_label.after(1 * 1000, self.update_time)
            else:
                self.show_time()


        def show_time(self):
            self.title_label = Label(
                self.window,
                textvariable=self.title_entry_var,
                font=("helvetica", 18),
                bg=bg_color,
                fg=content_color,
            )
            self.title_label.grid(
                row=0,
                column=0,
                rowspan=2,
                pady=20,
                padx=(20, 0)
            )

            self.time_label = Label(
                self.window,
                textvariable=self.time_label_var,
                font=("helvetica", 28),
                bg=bg_color,
                fg=content_color,
            )
            self.time_label.grid(
                row=0,
                column=1,
                columnspan=2,
                pady=20,
                padx=(10, 20)
            )



class StopWatch_Btn(Button):
        def __init__(self, window=None) -> None:
            super().__init__(window)
            self.window = window

            self.stopwatch_running = BooleanVar()
            self.stopwatch_running.set(False)

            self.time_label_var = StringVar()
            self.time_label_var.set("00:00:00")

            self.title_entry_var = StringVar()
            self.title_entry_var.set("Title")
            self.title_entry_label = Label(self.window, text="Title : ", bg=bg_color)
            self.title_entry_label.grid(row=0, column=0, padx=(20, 0), pady=20)
            self.title_entry = Entry(self.window, textvariable=self.title_entry_var, width=20)
            self.title_entry.grid(row=0, column=1, columnspan=2, padx=(0, 20), pady=20)

            self.show_btns()


        def show_btns(self):
            btn_txt_list = ["Start", "Stop", "Reset", "Delete"]
            btn_func_list = [
                self.start_stopwatch,
                self.stop_stopwatch,
                self.reset_stopwatch,
                self.delete_stopwatch
            ]
            for i in range(0, 4):
                btn = Button(
                    self.window,
                    text=btn_txt_list[i],
                    bg=btn_color,
                    fg="#ffffff",
                    command=btn_func_list[i]
                )
                btn.grid(
                    row=0,
                    column=i+3,
                    padx=10,
                    pady=20
                )


        def start_stopwatch(self):
            if not bool(self.stopwatch_running.get()):

                self.hour, self.minute, self.second = self.time_label_var.get().split(":")

                time_str = self.hour + ":" + self.minute + ":" + self.second
                self.time_label_var.set(time_str)

                self.title_entry_label.destroy()
                self.title_entry.destroy()

                self.update_time()
                
                self.stopwatch_running.set(True)

                self.update_time()


        def stop_stopwatch(self):
            if bool(self.stopwatch_running.get()):
                self.stopwatch_running.set(False)


        def reset_stopwatch(self):
            for child in self.window.winfo_children():
                child.destroy()
            self.__init__(window=self.window)
        

        def delete_stopwatch(self):
            self.window.destroy()


        def update_time(self):
            if bool(self.stopwatch_running.get()):
                if int(self.minute) == 60:
                    self.minute = str(0)
                    self.hour = str(int(self.hour) + 1)
                if int(self.second) == 60:
                    self.second = str(0)
                    self.minute = str(int(self.minute) + 1)
                

                time_str = self.hour + ":" + self.minute + ":" + self.second
                self.time_label_var.set(time_str)

                self.show_time()

                self.second = str(int(self.second) + 1)

                self.time_label.after(1 * 1000, self.update_time)
            else:
                self.show_time()


        def show_time(self):
            self.title_label = Label(
                self.window,
                textvariable=self.title_entry_var,
                font=("helvetica", 18),
                bg=bg_color,
                fg=content_color,
            )
            self.title_label.grid(
                row=0,
                column=0,
                rowspan=2,
                pady=20,
                padx=(20, 0)
            )

            self.time_label = Label(
                self.window,
                textvariable=self.time_label_var,
                font=("helvetica", 28),
                bg=bg_color,
                fg=content_color,
            )
            self.time_label.grid(
                row=0,
                column=1,
                columnspan=2,
                pady=20,
                padx=(10, 20)
            )

