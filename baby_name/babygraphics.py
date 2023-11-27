"""
File: babygraphics.py
Name: Tony
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * ((width - 2*GRAPH_MARGIN_SIZE) / (len(YEARS)))
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # 畫最上面的線
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)

    # 畫最下面的線
    canvas.create_line(GRAPH_MARGIN_SIZE,  CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    for i in range(len(YEARS)):
        x_axis = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_axis, 0, x_axis, CANVAS_HEIGHT)    # 畫年份垂直線，下一行code是標註年份文字
        canvas.create_text(x_axis + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    out_rank = MAX_RANK + 1     # 該年沒上榜的名次當做1001名
    height = CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE    # 點可以出現的垂直距離
    ratio = height / MAX_RANK
    gmz = GRAPH_MARGIN_SIZE

    for i in range(len(lookup_names)):
        if lookup_names[i] in name_data:    # 判斷名字是否在name_data裡
            c_i = i % len(COLORS)   # 線、文字顏色編號(取餘數)
            list_x = []
            list_y = []
            for j in range(len(YEARS)):
                list_x.append(get_x_coordinate(CANVAS_WIDTH, j))
                if str(YEARS[j]) not in name_data[lookup_names[i]]:
                    rank = out_rank
                    list_y.append(out_rank * ratio + gmz)
                else:
                    rank = int(name_data[lookup_names[i]][str(YEARS[j])])
                    list_y.append(rank * ratio + gmz)
                if j > 0:
                    canvas.create_line(list_x[j-1], list_y[j-1], list_x[j], list_y[j], width=LINE_WIDTH,
                                       fill=COLORS[c_i])
                if list_y[j] != out_rank * ratio + gmz:
                    canvas.create_text(list_x[j] + TEXT_DX, list_y[j], text=str(lookup_names[i])+" "+str(rank),
                                       anchor=tkinter.SW, fill=COLORS[c_i])
                else:
                    canvas.create_text(list_x[j] + TEXT_DX, list_y[j], text=str(lookup_names[i]) + "  *",
                                       anchor=tkinter.SW, fill=COLORS[c_i])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
