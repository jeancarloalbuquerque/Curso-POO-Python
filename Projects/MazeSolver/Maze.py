import sys

class Maze:
    def __init__(self) -> None:
        self.direction = 'up'
        self.origin = [0,0]
        self.destination = [0,0]
        pass

    def read(self):
        self.size = int(input())
        self.readLines = []

        for i in range(2 * self.size + 1):
            line = input()
            if line:
                self.readLines.append(line)
            else:
                break

        return self
    
    def map(self):
        self.map = []

        for line in self.readLines:
            self.map.append(list(line))

        for l, line in enumerate(self.map):
            if 'O' in line:
                self.origin[0] = l
                self.origin[1] = line.index('O')
            if 'X' in line:
                self.destination[0] = l
                self.destination[1] = line.index('X')
        return self
    
    def render(self):
        for line in self.map:
            for chunk in line:
                print(chunk, end='')
            print('\r')

    # def leftHand(self):
        