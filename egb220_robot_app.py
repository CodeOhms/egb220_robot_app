import tkinter as tk
from tkinter import ttk

# User modules
# from modules.robot_comm import *
from modules.gui.gui import Gui

if __name__ == "__main__":
    gui = Gui(tk.Tk())
    
    while True:
        gui.update()