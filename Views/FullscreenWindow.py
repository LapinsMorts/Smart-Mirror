from Tkinter import *
from Config import config
from Clock import Clock
from Weather import Weather
from News import News
from Calendar import Calendar # Even though it is not used


class FullscreenWindow:
    def __init__(self):
        self.tk = Tk()
        self.tk.configure(background='black')
        self.topFrame = Frame(self.tk, background = 'black')
        self.bottomFrame = Frame(self.tk, background = 'black')
        self.topFrame.pack(side = LEFT, fill=BOTH, expand = YES)
        self.bottomFrame.pack(side = RIGHT, fill=BOTH, expand = YES)
        self.state = False
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        # clock
        self.clock = Clock(self.topFrame)
        self.clock.pack(side=TOP, anchor=NW, padx=100, pady=60)
        # weather
        self.weather = Weather(self.topFrame, self.clock.day_of_week1)
        self.weather.pack(side=TOP, anchor=NW, padx=100, pady=(60, 0))
        # news
        self.news = News(self.bottomFrame)
        self.news.pack(side=RIGHT, anchor=N, padx=100, pady=(80,0))
        # calender - removing for now
        # self.calender = Calendar(self.bottomFrame)
        # self.calender.pack(side = RIGHT, anchor=S, padx=100, pady=60)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"
