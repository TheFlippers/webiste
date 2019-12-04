import os

class Display():
    def __init__(self):
        pass

    def write(self, frame):
        raise NotImplementedError

class ConsoleDisplay(Display):
    def __init__(self, size, on_char='*', off_char=' ', flip=False, mirror=False):
        super()
        self.size = size
        self.on_char = on_char
        self.off_char = off_char
        self.flip = flip
        self.mirror = mirror

    def write(self, frame):
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Draw frame
        '''
        x_range = range(self.size[0]) if not self.mirror else range(self.size[0] - 1. -1, -1)
        y_range = range(self.size[1]) if not self.flip else range(self.size[1] - 1. -1, -1)
        '''
        for y in range(self.size[1] - 1, -1, -1):
            for x in range(self.size[0]):
                print(self.on_char if frame[x][y] == 1 else self.off_char, end='')
            print()
