from pong import Pong
from web_interface import WebInterface
from flip_disk_display import FlipDiskDisplay

if __name__ == '__main__':
    controller = WebInterface()
    display = FlipDiskDisplay((14, 7))

    game = Pong(controller, display)
    game.start()

    controller.server_run_forever()
