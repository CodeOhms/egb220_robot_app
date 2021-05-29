class Model_Map:
    def __init__(self):
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