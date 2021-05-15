# Render a bitmap in Desmos using parallel list of colored coordinates technique
# Maze prototype: https://www.desmos.com/calculator/jjj3l82fg7

import mazegen

M = mazegen.M

def render_bitmap(bitmap: M, filled: bool):
    height = len(bitmap)
    width = len(bitmap[0])
    xlist = []
    ylist = []
    megalist = []
    for y in range(height):
        desmos_y = height - 1 - y
        megalist.extend(map(int, bitmap[y]))
        for x in range(width):
            if bitmap[y][x] == filled:
                xlist.append(x)
                ylist.append(desmos_y)
    # return xlist, ylist
    print('u={}'.format(xlist))
    print('v={}'.format(ylist))
    print('m={}'.format(megalist))

render_bitmap(mazegen.generate_maze(21, 21, 3157464641), mazegen.WALL)
# render_bitmap(mazegen.generate_maze(7, 7, 1337), mazegen.WALL)
