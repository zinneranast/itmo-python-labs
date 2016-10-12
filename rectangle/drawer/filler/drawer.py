from tkinter import *


class CoordinateException(Exception):
    def print_(self):
        print("Error: Incorrect coordinates of the rectangle.")


def draw(area, rects):
    try:
        root = Tk()
        canv = Canvas(root, width=area['width'], height=area['height'], bg="white", cursor="pencil")
        for rect in rects:
            canv.create_rectangle(rect['x1'], rect['y1'], rect['x2'], rect['y2'], outline="red")

    except CoordinateException as e:
        e.print_()

    return canv, root


def fill(canv, area, rects, x, y):
    minx = area["width"]
    maxx = 0
    miny = area["height"]
    maxy = 0

    xy = {'x': [minx, maxx], 'y': [miny, maxy]}
    for rect in rects:
        xy['x'] += [rect['x1'], rect['x2']]
        xy['y'] += [rect['y1'], rect['y2']]

    for k,v in xy.items():
        if k == 'x':
            for i in v:
                if i < minx and i > x:
                    minx = i
                if i > maxx and i < x:
                    maxx = i
        else:
            for i in v:
                if i < miny and i > y:
                    miny = i
                if i > maxy and i < y:
                    maxy = i

    canv.create_rectangle(minx, miny, maxx, maxy, fill="yellow")
    return canv
