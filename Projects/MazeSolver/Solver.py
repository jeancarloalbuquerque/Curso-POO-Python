from Maze import Maze

maze = Maze().read().map()

maze.render()
print("\nOrigin: ", maze.origin)
print("Destination: ", maze.destination)
# maze.leftHand()

