import tkinter as tk
from tkinter import ttk


class Setting(ttk.Frame):
    def __init__(self, container, controller, showframe):
        super().__init__(container)

        self["style"] = 'Background.TFrame'

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        setting_frame = ttk.Frame(self, style='Background.TFrame', padding=(30,15,30,15))
        setting_frame.grid(row=0, column=0, sticky='EW')
        setting_frame.columnconfigure(0, weight=1)

        pomodoro_label = ttk.Label(
            setting_frame,
            text='Pomodoro:',
            font='TkDefaultFont 11')
        pomodoro_label.grid(row=0, column=0, sticky='EW')

        pomodoro_Entry = tk.Spinbox(
            setting_frame,
            from_=0,
            to=120,
            increment=1,
            justify='center',
            textvariable=controller.pomodoro,
            width=10)
        pomodoro_Entry.grid(row=0, column=1, sticky='W')

        pomodoroSec_Entry = tk.Spinbox(
            setting_frame,
            from_=0,
            to=60,
            increment=1,
            justify='center',
            textvariable=controller.pomodoroSec,
            width=10)
        pomodoroSec_Entry.grid(row=0, column=2, sticky='W')

        shortbreak_label = ttk.Label(
            setting_frame,
            text='Short Break:',
            font='TkDefaultFont 11')
        shortbreak_label.grid(row=1, column=0, sticky='EW')

        shortbreak_entry = tk.Spinbox(
            setting_frame,
            from_=0,
            to=20,
            increment=1,
            justify='center',
            textvariable=controller.shortbreak,
            width=10)
        shortbreak_entry.grid(row=1, column=1, sticky='W')

        shortbreakSec_entry = tk.Spinbox(
            setting_frame,
            from_=0,
            to=60,
            increment=1,
            justify='center',
            textvariable=controller.shortbreakSec,
            width=10)
        shortbreakSec_entry.grid(row=1, column=2, sticky='W')

        longbreak_label = ttk.Label(
            setting_frame,
            text='Long Break:',
            font='TkDefaultFont 11')
        longbreak_label.grid(row=2, column=0, sticky='EW')

        longbreak_entry = tk.Spinbox(
            setting_frame,
            from_=0,
            to=60,
            increment=1,
            justify='center',
            textvariable=controller.longbreak,
            width=10)
        longbreak_entry.grid(row=2, column=1, sticky='W')

        longbreakSec_entry = tk.Spinbox(
            setting_frame,
            from_=0,
            to=60,
            increment=1,
            justify='center',
            textvariable=controller.longbreakSec,
            width=10)
        longbreakSec_entry.grid(row=2, column=2, sticky='W')

        back_button = ttk.Button(
            setting_frame,
            text='<- Back',
            cursor='hand2',
            command=showframe
        )
        back_button.grid(row=3, column=0, columnspan=3, sticky='EW', pady=(10, 0))

        for children in setting_frame.winfo_children():
            children.grid_configure(padx=5, pady=10)
