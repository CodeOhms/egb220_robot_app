import tkinter as tk
from tkinter import ttk

class View_Main:
    def __init__(self, frame):
        self.frame_main = frame

        # Have main frame take up all the room in root window:
        self.frame_main.pack()