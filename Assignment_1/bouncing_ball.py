"""
File: bouncing_ball.py
Name: Tony
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Below are constants
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global var
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
process = True  # indicates whether the ball is moving. # process =0
count = 1   # represents the number of times the ball exceeds the right window


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(move)
    window.add(ball, x=START_X, y=START_Y)
    ball.filled = True
    ball.fill_color = "green"
    ball.color = "green"


def move(mouse):
    global process, count
    speed = 0  # the ball's moving speed
    if process and count <= 3:  # process =0
        process = False     # process =1
        while True:
            if speed >= 0:
                # if 0 <= speed < 1:
                #     speed = GRAVITY
                ball.move(VX, speed)
                if ball.y + ball.height > window.height and speed > 0:     # if ball.y + ball.height >= window.height
                    # ball.move(VX, window.height-ball.y)   # y moves to the position of 500 (y-axis) use constant
                    speed = - REDUCE * speed
                else:
                    speed += GRAVITY
            if speed < 0:
                ball.move(VX, speed)
                speed += GRAVITY    # speed += 0.9*GRAVITY
            if ball.x + ball.width >= window.width:
                ball.x = START_X
                ball.y = START_Y
                break
            pause(10*DELAY)
        count += 1
        process = True  # process =0


if __name__ == "__main__":
    main()
