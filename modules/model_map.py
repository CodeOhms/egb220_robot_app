class Model_Map:
    def __init__(self, icoord_data):
        self.icoord_data = icoord_data

        self.abs_coordinates = []

        # # dummy data
        # self.abs_coordinates = [(0, 10), (20, 30), (25, 15), (0, 10), (25, 10), (-10, -10)]

    def store_map_coord(self, x, y):
        """
        Append given coordinates to stored list of absolute coordinates.
        """

        self.abs_coordinates.append((x, y))
    
    def store_map_coords(self, abs_coords):
        for coord in abs_coords:
            self.store_map_coord(abs_coords[0], abs_coords[1])

    def get_map_coord(self, index):
        result = None
        if index < len(self.abs_coordinates):
            result = self.abs_coordinates[index]
        return result
    
    def get_comm_data(self):
        return self.icoord_data.get_comm_data()

    def process_comm_data(self, comm_data):
        return self.icoord_data.process_comm_data(comm_data)