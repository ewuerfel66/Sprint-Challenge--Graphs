from room import Room
from player import Player
from world import World
from graph import Graph
from util import Stack, Queue

import random
from ast import literal_eval

opposite_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited = set()


# Instantiate Graph
graph = Graph()

# Add the first room to graph and visited
graph.add_current_room(player.current_room.id, player.current_room.get_exits())
visited.add(player.current_room.id)

while len(visited) < 500:
    # Find unexplored directions
    unexplored_dirs = []
    for key in graph.rooms[player.current_room.id]:
        if graph.rooms[player.current_room.id][key] == "?":
            unexplored_dirs.append(key)
            
    # If there are unexplored dirs, make a random move
    if len(unexplored_dirs) > 0:
        player.random_move(graph, traversal_path, visited, unexplored_dirs)
        # path = graph.find_longest_path(player)
        # if path is not None:
        #     # Get directions
        #     directions = graph.path_to_directions(path)

        #     # Follow directions
        #     player.follow_directions(graph, visited, directions, traversal_path)
        
    # If there are no unexplored dirs, bfs
    else:
        path = graph.find_nearest_unexplored_room(player)
        if path is not None:
            # Get directions for path
            directions = graph.path_to_directions(path)

            # Follow directions
            player.follow_directions(graph, visited, directions, traversal_path)
        else:
            pass

# graph.connect_all()
# breakpoint()

# REPORTING
print("")
print(f"Path: {traversal_path}")
print("")
print("Graph:")
print(graph.rooms)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")