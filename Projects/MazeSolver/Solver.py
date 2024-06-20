from Maze import Maze

class Solver():
    def __init__(self, maze: Maze):
        self.maze = maze
        self.position = maze.origin
        self.direction = 'down'

    def turn(self, direction = 1):
        directions = ['up', 'right', 'down', 'left']
        total = len(directions)

        current = directions.index(self.direction)
        next = (current + direction) % total
        
        return directions[next]

    def right(self):
       self.direction = self.turn(1)
    
    def left(self):
       self.direction = self.turn(-1)
    
    def forward(self):
        if (self.direction == 'up'):
            self.move(self.position[0] - 1, self.position[1])
        elif (self.direction == 'right'):
            self.move(self.position[0], self.position[1] + 1)
        elif (self.direction == 'down'):
            self.move(self.position[0] + 1, self.position[1])
        elif (self.direction == 'left'):
            self.move(self.position[0], self.position[1] - 1)
        
        return self
        
    
    def move(self, line, column):
        if (self.look(line, column) != 'wall'):
            self.position = [line, column]
        return self

    
    def look(self, line, column):
        if (line >= 0 and line <= len(self.maze.map) and column >= 0 and column <= len(self.maze.map[0])):
            if (self.maze.map[line][column] == '█'):
                return 'wall'
            if (self.maze.map[line][column] == ' '):
                return 'passage'
            if (self.maze.map[line][column] == 'O'):
                return 'passage'
            if (self.maze.map[line][column] == 'X'):
                return 'exit'  
        else:
            return 'wall'
        
    def lookAhead(self):
        if (self.direction == 'up'):
            return self.look(self.position[0] - 1, self.position[1])
        elif (self.direction == 'right'):
            return self.look(self.position[0], self.position[1] + 1)
        elif (self.direction == 'down'):
            return self.look(self.position[0] + 1, self.position[1])
        elif (self.direction == 'left'):
            return self.look(self.position[0], self.position[1] - 1)

    def render(self):
        self.maze.render(self.position, self.direction)