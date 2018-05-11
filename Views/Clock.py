from Tkinter import *
from contextlib import contextmanager
from Config import config
import time
import threading
import locale


LOCALE_LOCK = threading.Lock()

@contextmanager
def setlocale(name): #thread proof function to work with locale
    with LOCALE_LOCK:
        saved = locale.setlocale(locale.LC_ALL)
        try:
            yield locale.setlocale(locale.LC_ALL, name)
        finally:
            locale.setlocale(locale.LC_ALL, saved)

class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.setlocale = setlocale
        # initialize time label
        self.time1 = ''
        self.timeLbl = Label(self, font=(config["font_family"], config["xlarge_text_size"]), fg="white", bg="black")
        self.timeLbl.pack(side=TOP, anchor=E)
        # initialize day of week
        self.day_of_week1 = ''
        self.dayOWLbl = Label(self, text=self.day_of_week1, font=(config["font_family"], config["small_text_size"]), fg="white", bg="black")
        self.dayOWLbl.pack(side=TOP, anchor=E, padx=(0, 5))
        # initialize date label
        self.date1 = ''
        self.dateLbl = Label(self, text=self.date1, font=(config["font_family"], config["small_text_size"]), fg="white", bg="black")
        self.dateLbl.pack(side=TOP, anchor=E, padx=(0, 5))
        self.tick()

    def tick(self):
        with self.setlocale(config["ui_locale"]):
            if config["time_format"] == 12:
                time2 = time.strftime('%I:%M %p') #hour in 12h format
            else:
                time2 = time.strftime('%H:%M') #hour in 24h format

            day_of_week2 = time.strftime('%A')
            date2 = time.strftime(config["date_format"])
            # if time string has changed, update it
            if time2 != self.time1:
                self.time1 = time2
                self.timeLbl.config(text=time2)
            if day_of_week2 != self.day_of_week1:
                self.day_of_week1 = day_of_week2
                self.dayOWLbl.config(text=day_of_week2)
            if date2 != self.date1:
                self.date1 = date2
                self.dateLbl.config(text=date2)
            # calls itself every 200 milliseconds
            # to update the time display as needed
            # could use >200 ms, but display gets jerky
            self.timeLbl.after(200, self.tick)
