XCOORD_BYTE_ID = bytes(b'\x00')
YCOORD_BYTE_ID = bytes(b'\x01')

class Coord_Data_Interpreter:
    def __init__(self):
        pass

    def interpret_single_command(self, comm_data):
        """
        Pass in `comm_data` which must be a tuple with the 1st element
        as a byte used to identify type of the data in the 2nd element.
        Returns a tuple containing an x and y coordinate, but one will
        always be zero as if it is an x coordinate it will only have
        that to store.
        """

        rel_coord = None
        # Command byte to indicate x or y coordinate:
        if comm_data[0] == XCOORD_BYTE_ID:
            # x coord
            rel_coord = (comm_data, 0)
        elif comm_data[0] == YCOORD_BYTE_ID:
            # y coord
            rel_coord = (0, comm_data)

    def interpret_stream(self, comm_data_stream):
        rel_coords = []

        for data in comm_data_stream:
            rel_coords.append(self.interpret_single_command(data))
        
        return rel_coords

class Coord_Data_Evaluator:
    def __init__(self):
        pass

    def relative_to_absolute_coords(self, rel_coords):
        """
        Pass in list of tuples containing relative x and y
        coordinates, in that order, to produce a list of absolute x and y
        coordinates.
        """

        abs_coords = []
        sum_x = 0
        sum_y = 0
        for p in rel_coords:
            abs_x = p[0] + sum_x
            abs_y = p[1] + sum_y
            abs_coords.append((abs_x , abs_y))
            sum_x = abs_x
            sum_y = abs_y
        
        return abs_coords

class ICoord_Data:
    def __init__(self, robot_comms, coord_data_interpreter, coord_data_math):
        self.comms = robot_comms
        self.interpreter = coord_data_interpreter
        self.evaluator = coord_data_math

    def get_comm_data(self):
        """
        Get the raw bytes from the robot communications to process
        with `process_comm_data`.
        """
        
        return self.comms.get_input_stream()

    def process_comm_data(self, comm_data):
        """
        Interpret and calculate absolute x and y coords.
        """
        
        rel_coords = self.interpreter.interpret_stream(comm_data)
        return self.evaluator.relative_to_absolute_coords(rel_coords)

def generate_coord_data_interface(robot_comms):
    interpreter = Coord_Data_Interpreter()
    evaluator = Coord_Data_Evaluator()
    interface = ICoord_Data(robot_comms, interpreter, evaluator)
    return interface