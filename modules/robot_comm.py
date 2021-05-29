import serial
import array as arr

class Robot_Comm:
    def __init__(self, serial_port_str, baud_rate, input_buffer_size):
        self.serial_port_str = serial_port_str
        self.baud_rate = baud_rate
        self.serial = None
        self.input_buffer_size = input_buffer_size
        self.input_buffer = arr.array('B')
        # Initialise the array:
        # self.input_buffer.extend()

    def connect(self):
        self.serial = serial.Serial(self.serial_port_str, self.baud_rate)

    def get_input_byte(self):
        return self.serial.read()