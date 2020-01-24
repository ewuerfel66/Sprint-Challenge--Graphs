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

    # def connect_rooms(self, prev_room, next_room):


    def get_neighbor_dict(self, room_id):
        return self.rooms[room_id]

    # Get a room's neighbors
    def get_neighbors(self, room_id):
        neighbors = []

        # Iter through dict and add values
        for key in self.rooms[room_id]:
            # print(key)
            neighbors.append(self.rooms[room_id][key])

        return neighbors

    def find_nearest_unexplored_room(self, player):
        """
        Basically a breadth-first search
        """        
        # Create empty queue & enqueue starting room
        queue = Queue()
        queue.enqueue([player.current_room.id])
        
        # Create a new visited set
        bfs_visited = set()
        
        while queue.size() > 0:
            
            # dequeue the current room/path
            path = queue.dequeue()
            cur_room = path[-1]
            
            if cur_room not in bfs_visited:
                
                # Check if there is an unexplored exit
                if "?" in self.get_neighbors(cur_room):
                    # If so, return the path
                    return path
                
                # Mark as visited
                bfs_visited.add(cur_room)
                
                # Add it's neighbors
                for neighbor in self.get_neighbors(cur_room):
                    # Copy to avoid reference error
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

    def find_longest_path(self):
        """
        Basically a BFS for the longest chain
        """
        # Create empty queue
        queue = Queue()
        queue.enqueue([0])
        
        max_path = []
        
        while queue.size() > 0:
            # Get path and current room back
            path = queue.dequeue()
            cur_room = path[-1]
            
            # If the path is longer than max_path_len
            if len(path) > len(max_path):
                max_path = path
                
            # Add the neighbors
            for neighbor in self.get_neighbors(cur_room):
                new_path = list(path)
                new_path.append(neighbor)
                queue.enqueue(new_path)
                
        return max_path

    def path_to_directions(self, path):
        directions = []

        for i in range(len(path) - 1):
            # Get current and next room
            cur_room, next_room = path[i], path[i+1]

            # Iterate through keys, look for entry matching next_room
            for key in self.rooms[cur_room]:
                if self.rooms[cur_room][key] == next_room:
                    directions.append(key)
                    
        return directions

    def connect_all(self):
        # Iterate through rooms
        for room in self.rooms:
            neighbors = self.rooms[room]
            # Iterate through neighbors
            for neighbor in neighbors:
                value = neighbors[neighbor]
                if value != "?":
                    # Update value
                    self.rooms[value] = room 