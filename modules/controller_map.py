class Controller_Map:
    def __init__(self, model_map, view_map):
        self.model_map = model_map
        self.view_map = view_map
        self.current_coord_index = 0

    def update(self):
        self.update_map()

    def update_map(self):
        # Check for new data and update model:
        # comm_data = self.model_map.get_comm_data()
        # if comm_data != None:
        #     self.model_map.process_comm_data(comm_data)

        # Get data from model to recursively update view:
        while True:
            curr_coord = self.model_map.get_map_coord(self.current_coord_index)
            if curr_coord != None:
                next_coord_index = self.current_coord_index + 1
                next_coord = self.model_map.get_map_coord(next_coord_index)
                if next_coord != None:
                    self.view_map.update_map(curr_coord, next_coord)
                    self.current_coord_index += 1
                else:
                    break
            else:
                break
        