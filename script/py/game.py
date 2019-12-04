from threading import Thread
from time import sleep

class Game(Thread):
    def __init__(self, controller, display, tick_rate=15):
        super().__init__()
        self.controller = controller
        self.display = display
        self.frame_period = 1 / tick_rate
        self.game_over = False

    def tick(self):
        raise NotImplementedError

    def run(self):
        # Run game loop
        while not self.game_over:

            # Receive user input
            user_input = self.controller.read()

            # Update game state
            frame = self.tick(user_input)

            # Display game state
            self.display.write(frame)

            # Wait for next frame
            sleep(self.frame_period)
