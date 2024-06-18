import sys

class Maze:
    def __init__(self) -> None:
        self.origin = [0,0]
        self.destination = [0,0]
        self.sizeColumns = 0
        self.sizeLines = 0
        self.map = []
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
    
    def makeMap(self):
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

        self.sizeLines = len(self.map)
        self.sizeColumns = len(self.map[0])

        return self
    
    def render(self, position: list):
        for l, line in enumerate(self.map):
            for c, chunk in enumerate(line):
                if (position == [l, c]):
                    print('*', end='')
                else:
                    print(chunk, end='')
            print('\r')

