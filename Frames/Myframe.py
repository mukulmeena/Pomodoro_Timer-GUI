import tkinter as tk
from tkinter import ttk


class MyFrame(ttk.Frame):
    def __init__(self, container, controller, showframe):
        super().__init__(container)

        self['style'] = 'Background.TFrame'

        frame = ttk.Frame(self, style='Background.TFrame', padding=(30, 15, 30, 15))
        frame.grid(row=0, column=0, sticky='NSEW')

        user_timer = ttk.Label(
            frame,
            text='Enter your timer name:',
            style='LightText.TLabel'
        )
        user_timer.grid(row=0, column=0, sticky='W', padx=(0,10))

        user_entry = ttk.Entry(
            frame,
            width=25,
            textvariable=controller.user_timer
        )
        user_entry.grid(row=0, column=1, sticky='W')

        usertimer_label = ttk.Label(
            frame,
            text='Enter the time:',
            style='LightText.TLabel')
        usertimer_label.grid(row=1, column=0, sticky='EW', pady=(0,10))

        usertimer_Entry = tk.Spinbox(
            frame,
            from_=0,
            to=120,
            increment=1,
            justify='center',
            textvariable=controller.pomodoro,
            width=10)
        usertimer_Entry.grid(row=1, column=1, sticky='W')

        usertimerSec_Entry = tk.Spinbox(
            frame,
            from_=0,
            to=60,
            increment=1,
            justify='center',
            textvariable=controller.pomodoroSec,
            width=10)
        usertimerSec_Entry.grid(row=1, column=2, sticky='W')

        submit_label = ttk.Button(
            frame,
            cursor='hand2',
            command=lambda: self.submit(controller, showframe),
            text='Submit'
        )
        submit_label.grid(row=2, column=0, columnspan=3, sticky='EW', pady=(20,0))
        
        for children in frame.winfo_children():
            children.grid_configure(pady=10)
    
    def submit(self, controller, showframe):
        controller.schedule_timer.insert(0, controller.user_timer.get())
        showframe()




