from Maze import Maze
from Solver import Solver

maze = Maze().read().makeMap()
solver = Solver(maze)


solver.right().right().forward()
solver.left().forward().forward()
solver.forward()

maze.render(solver.position)


# maze.leftHand()

