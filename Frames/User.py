import tkinter as tk
from tkinter import ttk
from collections import deque
from turtle import back


class UserFrame(ttk.Frame):
    def __init__(self, frame, container, controller, showframe):
        super().__init__(container)

        self["style"] = "Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.controller = controller
        self.current_timer = tk.StringVar(value=f"{controller.pomodoro.get()}:{controller.pomodoroSec.get()}")
        self.timer_running = False
        self._job_decreament_state = None
        self.timer_label = tk.StringVar(value = self.controller.current_schedule[0])


        timer_description = ttk.Label(
            self,
            textvariable=self.timer_label,
            style='LightText.TLabel'
        )
        timer_description.grid(row=0, column=0, pady=(0, 10), sticky='W')
        timer_description.config(font=10)

        counter_frame = ttk.Frame(self, height=100, style='Timer.TFrame')
        counter_frame.grid(row=1, column=0, columnspan=2, pady=(20, 10))
        label = ttk.Label(
            counter_frame,
            textvariable=self.current_timer,
            style='TimerText.TLabel'
        )
        label.grid()

        button_frame = ttk.Frame(self, padding=30, style='Background.TFrame')
        button_frame.grid(row=2, column=0, columnspan=2)
        button_frame.columnconfigure((0, 1, 2), weight=1)

        self.start_button = ttk.Button(
            button_frame,
            text='Start',
            cursor='hand2',
            command=self.start_count,
            style='PomodoroButton.TButton'
        )
        self.start_button.grid(row=0, column=0, sticky='EW', padx=15)

        self.stop_button = ttk.Button(
            button_frame,
            text='Stop',
            state='disabled',
            cursor='hand2',
            command=self.stop_count,
            style='PomodoroButton.TButton'

        )
        self.stop_button.grid(row=0, column=1, sticky='EW')

        self.reset_button = ttk.Button(
            button_frame,
            text='Reset',
            command=self.reset_count,
            cursor='hand2',
            state='enabled',
            style='PomodoroButton.TButton'

        )
        self.reset_button.grid(row=0, column=2, sticky='EW', padx=15)

        setting_button = ttk.Button(
            self,
            text='Setting',
            cursor='hand2',
            command=showframe,
            style='PomodoroButton.TButton'

        )
        setting_button.grid(row=0, column=1, sticky='NSEW', padx=(0,10), pady=(5,0))
        
        back_button = ttk.Button(
            self,
            text='<-Back',
            cursor='hand2',
            command=lambda: self.back(controller, frame),
            style = 'PomodoroButton.TButton'
        )
        back_button.grid(row=3, column=0, columnspan=3, sticky='NSEW', padx=(5,5), pady=(5,5))

    def back(self, controller, frame):
        controller.show_frame(frame)

    def decrease_counter(self):
        current_time = self.current_timer.get()

        if self.timer_running and current_time != '00:00':
            min, sec = current_time.split(':')
            if int(sec) > 0:
                sec = int(sec) - 1
                min = int(min)
            else:
                sec = 59
                min = int(min) - 1

            self.current_timer.set(f"{min:02d}:{sec:02d}")
            self._job_decreament_state = self.after(1000, self.decrease_counter)

        elif self.timer_running and current_time == '00:00':
            self.controller.current_schedule.rotate(-1)
            next_timer = self.controller.current_schedule[0]
            self.timer_label.set(next_timer)

            if next_timer == 'pomodoro':
                self.current_timer.set(f"{self.controller.pomodoro.get()}:{self.controller.pomodoroSec.get()}")
            elif next_timer == 'short break':
                self.current_timer.set(f"{self.controller.shortbreak.get()}:{self.controller.shortbreakSec.get()}")
            else:
                self.current_timer.set(f"{self.controller.longbreak.get()}:{self.controller.longbreakSec.get()}")

            self.after(1000, self.decrease_counter)

    def start_count(self):
        self.timer_running = True
        self.start_button['state'] = 'disabled'
        self.stop_button['state'] = 'enabled'
        self.decrease_counter()

    def stop_count(self):
        self.timer_running = False
        self.start_button['state'] = 'enabled'
        self.stop_button['state'] = 'disabled'
        if self._job_decreament_state:
            self.after_cancel(self._job_decreament_state)
            self._job_decreament_state = None

    def reset_count(self):
        self.stop_count()
        self.current_timer.set(f"{self.controller.pomodoro.get()}:{self.controller.pomodoroSec.get()}")
        self.controller.current_schedule = deque(self.controller.schedule_timer)
        self.timer_label.set(self.controller.current_schedule[0])
