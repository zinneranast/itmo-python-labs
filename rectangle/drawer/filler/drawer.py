from tkinter import *
import uuid


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


def fill(canv, area, rects, x, y):
    all_rects = []

    # assign unique id for background
    back_id = int(uuid.uuid1().int >> 64)
    unique_areas = {}

    # form two arrays for storing all x coordinates and all y coordinates
    xx = [0, area["width"]]
    yy = [0, area["height"]]

    for rect in rects:
        xx += [rect['x1'], rect['x2']]
        yy += [rect['y1'], rect['y2']]

    # sort this arrays
    xx.sort()
    yy.sort()

    # form array which contains all rectangles formed by splitting the main field
    for j in range(len(yy) - 1):
        for i in range(len(xx) - 1):
            all_rects.append({'x1': xx[i], 'y1': yy[j], 'x2': xx[i + 1], 'y2': yy[j + 1]})

    # check which rectangles are included in main rectangles
    point_id = 0
    for small_rect in all_rects:
        contains_rect = []

        for rect in rects:
            if small_rect['x1'] >= rect['x1'] and small_rect['x2'] <= rect['x2'] and small_rect['y1'] >= rect['y1'] and small_rect['y2'] <= \
                    rect['y2']:
                contains_rect.append(rect)

        # assign new id for area formed by crossed rectangles
        id = 0
        if contains_rect:
            for i in contains_rect:
                id += i['id']
        else:
            id = back_id

        # form new array
        if id in unique_areas:
            unique_areas[id] += [small_rect]
        else:
            unique_areas[id] = [small_rect]

        if x >= small_rect['x1'] and x <= small_rect['x2'] and y >= small_rect['y1'] and y <= small_rect['y2']:
            point_id = id

    # check whether two rectangles are adjacent
    def check(canv, rect1, rect2):
        if (rect1['x2'] == rect2['x1'] and (rect1['y1'] < rect2['y2'] or rect1['y2'] > rect2['y1'])) or (
                        rect1['x1'] == rect2['x2'] and (rect1['y1'] < rect2['y2'] or rect1['y2'] > rect2['y1'])) or (
                        rect1['y1'] == rect2['y2'] and (rect1['x1'] > rect2['x2'] or rect1['x2'] < rect2['x1'])) or (
                        rect1['y2'] == rect2['y1'] and (rect1['x1'] > rect2['x2'] or rect1['x2'] < rect2['x1'])):
            canv.create_rectangle(rect1['x1'], rect1['y1'], rect1['x2'], rect1['y2'], fill="black")
            canv.create_rectangle(rect2['x1'], rect2['y1'], rect2['x2'], rect2['y2'], fill="black")
            return canv

        if x >= rect1['x1'] and x <= rect1['x2'] and y >= rect1['y1'] and y <= rect1['y2']:
            canv.create_rectangle(rect1['x1'], rect1['y1'], rect1['x2'], rect1['y2'], fill="black")
        else:
            canv.create_rectangle(rect2['x1'], rect2['y1'], rect2['x2'], rect2['y2'], fill="black")

        return canv

    # draw
    if len(unique_areas[point_id]) == 2:
        return check(canv, unique_areas[point_id][0], unique_areas[point_id][1])
    for rect in unique_areas[point_id]:
        canv.create_rectangle(rect['x1'], rect['y1'], rect['x2'], rect['y2'], fill="black")

    return canv
