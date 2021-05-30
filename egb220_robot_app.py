import tkinter as tk
from tkinter import ttk

# User modules
from modules.robot_comm import *
from modules.model_map import *
from modules.controller_map import *
from modules.coord_data import *
from modules.gui import Gui

if __name__ == "__main__":
    # Initialise the backend:
    robot_comms = Robot_Comm('/dev/ttyACM0', 9600, 128)
    icoord_data = generate_coord_data_interface(robot_comms)
    model_main = None
    model_map = Model_Map(icoord_data)
    gui = Gui(tk.Tk(), model_main, model_map)
    
    while True:
        gui.update()