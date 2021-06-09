import serial
import array as arr

import random

class Robot_Comm:
    def __init__(self, size_of_coord_data, serial_port_str, baud_rate):
        self.size_of_coord_data = 2
        
        self.serial_port_str = serial_port_str
        self.baud_rate = baud_rate
        self.serialcon = None

    def connect(self):
        self.serialcon = serial.Serial(self.serial_port_str, self.baud_rate)

    def get_input_bytes(self, num_bytes):
        return self.serialcon.read(num_bytes)
    
    def get_input(self):
        # Read in identifier byte:
        id_byte = self.get_input_bytes(1)

        # Read in following data, more than one byte:
        data = self.get_input_bytes(self.size_of_coord_data)

        return (id_byte, data)
    
    def get_input_stream(self):
        comm_data_stream = []
        
        # While data is available to retrieve, grab it:
        while self.serialcon.in_waiting != 0:
            comm_data_stream.append(self.get_input())

        return comm_data_stream
    
    def get_input_stream_dummy(self):
        comm_data_stream = []
        
        x = 0
        y = 0
        for p in range(2):
            x += random.randint(1, 200)
            y += random.randint(1, 200)
            comm_data_stream.append((bytes(b'\x00'), x))
            comm_data_stream.append((bytes(b'\x01'), y))
        
        return comm_data_stream