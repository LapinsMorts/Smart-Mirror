from Tkinter import *
from Config import config


class CalendarEvent(Frame):
    def __init__(self, parent, event_name="Event 1"):
        Frame.__init__(self, parent, bg='black')
        self.eventName = event_name
        self.eventNameLbl = Label(self, text=self.eventName, font=(config["font_family"], config["small_text_size"]), fg="white", bg="black")
        self.eventNameLbl.pack(side=TOP, anchor=E)
