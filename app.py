
from windows import set_process_dpi
import tkinter as tk
from tkinter import ttk
from collections import deque
from Frames import UserFrame, Setting

set_process_dpi()

COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"


class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Background.TFrame", background=COLOUR_PRIMARY)
        style.configure("Timer.TFrame", background=COLOUR_LIGHT_BACKGROUND)
        style.configure(
            "TimerText.TLabel",
            background=COLOUR_LIGHT_BACKGROUND,
            foreground=COLOUR_DARK_TEXT,
            font='Courier 38'
        )

        style.configure(
            "LightText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
            font='TkDefaultFont 11'
        )

        style.configure(
            "PomodoroButton.TButton",
            background=COLOUR_SECONDARY,
            foreground=COLOUR_LIGHT_TEXT,
        )

        style.map(
            "PomodoroButton.TButton",
            background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)]
        )

        self["background"] = COLOUR_PRIMARY

        self.title('Pomodoro Timer')
        container = ttk.Frame(self, padding=(30, 15))
        container.grid(sticky='NSEW')
        container.columnconfigure(0, weight=1)

        self.frames = dict()

        self.pomodoro = tk.StringVar(value='20')
        self.pomodoroSec = tk.StringVar(value='00')
        self.shortbreak = tk.StringVar(value='05')
        self.shortbreakSec = tk.StringVar(value='00')
        self.longbreak = tk.StringVar(value='15')
        self.longbreakSec = tk.StringVar(value='00')

        self.schedule_timer = ['pomodoro', 'short break', 'pomodoro', 'long break', 'short break']
        self.current_schedule = deque(self.schedule_timer)

        frame_1 = UserFrame(container, self, lambda: self.show_frame(Setting))
        self.frames[UserFrame] = frame_1
        frame_2 = Setting(container, self, lambda: self.show_frame(UserFrame))
        self.frames[Setting] = frame_2
        frame_1.grid(row=0, column=0, sticky='NSEW')
        frame_2.grid(row=0, column=0, sticky='NSEW')

        frame_1.tkraise()

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


root = PomodoroTimer()
root.mainloop()
