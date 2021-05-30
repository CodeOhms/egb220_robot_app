class Model_Map:
    def __init__(self, icoord_data):
        self.icoord_data = icoord_data

        # self.coordinates = []

        # dummy data
        self.coordinates = [(0, 10), (20, 30), (25, 15), (0, 10), (25, 10), (-10, -10)]

    def store_map_coord(self, x, y):
        self.coordinates.append((x, y))

    def get_map_coord(self, index):
        result = None
        if index < len(self.coordinates):
            result = self.coordinates[index]
        return result
    
    def get_comm_data(self):
        return self.icoord_data.get_comm_data()

    def process_comm_data(self, comm_data):
        return self.icoord_data.process_comm_data(comm_data)