from time import sleep
from keyboard import is_pressed

class Controller():
    def __init__(self):
        pass

    def read(self):
        raise NotImplementedError

class Keyboard(Controller):
    def __init__(self, watch_keys):
        super()
        self.watch_keys = watch_keys

    def read(self):
        # check watched keys for presses
        return [key for key in self.watch_keys if is_pressed(key)]

if __name__ == '__main__':
    pass
