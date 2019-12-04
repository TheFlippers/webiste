from display import Display

class FlipDiskDisplay(Display):
    def __init__(self, size=(7, 7), fdd_dim=7):
        super()
        self.size = size
        self.fdd_dim = fdd_dim
        self.fdd_size = tuple([int(size / self.fdd_dim) for size in self.size])

    def write(self, frame):

        # Print control word
        print('frame', end=' ')

        # Convert each grid into bytes row-wise
        for fdd_x in range(self.fdd_size[0]):
            for fdd_y in range(self.fdd_size[1]):
                print('(' + str(fdd_x) + ',' + str(fdd_y) + ')', end=' ')

                # Traverse subarrays to calculate byte values
                for y in range(self.fdd_dim * fdd_y, self.fdd_dim * (fdd_y + 1)):
                    byte = 0
                    for x in range(self.fdd_dim * fdd_x, self.fdd_dim * (fdd_x + 1)):
                        byte |= (frame[x][y] & 1)
                        byte <<= 1
                    print(hex(byte), end=' ')

if __name__ == '__main__':
    display = FlipDiskDisplay((14,7))
    frame = [[1] * 7 for i in range(14)]
    display.write(frame)
