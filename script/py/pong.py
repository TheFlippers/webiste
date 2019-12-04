import random
from game import Game
from controller import Keyboard
from display import ConsoleDisplay

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        return False

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def to_grid(self):
        return Vector(int(self.x), int(self.y))

    def copy(self):
        return Vector(self.x, self.y)

class PongBall():
    init_speeds = [-1, 1]

    def __init__(self, pos=(0, 0)):
        self.start = Vector(pos[0], pos[1])
        self.pos = None
        self.velocity = None

        self.reset()

    def bounce(self, x=False, y=False):
        if x is True:
            self.velocity.x *= -1
        if y is True:
            self.velocity.y *= -1

    def move(self):
        self.pos += self.velocity

    def next_pos(self):
        return self.pos + self.velocity

    def reset(self):
        self.pos = self.start.copy()
        self.velocity = Vector(random.choice(PongBall.init_speeds), \
                               random.choice(PongBall.init_speeds))

class PongPaddle():
    def __init__(self, pos=(0, 0), length=2, controls=('w', 's')):
        self.pos = Vector(pos[0], pos[1])
        self.length = length
        self.controls = controls

    def top(self):
        return self.pos.y + self.length - 1

    def bottom(self):
        return self.pos.y

    def get_points(self):
        for i in range(self.length):
            yield Vector(self.pos.x, self.pos.y + i)

    def move_up(self):
        self.pos.y += 1

    def move_down(self):
        self.pos.y -= 1

    def move(self, keys, clear_above, clear_below):
        if self.controls[0] in keys and clear_above:
            self.move_up()
        if self.controls[1] in keys and clear_below:
            self.move_down()

class Pong(Game):
    def __init__(self, controller, display, tick_rate=15, size=(14, 7), max_score=3, enable_key='r'):
        super().__init__(controller, display, tick_rate)
        self.size = Vector(size[0], size[1])
        self.board = [[0] * self.size.y for i in range(self.size.x)]
        self.ball = PongBall((7, 3))
        self.paddles = [PongPaddle(pos=(1, 3)), PongPaddle(pos=(12, 3), controls=('o', 'l'))]
        self.score = [0, 0]
        self.max_score = max_score
        self.enable_key = enable_key
        self.enabled = False

    def tick(self, keys):
        # Check for enable
        if self.enable_key in keys:
            self.enabled = True
        if not self.enabled:
            return self.board

        # Check for goal
        if int(self.ball.pos.x) == 0:
            self.score[1] += 1
            self.ball.reset()
        if int(self.ball.pos.x) == self.size.x - 1:
            self.score[0] += 1
            self.ball.reset()

        # Move paddles
        for paddle in self.paddles:
            paddle.move(keys, paddle.top() != self.size.y - 1, paddle.bottom() != 0)

        # Move Ball
        bounce_x = sum([self.ball.next_pos().to_grid() in paddle.get_points() for paddle in self.paddles]) > 0
        bounce_y = (int(self.ball.pos.y) == 0 and self.ball.velocity.y < 0) or \
            (int(self.ball.pos.y) == self.size.y - 1 and self.ball.velocity.y > 0)
        self.ball.bounce(x=bounce_x, y=bounce_y)
        self.ball.move()

        # Check for scores
        if int(self.ball.pos.x) == 0 or int(self.ball.pos.x) == self.size.x - 1:
            print("game over!")

        # Update board
        self.board = [[0] * self.size.y for i in range(self.size.x)]
        self.board[int(self.ball.pos.x)][int(self.ball.pos.y)] = 1
        for paddle in self.paddles:
            for point in paddle.get_points():
                self.board[point.x][point.y] = 1

        # Check end game condition
        if max(self.score) == self.max_score:
            self.game_over = True

        return self.board

if __name__ == '__main__':

    controller = Keyboard(['w', 's', 'o', 'l'])
    display = ConsoleDisplay((14, 7), flip=True)
    pong = Pong(controller, display, tick_rate=5)

    pong.run()
