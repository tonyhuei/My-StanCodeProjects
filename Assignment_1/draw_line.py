"""
File: draw_line.py
Name: Tony
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the dot
SIZE = 20

# Global var
window = GWindow(800, 800)
# number_click = 1
second_click = False
pre_x = 0   # "pre_x" represents the dot's x-coordinate
pre_y = 0   # "pre_y" represents the dot's y-coordinate


def main():
    onmouseclicked(first)


def first(circle):
    global second_click, pre_x, pre_y
    if second_click is False:
        dot = GOval(SIZE, SIZE)
        window.add(dot, x=circle.x-SIZE/2, y=circle.y-SIZE/2)
        pre_x = circle.x
        pre_y = circle.y
        second_click = True
    else:
        objects = window.get_object_at(pre_x, pre_y)
        if objects is not None:
            window.remove(objects)
        line = GLine(circle.x, circle.y, pre_x, pre_y)
        window.add(line)
        second_click = False


if __name__ == "__main__":
    main()
