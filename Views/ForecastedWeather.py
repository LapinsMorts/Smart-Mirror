from Tkinter import *
from Config import config, icon_lookup
from PIL import Image, ImageTk
import json

class ForecastedWeather(Frame):
    def __init__(self, parent, day="", icon="clear-day", min="", max="", *args, **kwargs):
        Frame.__init__(self, parent, bg='black')

        frame = Frame(self, width=130, height=50, background="black")
        frame.pack_propagate(False)
        frame.pack(side=LEFT, anchor=CENTER)
        self.day_of_week = Label(frame, font=(config["font_family"], config["small_text_size"]), fg="white", bg="black")
        self.day_of_week.pack(side=LEFT, anchor=CENTER)
        self.day_of_week.config(text=day)

        self.icon = Label(self, bg="black")
        self.icon.pack(side=LEFT, anchor=N, padx=20)
        image = Image.open(icon_lookup[icon])
        image = image.resize((config["forecast_icone_width"], config["forecast_icone_height"]), Image.ANTIALIAS)
        image = image.convert('RGB')
        photo = ImageTk.PhotoImage(image)
        self.icon.config(image=photo)
        self.icon.image = photo

        frame2 = Frame(self, width=100, height=50, background="black")
        frame2.pack_propagate(False)
        frame2.pack(side=LEFT, anchor=CENTER)
        self.min = Label(frame2, font=(config["font_family"], config["small_text_size"]), fg="white", bg="black")
        self.min.pack(side=LEFT, anchor=CENTER,padx=20)
        self.min.config(text=min)

        frame3 = Frame(self, width=100, height=50, background="black")
        frame3.pack_propagate(False)
        frame3.pack(side=LEFT, anchor=CENTER)
        self.max = Label(frame3, font=(config["font_family"], config["small_text_size"]), fg="white", bg="black")
        self.max.pack(side=LEFT, anchor=CENTER, padx=20)
        self.max.config(text=max)
