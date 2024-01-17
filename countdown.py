import time
from tkinter import *


class Countdown:
    def __init__(self, window, minutes_entry, seconds_entry, timer_is_on):
        self.window = window
        self.minutes_entry = minutes_entry
        self.seconds_entry = seconds_entry
        self.timer_is_on = timer_is_on

        self.minutes = int(self.minutes_entry.get())
        self.seconds = int(self.seconds_entry.get())

    def timer(self):
        self.time()

        # Sprawdź, czy mamy jeszcze co odliczać
        if self.seconds > 0 or self.minutes > 0:
            # Zastosuj metody after do opóźnienia wywołania kolejnej iteracji funkcji timer
            self.window.after(1000, self.timer)

    def time(self):
        # Zmniejsz czas odliczania
        if self.seconds > 0:
            self.seconds -= 1
        elif self.minutes > 0:
            self.minutes -= 1
            self.seconds = 59


        # Sformatuj wartości do postaci z dwiema cyframi
        formatted_minutes = str(self.minutes).zfill(2)
        formatted_seconds = str(self.seconds).zfill(2)

        # Aktualizuj wartości Entry
        self.minutes_entry.delete(0, END)
        self.minutes_entry.insert(END, formatted_minutes)

        self.seconds_entry.delete(0, END)
        self.seconds_entry.insert(END, formatted_seconds)
