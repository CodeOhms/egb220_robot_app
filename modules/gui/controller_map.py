class Controller_Map:
    def __init__(self, model_map, view_map):
        self.model_map = model_map
        self.view_map = view_map
        self.current_coord_index = 0

    def update(self):
        curr_coord = self.model_map.get_map_coord(self.current_coord_index)
        if curr_coord != None:
            next_coord_index = self.current_coord_index + 1
            next_coord = self.model_map.get_map_coord(next_coord_index)
            if next_coord != None:
                self.update_map(curr_coord, next_coord)
                self.current_coord_index += 1

    def update_map(self, prev_coord, curr_coord):
        self.view_map.update_map(prev_coord, curr_coord)