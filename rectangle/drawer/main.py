# from rectangle.drawer.placer.rectangleplacer import place
from Tkinter import *
import uuid


def place():
    try:
        data = read("input.txt")
    except Exception:
        print("Error: Something was going wrong while reading the file.")

    data = data.split()
    area = {'width': int(data[0]), 'height': int(data[1])}
    rects = []
    if not len(data[2:]) % 4:
        number_of_rects = int(len(data[2:]) / 4)
        i = 2
        for rect in range(number_of_rects):
            x1 = int(data[i])
            x2 = int(data[i + 2])
            y1 = int(data[i + 1])
            y2 = int(data[i + 3])
            if x1 > area['width'] or x2 > area['width'] or y1 > area['height'] or y2 > area['height']:
                raise CoordinateException
            rects.append({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'id': uuid.uuid1().int >> 64})
            i += 4

    canv, root = draw(area, rects)
    canv.pack()
    root.bind_all('<Button-1>', lambda e: fill(canv, area, rects, e.x, e.y))
    root.mainloop()


def read(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read()
            return data
    except Exception:
        raise Exception


class CoordinateException(Exception):
    def print_(self):
        print("Error: Incorrect coordinates of the rectangle.")


def draw(area, rects):
    try:
        root = Tk()
        canv = Canvas(root, width=area['width'], height=area['height'], bg="white", cursor="pencil")
        for rect in rects:
            canv.create_rectangle(rect['x1'], rect['y1'], rect['x2'], rect['y2'])

    except CoordinateException as e:
        e.print_()

    return canv, root


def fill1(canv, area, rects, x, y):
    minx = area["width"]
    maxx = 0
    miny = area["height"]
    maxy = 0

    xy = {'x': [minx, maxx], 'y': [miny, maxy]}
    for rect in rects:
        xy['x'] += [rect['x1'], rect['x2']]
        xy['y'] += [rect['y1'], rect['y2']]

    for k, v in xy.items():
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


def fill2(canv, area, rects, x, y):
    for rect in rects:
        if x > rect['x1'] and x < rect['x2'] and y > rect['y1'] and y < rect['y2']:
            return fill1(canv, area, rects, x, y)
    canv.create_rectangle(0, 0, area["width"], area["height"], fill="yellow")
    for rect in rects:
        canv.create_rectangle(rect['x1'], rect['y1'], rect['x2'], rect['y2'], fill="white")
    rects.reverse()
    for rect in rects:
        canv.create_line(rect['x1'], rect['y1'], rect['x1'], rect['y2'])
        canv.create_line(rect['x2'], rect['y1'], rect['x2'], rect['y2'])
        canv.create_line(rect['x1'], rect['y2'], rect['x2'], rect['y2'])
        canv.create_line(rect['x1'], rect['y1'], rect['x2'], rect['y1'])
    return canv


def fill(canv, area, rects, x, y):
    all_rects = []

    back_id = int(uuid.uuid1().int >> 64)
    unique_areas = {}

    xx = [0, area["width"]]
    yy = [0, area["height"]]

    for rect in rects:
        xx += [rect['x1'], rect['x2']]
        yy += [rect['y1'], rect['y2']]

    xx.sort()
    yy.sort()

    for j in range(len(yy) - 1):
        for i in range(len(xx) - 1):
            all_rects.append({'x1': xx[i], 'y1': yy[j], 'x2': xx[i + 1], 'y2': yy[j + 1]})

    point_id = 0
    for small_rect in all_rects:
        contains_rect = []

        for rect in rects:
            if small_rect['x1'] >= rect['x1'] and small_rect['x2'] <= rect['x2'] and small_rect['y1'] >= rect['y1'] and small_rect['y2'] <= \
                    rect['y2']:
                contains_rect.append(rect)

        id = 0
        if contains_rect:
            for i in contains_rect:
                id += i['id']
        else:
            id = back_id

        if id in unique_areas:
            unique_areas[id] += [small_rect]
        else:
            unique_areas[id] = [small_rect]

        if x >= rect['x1'] and x <= rect['x2'] and y >= rect['y1'] and y <= rect['y2']:
            point_id = id

    for area in unique_areas:
        if area == point_id:
            for rect in unique_areas[area]:
                canv.create_rectangle(rect['x1'], rect['y1'], rect['x2'], rect['y2'], fill="red", outline="red")

    return canv


place()
