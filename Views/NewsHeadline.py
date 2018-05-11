from Tkinter import *
from Config import config
from PIL import Image, ImageTk


class NewsHeadline(Frame):
    def __init__(self, parent, event_name=""):
        Frame.__init__(self, parent, bg='black')

        image = Image.open("assets/Newspaper.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        photo = ImageTk.PhotoImage(image)

        self.iconLbl = Label(self, bg='black', image=photo)
        self.iconLbl.image = photo
        self.iconLbl.pack(side=LEFT, anchor=N)

        self.eventName = event_name
        self.eventNameLbl = Label(self, text=self.eventName, font=(config["font_family"], config["small_text_size"]), fg="white", bg="black", wraplength=config["headline_wrap_width"], justify=LEFT)
        self.eventNameLbl.pack(side=LEFT, anchor=N, padx=(10, 0))
