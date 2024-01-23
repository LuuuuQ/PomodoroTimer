from tkinter import END


class Countdown:
    def __init__(self, window, minutes_entry, seconds_entry, progress_bar, callback, pauza):
        self.window_timer = None

        self.window = window
        self.minutes_entry = minutes_entry
        self.seconds_entry = seconds_entry
        self.progress_bar = progress_bar

        self.minutes = int(self.minutes_entry.get()) if self.minutes_entry.get() else 0
        self.seconds = int(self.seconds_entry.get()) if self.seconds_entry.get() else 0

        self.total_seconds = self.minutes * 60 + self.seconds
        self.remaining_seconds = self.total_seconds

        self.callback = callback
        self.pauza = pauza

    def set_time(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds
        self.total_seconds = self.minutes * 60 + self.seconds
        self.remaining_seconds = self.total_seconds
        self.update_progress_bar()

    def update_timer_time(self):
        if self.window_timer:
            self.window.after_cancel(self.window_timer)
        self.window_timer = self.window.after(10, self.timer)
        self.time()

    def timer(self):
        if not self.pauza:
            self.time()
            self.update_progress_bar()

            if self.remaining_seconds > 0:
                self.window_timer = self.window.after(1000, self.timer)
            else:
                self.callback()
        else:
            return

    def time(self):
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1

            self.minutes = self.remaining_seconds // 60
            self.seconds = self.remaining_seconds % 60

            formatted_minutes = str(self.minutes).zfill(2)
            formatted_seconds = str(self.seconds).zfill(2)

            self.minutes_entry.delete(0, END)
            self.minutes_entry.insert(END, formatted_minutes)

            self.seconds_entry.delete(0, END)
            self.seconds_entry.insert(END, formatted_seconds)

    def update_progress_bar(self):
        try:
            progress_percentage = 1 - (self.remaining_seconds / self.total_seconds)
            self.progress_bar.set(progress_percentage)

        except ZeroDivisionError:
            self.progress_bar.set(100)
            pass
