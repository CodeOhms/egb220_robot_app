import tkinter as tk
from tkinter import ttk
# User modules
from .view_main import View_Main
from .view_map import View_Map
# from .model_main import Model_Main
from .model_map import Model_Map
from .controller_main import Controller_Main
from .controller_map import Controller_Map

class Gui:
    def __init__(self, tkinter_root):
        self.tk_root = tkinter_root
        self.frame_main = tk.Frame(self.tk_root)
        self.frame_map = tk.Frame(self.frame_main)
        
        # Views:
        self.view_main = View_Main(self.frame_main)
        self.view_map = View_Map(self.frame_map)

        # Models:
        # self.model_main = Model_Main()
        self.model_map = Model_Map()

        # Controllers:
        # self.controller_main = Controller_Main(model_main, view_main)
        self.controller_map = Controller_Map(self.model_map, self.view_map)

    def update(self):
        # Update data:
        # self.controller_main.update()
        self.controller_map.update()

        # Update GUI:
        self.tk_root.update()