from util import Stack, Queue

class Graph:
    """
    Represent Graph as a dict with `room_id` as the key, 
    and a dict with valid directions to move and their neighbor's
    `room_id` as the value

    {
        0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
        5: {'n': 0, 's': '?', 'e': '?'}
    }
    """

    def __init__(self):
        self.rooms = {}

    # Add current `room_id` and valid directions with `?` as a place-holder
    def add_current_room(self, room_id, valid_directions):
        # Add room_id and empty dict to rooms
        self.rooms[room_id] = {}

        # Fill in valid directions with `?` as place-holder
        for direction in valid_directions:
            self.rooms[room_id][direction] = "?"

    # Get a room's neighbors
    def get_neighbors(self, room_id):
        neighbors = []

        # Iter through dict and add values
        for key in self.rooms[room_id]:
            neighbors.append(self.rooms[room_id][key])

        return neighbors