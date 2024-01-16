from tkinter import *

rely = 0.23


class PomodoroTimerWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Pomodoro Timer ")
        self.window.minsize(width=500, height=450)

        # Work/Break label
        self.work_break_label = Label(text="Work/Break", fg="#000000", font=("Arial", 30, "bold"))
        self.work_break_label.place(relx=0.5, rely=0.07, anchor=CENTER)

        # Tomato image
        self.tomato_canvas = Canvas(width=200, height=224, borderwidth=0, highlightthickness=0, )
        self.tomato_image = PhotoImage(file="assets/images/tomato.png")
        self.tomato_canvas.create_image(100, 113, image=self.tomato_image)
        self.tomato_canvas.place(relx=0.5, rely=0.45, anchor=CENTER)

        # Hours entry
        self.hours_entry = Entry(master=self.tomato_canvas, width=2, borderwidth=0, fg="#FFFFFF", bg="#F26849",
                                 font=("Arial", 30, "bold"))
        self.hours_entry.insert(END, string="15")
        self.hours_entry.place(relx=0.36, rely=0.57, anchor=CENTER)

        # Colon label
        self.colon_label = Label(master=self.tomato_canvas, text=":", fg="#FFFFFF", bg="#F26849",
                                 font=("Arial", 30, "bold"))
        self.colon_label.place(relx=0.51, rely=0.57, anchor=CENTER)

        # Minutes entry
        self.minutes_entry = Entry(master=self.tomato_canvas, width=2, borderwidth=0, fg="#FFFFFF", bg="#F26849",
                                   font=("Arial", 30, "bold"))
        self.minutes_entry.insert(END, string="00")
        self.minutes_entry.place(relx=0.66, rely=0.57, anchor=CENTER)

        # Next track icon
        self.next_track_icon = PhotoImage(file="assets/images/next_track_icon.png")
        self.next_track_icon = self.next_track_icon.subsample(4, 4)
        self.next_track_icon_button = Button(self.window, image=self.next_track_icon, bd=0)
        self.next_track_icon_button.place(relx=0.85, rely=0.51, anchor=CENTER)

        # Start_pauza button
        self.start_button = Button(text="Start", font=("Arial", 20, "bold"))
        self.start_button.place(relx=0.5, rely=0.85, anchor=CENTER)

    def run(self):
        self.window.mainloop()

    def add_checkmark(self):
        pass

    def add_hourglass(self):
        pass

        # for mark in range(4):
        #     Label(text="✔", fg="#16C60C", font=(FONT, 30, "bold")).place(relx=0.10, rely=rely, anchor=CENTER)
        #     Label(text="⌛", fg="#ff0000", font=(FONT, 30, "bold")).place(relx=0.20, rely=rely, anchor=CENTER)
