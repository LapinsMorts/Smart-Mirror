# smartmirror.py
# requirements
# requests, feedparser, traceback, Pillow

from Tkinter import *
import sys

sys.path.insert(0, 'Views/')

from FullscreenWindow import FullscreenWindow

if __name__ == '__main__':
    w = FullscreenWindow()
    w.tk.mainloop()
