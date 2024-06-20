from Maze import Maze
from Solver import Solver
import time

maze = Maze().read().makeMap()
solver = Solver(maze)

def handOnWall(hand = 'right'):
    while (solver.position != maze.destination):
    
        if(solver.lookAhead() != 'wall'):
            solver.forward()
            maze.render(solver.position, solver.direction)
            solver.left() if hand == 'left' else solver.right()

            if (solver.lookAhead() != 'wall'):
                solver.forward()
                maze.render(solver.position, solver.direction)

            else:
                solver.right() if hand == 'left' else solver.left()
        else:
            solver.right() if hand == 'left' else solver.left()

handOnWall('left')

