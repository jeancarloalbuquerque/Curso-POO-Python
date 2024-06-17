import sys


class Maze:
    def parse(self, input):
        return input
    
    def read(self):
        self.size = int(input())
        self.lines = []

        for i in range(2 * self.size + 1):
            line = input()
            if line:
                self.lines.append(line)
            else:
                break

        return self
    
    def map(self):
        self.map = []

        for line in self.lines:
            self.map.append(list(line))

        return self
    
    def render(self):
        for line in self.map:
            for chunk in line:
                print(chunk, end='')
            print('\r')
