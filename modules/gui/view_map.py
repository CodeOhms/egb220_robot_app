import tkinter as tk
from tkinter import ttk

class View_Map:
    def __init__(self, frame):
        self.frame_map = frame
        self.map_canvas = tk.Canvas(self.frame_map)

        # Set layout
            # Place the map frame within the main frame:
        self.frame_map.grid(row=0, column=0)
            # Layout within the map frame:
                # Map canvas should be the only thing in the map frame:
        self.map_canvas.pack()

    def update_map(self, coord_0, coord_1):
        """
        Call from controler to draw new coordinate data on the map.
        """

        self.map_canvas.create_line(coord_0[0], coord_0[1], coord_1[0], coord_1[1])
    
    def map_smooth(self):
        """
        Will destroy all the lines representing the map and produce a new map of one line consisting of splines.
        """

        pass