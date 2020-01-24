import random
from util import Queue

opposite_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}

class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room

    def travel(self, direction, show_rooms = False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")

    def random_move(self, graph, traversal_path, visited, unexplored_dirs):
        global opposite_dirs

        # Save previous room before moving
        prev_room = self.current_room.id

        # If there are unexplored dirs, move that way
        direction = random.choice(unexplored_dirs)
        traversal_path.append(direction)

        # Move that direction
        self.travel(direction)
        new_room = self.current_room.id

        # Add new room to graph.rooms and visited
        graph.add_current_room(new_room, self.current_room.get_exits())

        # Connect rooms in graph
        graph.rooms[prev_room][direction] = int(new_room)
        graph.rooms[new_room][opposite_dirs[direction]] = int(prev_room)

        visited.add(new_room)

        print("")
        print(f"Prev: {prev_room}, Next: {self.current_room.id}")
        print(graph.rooms)
        print("")

    def follow_directions(self, graph, visited, directions, traversal_path):
        global opposite_dirs

        for direction in directions:
            # Save previous room to connect later
            prev_room = self.current_room.id

            # Add direction to traversal path
            traversal_path.append(direction)

            # Move that dir
            self.travel(direction)

            # Add new room if not in visited
            if self.current_room.id not in visited:
                graph.add_current_room(self.current_room.id, self.current_room.get_exits())
                visited.add(self.current_room.id)

            # Connect rooms
            # graph.rooms[prev_room][direction] = self.current_room.id
            # graph.rooms[self.current_room.id][opposite_dirs[direction]] = prev_room        