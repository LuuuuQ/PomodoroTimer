from tkinter import *
from countdown import Countdown
import pygame

FONT = "Roboto"
SOUND_CLICK = "assets/sounds/click.mp3"
SOUND_BREAK = "assets/sounds/break.mp3"
SOUND_RESET = "assets/sounds/reset.mp3"


class PomodoroTimerWindow:
    def __init__(self):

        self.work_times = 0
        self.checkmark_labels = []
        self.rely = 0.23

        self.starting_work_minutes = None
        self.starting_work_seconds = None
        self.starting_break_minutes = None
        self.starting_break_seconds = None

        self.timer_is_on = False
        self.pauza = False

        self.window = Tk()
        self.window.title("Pomodoro Timer ")
        self.window.minsize(width=500, height=450)

        # Work/Break label
        self.work_break_label = Label(text="Choose your timer", fg="#000000", font=(FONT, 30, "bold"))
        self.work_break_label.place(relx=0.5, rely=0.07, anchor=CENTER)

        # Tomato image
        self.tomato_canvas = Canvas(width=200, height=224, borderwidth=0, highlightthickness=0)
        self.tomato_image = PhotoImage(file="assets/images/tomato.png")
        self.tomato_canvas.create_image(100, 113, image=self.tomato_image)
        self.tomato_canvas.place(relx=0.5, rely=0.45, anchor=CENTER)

        # Hours entry
        self.minutes = Entry(master=self.tomato_canvas, width=2, borderwidth=0, fg="#FFFFFF", bg="#F26849",
                             font=(FONT, 30, "bold"))
        self.minutes.insert(END, string="00")
        self.minutes.place(relx=0.36, rely=0.57, anchor=CENTER)

        # Colon label
        self.colon_label = Label(master=self.tomato_canvas, text=":", fg="#FFFFFF", bg="#F26849",
                                 font=(FONT, 30, "bold"))
        self.colon_label.place(relx=0.51, rely=0.57, anchor=CENTER)

        # Minutes entry
        self.seconds = Entry(master=self.tomato_canvas, width=2, borderwidth=0, fg="#FFFFFF", bg="#F26849",
                             font=(FONT, 30, "bold"))
        self.seconds.insert(END, string="10")
        self.seconds.place(relx=0.66, rely=0.57, anchor=CENTER)

        # Start_pauza button
        self.start_button = Button(text="Start", font=(FONT, 20, "bold"),
                                   command=self.start_button)
        self.start_button.place(relx=0.5, rely=0.85, anchor=CENTER)

        self.countdown = Countdown(self.window, self.minutes, self.seconds, self.timer_finished, self.pauza)

    @staticmethod
    def play_sound(sound_path):
        pygame.mixer.init()
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()

    def start_button(self):
        if self.timer_is_on:
            self.timer_is_on = False
            self.pauza = True
            self.countdown.pauza = self.pauza
            self.play_sound(SOUND_BREAK)
            self.start_button.configure(text="Start")
            self.next_track_icon_button.destroy()
            self.work_break_manager()

        else:
            self.pauza = False
            self.timer_is_on = True
            self.countdown.pauza = self.pauza
            self.start_button.configure(text="Pauza")
            self.countdown.set_time(int(self.minutes.get()), int(self.seconds.get()))
            self.play_sound(SOUND_CLICK)
            self.get_starting_time()
            self.countdown.timer()
            self.create_next_track_button()
            self.work_break_manager()

    def timer_finished(self):
        self.timer_is_on = False
        self.start_button.configure(text="Start")
        self.pauza = False
        self.countdown.pauza = self.pauza
        self.work_break_label.config(text="Choose your timer")
        self.next_track_icon_button.destroy()
        self.play_sound(SOUND_RESET)
        self.work_times += 1
        self.checkmark_manager()
        self.work_break_manager()

    def skip_button(self):
        self.countdown.update_timer_time()
        self.countdown.set_time(0, 0)
        self.timer_is_on = False
        self.pauza = False
        self.countdown.pauza = self.pauza
        self.next_track_icon_button.destroy()

    def create_next_track_button(self):
        if self.timer_is_on:
            self.next_track_icon = PhotoImage(file="assets/images/next_track_icon.png")
            self.next_track_icon = self.next_track_icon.subsample(4, 4)
            self.next_track_icon_button = Button(self.window, image=self.next_track_icon, bd=0,
                                                 command=self.skip_button)
            self.next_track_icon_button.place(relx=0.85, rely=0.51, anchor=CENTER)

    def run(self):
        self.window.mainloop()

    def checkmark_manager(self):
        if self.work_times >= 9:
            self.work_times = 0

            self.rely = 0.23
            for label in self.checkmark_labels:
                label.destroy()
            self.checkmark_labels = []
            self.add_check()
            self.work_times += 1


        elif len(self.checkmark_labels) % 2 == 0 and len(self.checkmark_labels) <= self.work_times:
            self.add_check()
        elif len(self.checkmark_labels) % 2 == 1 and len(self.checkmark_labels) <= self.work_times:
            self.add_hourglass()

    def add_check(self):
        label = Label(text="✔", fg="#16C60C", font=(FONT, 30, "bold"))
        label.place(relx=0.10, rely=self.rely, anchor=CENTER)
        self.checkmark_labels.append(label)

    def add_hourglass(self):
        label = Label(text="⌛", fg="#ff0000", font=(FONT, 30, "bold"))
        label.place(relx=0.20, rely=self.rely, anchor=CENTER)
        self.rely += 0.10
        self.checkmark_labels.append(label)

    def work_break_manager(self):
        if len(self.checkmark_labels) % 2 == 0 and not self.timer_is_on and not self.pauza:
            self.work_break_label.config(text="Work")
            # Ustaw wartości w polach Entry
            self.minutes.delete(0, END)
            self.minutes.insert(END, str(self.starting_work_minutes).zfill(2))

            self.seconds.delete(0, END)
            self.seconds.insert(END, str(self.starting_work_seconds).zfill(2))

        elif len(self.checkmark_labels) == 7 and not self.timer_is_on and not self.pauza:
            self.work_break_label.config(text="Long Break")
            if self.starting_break_minutes is not None and self.starting_break_seconds is not None:

                long_break_minutes = self.starting_break_minutes * 3

                self.minutes.delete(0, END)
                self.minutes.insert(END, str(long_break_minutes).zfill(2))

                self.seconds.delete(0, END)
                self.seconds.insert(END, str(self.starting_break_seconds).zfill(2))

        elif len(self.checkmark_labels) % 2 == 1 and not self.timer_is_on and not self.pauza:
            self.work_break_label.config(text="Break")

            if self.starting_break_minutes is not None and self.starting_break_seconds is not None:
                self.minutes.delete(0, END)
                self.minutes.insert(END, str(self.starting_break_minutes).zfill(2))

                self.seconds.delete(0, END)
                self.seconds.insert(END, str(self.starting_break_seconds).zfill(2))

    def get_starting_time(self):
        if (len(self.checkmark_labels) == 0 and self.starting_work_minutes
                is None and self.starting_work_seconds is None):
            self.starting_work_minutes = int(self.minutes.get())
            self.starting_work_seconds = int(self.seconds.get())

        elif (len(self.checkmark_labels) == 1 and self.starting_break_minutes
              is None and self.starting_break_seconds is None):
            self.starting_break_minutes = int(self.minutes.get())
            self.starting_break_seconds = int(self.seconds.get())
