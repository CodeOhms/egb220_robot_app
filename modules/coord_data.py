class Coord_Data_Interpreter:
    def __init__(self):
        pass

class Coord_Data_Evaluator:
    def __init__(self):
        pass

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
        
        return self.comms.get_input()

    def process_comm_data(self, comm_data):
        """
        Interpret and calculate x and y coord.
        """
        
        coord_vars = self.interpreter.interpret(comm_data)
        return self.evaluator.evaluate(coord_vars)

def generate_coord_data_interface(robot_comms):
    interpreter = Coord_Data_Interpreter
    evaluator = Coord_Data_Evaluator
    interface = ICoord_Data(robot_comms, interpreter, evaluator)
    return interface