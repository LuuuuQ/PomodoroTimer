import customtkinter
import pygame
from PIL import Image
from countdown import Countdown

FONT = "Roboto"
SOUND_CLICK = "assets/sounds/click.mp3"
SOUND_BREAK = "assets/sounds/break.mp3"
SOUND_RESET = "assets/sounds/reset.mp3"
SOUND_ERROR = "assets/sounds/error.mp3"


class PomodoroTimerWindow:
    def __init__(self):

        self.work_times = 0
        self.checkmark_labels = []
        self.relx = 0.2

        self.starting_work_minutes = None
        self.starting_work_seconds = None
        self.starting_break_minutes = None
        self.starting_break_seconds = None

        self.timer_is_on = False
        self.pauza = False

        self.window = customtkinter.CTk()
        self.window.title("Pomodoro Timer")
        self.window.minsize(width=500, height=450)

        self.apperance = customtkinter.set_appearance_mode("dark")
        self.color_scheem = customtkinter.set_default_color_theme("blue")

        self.frame = customtkinter.CTkFrame(master=self.window)
        self.frame.pack(padx=25, pady=25, fill="both", expand=True)

        self.second_frame = customtkinter.CTkFrame(master=self.frame, width=250, height=100)
        self.second_frame.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

        # Work/Break label
        self.work_break_label = customtkinter.CTkLabel(master=self.frame, text="Choose your timer",
                                                       font=(FONT, 35, "bold"))
        self.work_break_label.place(relx=0.5, rely=0.06, anchor=customtkinter.CENTER)

        # Hours entry
        self.minutes = customtkinter.CTkEntry(master=self.frame,
                                              width=120,
                                              justify=customtkinter.CENTER,
                                              placeholder_text="25",
                                              font=(FONT, 30, "bold"))
        self.minutes.insert(customtkinter.END, string="25")
        self.minutes.place(relx=0.30, rely=0.59, anchor=customtkinter.CENTER)

        # Colon label
        self.colon_label = customtkinter.CTkLabel(master=self.frame, text=":", font=(FONT, 30, "bold"))
        self.colon_label.place(relx=0.50, rely=0.59, anchor=customtkinter.CENTER)

        # Minutes entry
        self.seconds = customtkinter.CTkEntry(master=self.frame,
                                              width=120,
                                              justify=customtkinter.CENTER,
                                              font=(FONT, 30, "bold"))
        self.seconds.insert(customtkinter.END, string="00")
        self.seconds.place(relx=0.70, rely=0.59, anchor=customtkinter.CENTER)

        # Start_pauza button
        self.start_button = customtkinter.CTkButton(master=self.frame,
                                                    text="Start",
                                                    width=130,
                                                    height=45,
                                                    border_color="#606060",
                                                    border_width=2,
                                                    font=(FONT, 30, "bold"),
                                                    command=self.start_button)
        self.start_button.place(relx=0.5, rely=0.85, anchor=customtkinter.CENTER)

        # Progress_bar
        self.progress_bar = customtkinter.CTkProgressBar(master=self.frame, height=300, orientation="vertical",)
        self.progress_bar.place(relx=0.92, rely=0.5, anchor=customtkinter.CENTER)

        self.countdown = Countdown(self.window, self.minutes, self.seconds, self.progress_bar, self.timer_finished,
                                   self.pauza)

    @staticmethod
    def play_sound(sound_path):
        pygame.mixer.init()
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()

    def start_button(self):
        try:
            minutes = int(self.minutes.get())
            seconds = int(self.seconds.get())

            if minutes == 0 and seconds == 0:
                raise ValueError("Invalid time: Both minutes and seconds cannot be 0.")

            if self.timer_is_on:
                self.countdown.set_time(minutes, seconds)
                self.timer_is_on = False
                self.pauza = True
                self.countdown.pauza = self.pauza
                self.play_sound(SOUND_BREAK)
                self.start_button.configure(text="Start")
                self.next_track_icon_button.destroy()
                self.work_break_manager()
                self.seconds.configure(takefocus=True)
            else:
                self.pauza = False
                self.countdown.set_time(minutes, seconds)
                self.timer_is_on = True
                self.countdown.pauza = self.pauza
                self.start_button.configure(text="Pause")
                self.get_starting_time()
                self.play_sound(SOUND_CLICK)
                self.countdown.timer()
                self.create_next_track_button()
                self.work_break_manager()

        except ValueError:
            self.play_sound(SOUND_ERROR)
            return

    def timer_finished(self):
        self.timer_is_on = False
        self.start_button.configure(text="Start")
        self.pauza = False
        self.countdown.pauza = self.pauza
        self.work_break_label.configure(text="Choose your timer")
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
            self.next_track_icon_button = customtkinter.CTkButton(master=self.frame, text="⏭️",
                                                                  command=self.skip_button,
                                                                  width=45,
                                                                  height=45,
                                                                  fg_color="transparent",
                                                                  hover_color="#606060",
                                                                  font=(FONT, 35))
            self.next_track_icon_button.place(relx=0.8, rely=0.85, anchor=customtkinter.CENTER)

    def run(self):
        self.window.mainloop()

    def checkmark_manager(self):
        if self.work_times >= 9:
            self.work_times = 0
            self.relx = 0.2

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
        label = customtkinter.CTkLabel(master=self.second_frame, text="✔", font=(FONT, 30, "bold"))
        label.place(relx=self.relx, rely=0.23, anchor=customtkinter.CENTER)
        self.checkmark_labels.append(label)

    def add_hourglass(self):
        label = customtkinter.CTkLabel(master=self.second_frame, text="⌚", font=(FONT, 30, "bold"))
        label.place(relx=self.relx, rely=0.73, anchor=customtkinter.CENTER)
        self.relx += 0.20
        self.checkmark_labels.append(label)

    def work_break_manager(self):
        if len(self.checkmark_labels) % 2 == 0:
            self.work_break_label.configure(text="Work")
            self.change_color_blue()

            if len(self.checkmark_labels) % 2 == 0 and not self.timer_is_on and not self.pauza:
                self.minutes.delete(0, customtkinter.END)
                self.minutes.insert(customtkinter.END, str(self.starting_work_minutes).zfill(2))
                self.seconds.delete(0, customtkinter.END)
                self.seconds.insert(customtkinter.END, str(self.starting_work_seconds).zfill(2))

        elif len(self.checkmark_labels) == 7 and not self.timer_is_on and not self.pauza:
            self.work_break_label.configure(text="Long Break")
            self.change_color_purple()

            if self.starting_break_minutes is not None and self.starting_break_seconds is not None:
                long_break_minutes = self.starting_break_minutes * 3

                self.minutes.delete(0, customtkinter.END)
                self.minutes.insert(customtkinter.END, str(long_break_minutes).zfill(2))

                self.seconds.delete(0, customtkinter.END)
                self.seconds.insert(customtkinter.END, str(self.starting_break_seconds).zfill(2))

        elif len(self.checkmark_labels) % 2 == 1 and not self.timer_is_on and not self.pauza:
            self.work_break_label.configure(text="Break")
            self.change_color_green()

            if self.starting_break_minutes is not None and self.starting_break_seconds is not None:
                self.minutes.delete(0, customtkinter.END)
                self.minutes.insert(customtkinter.END, str(self.starting_break_minutes).zfill(2))

                self.seconds.delete(0, customtkinter.END)
                self.seconds.insert(customtkinter.END, str(self.starting_break_seconds).zfill(2))

    def get_starting_time(self):
        if (len(self.checkmark_labels) == 0 and self.starting_work_minutes
                is None and self.starting_work_seconds is None):
            self.starting_work_minutes = int(self.minutes.get())
            self.starting_work_seconds = int(self.seconds.get())

        elif (len(self.checkmark_labels) == 1 and self.starting_break_minutes
              is None and self.starting_break_seconds is None):
            self.starting_break_minutes = int(self.minutes.get())
            self.starting_break_seconds = int(self.seconds.get())

    def change_color_blue(self):
        self.work_break_label.configure(text_color="#1f6aa5")
        self.start_button.configure(fg_color="#1f6aa5", hover_color="#144870")
        self.progress_bar.configure(progress_color="#1f6aa5")

    def change_color_green(self):
        self.work_break_label.configure(text_color="#2ca474")
        self.start_button.configure(fg_color="#2ca474", hover_color="#106a43")
        self.progress_bar.configure(progress_color="#2ca474")

    def change_color_purple(self):
        self.work_break_label.configure(text_color="#6d2c7e")
        self.start_button.configure(fg_color="#6d2c7e", hover_color="#5d1470")
        self.progress_bar.configure(progress_color="#6d2c7e")

