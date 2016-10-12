from tkinter import *


class CoordinateException(Exception):
    def print_(self):
        print("Error: Incorrect coordinates of the rectangle.")


def filereader(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        raise FileNotFoundError
    except Exception:
        raise Exception


def placer(canv, area, rects, color='white'):
    xx = []
    yy = []
    for rect in rects:
        if rect['x1'] > area['width'] or rect['x2'] > area['width'] or rect['y1'] > area['height'] or rect['y2'] > area[
            'height']:
            raise CoordinateException
        xx.append(rect['x1'])
        xx.append(rect['x2'])
        yy.append(rect['y1'])
        yy.append(rect['y2'])
        canv.create_rectangle(rect['x1'], rect['y1'], rect['x2'], rect['y2'], fill=color, outline="red")
    return canv, xx, yy


def find_closest_lines(area, xx, yy, cross_points, x, y):
    minx = area["width"]
    maxx = 0
    miny = area["height"]
    maxy = 0

    for i in xx:
        if i < minx and i > x:
            minx = i
        if i > maxx and i < x:
            maxx = i
    for i in yy:
        if i < miny and i > y:
            miny = i
        if i > maxy and i < y:
            maxy = i

    if not ([minx, miny] in cross_points and [minx, maxy] in cross_points and [maxx, maxy] in cross_points and [
        maxy, minx] in cross_points):
        return 0, 0, 0, 0

    return minx, miny, maxx, maxy


def cross(rect, new_rect):
    x11 = rect['x1']
    x21 = rect['x2']
    y11 = rect['y1']
    y21 = rect['y2']
    x12 = new_rect['x1']
    x22 = new_rect['x2']
    y12 = new_rect['y1']
    y22 = new_rect['y2']

    points = []
    if not (x21 < x12 or x11 > x22 or y21 < y12 or y11 > y22):
        if x11 > x12 and x21 < x22:
            if y11 < y12:
                if y21 < y22:
                    points.append([x11, y12])
                    points.append([x21, y12])
                elif y21 != y22:
                    points.append([x11, y12])
                    points.append([x11, y22])
                    points.append([x12, y12])
                    points.append([x12, y22])
            elif y11 != y12:
                points.append([x11, y22])
                points.append([x21, y22])
        elif x11 < x12 and x21 > x22:
            if y11 < y12:
                if y21 < y22:
                    points.append([x12, y21])
                    points.append([x22, y21])
                elif y21 != y22:
                    points.append([x12, y11])
                    points.append([x12, y22])
                    points.append([x22, y11])
                    points.append([x22, y22])
            elif y11 != y12:
                points.append([x12, y11])
                points.append([x22, y11])
        elif x11 < x12:
            if y21 < y22:
                if y11 < y12:
                    points.append([x12, y21])
                    points.append([x21, y12])
                elif y11 != y12:
                    points.append([x12, y11])
                    points.append([x12, y21])
            if y21 > y22:
                if y11 < y12:
                    points.append([x12, y11])
                    points.append([x21, y22])
                elif y11 != y12:
                    points.append([x21, y21])
                    points.append([x21, y22])
        elif x21 > x22:
            if y21 < y22:
                if y11 < y12:
                    points.append([x11, y12])
                    points.append([x21, y21])
                elif y11 != y12:
                    points.append([x22, y11])
                    points.append([x22, y21])
            if y21 > y22:
                if y11 < y12:
                    points.append([x11, y12])
                    points.append([x11, y22])
                elif y11 != y12:
                    points.append([x11, y22])
                    points.append([x22, y11])
    return points


def find_cross(rects, new_rect, cross_points):
    for rect in rects:
        points = cross(rect, new_rect)
        if points:
            cross_points += points
    return cross_points


def main():
    try:
        data = filereader("input.txt")
    except FileNotFoundError:
        print("Error: File does not exist.")
    except Exception:
        print("Error: Something was going wrong while reading the file.")

    data = data.split()
    area = {'width': int(data[0]), 'height': int(data[1])}
    rects = []
    cross_points = []
    if not len(data[2:]) % 4:
        number_of_rects = int(len(data[2:]) / 4)
        i = 2
        for rect in range(number_of_rects):
            new_rect = {'x1': int(data[i]), 'y1': int(data[i + 1]), 'x2': int(data[i + 2]), 'y2': int(data[i + 3])}
            cross_points = find_cross(rects, new_rect, cross_points)
            cross_points.append([int(data[i]), int(data[i + 1])])
            cross_points.append([int(data[i + 2]), int(data[i + 3])])
            cross_points.append([int(data[i]), int(data[i + 3])])
            cross_points.append([int(data[i + 2]), int(data[i + 1])])
            rects.append(new_rect)
            i += 4

    try:
        root = Tk()
        canv = Canvas(root, width=area['width'], height=area['height'], bg="white",
                      cursor="pencil")
        canv, xx, yy = placer(canv, area, rects)
        x1, y1, x2, y2 = find_closest_lines(area, xx, yy, cross_points, 350, 350)
        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            canv = Canvas(root, width=area['width'], height=area['height'], bg="yellow",
                          cursor="pencil")
            canv, xx, yy = placer(canv, area, rects)
        else:
            canv.create_rectangle(x1, y1, x2, y2, fill="yellow")
        canv.pack()
        root.mainloop()
    except CoordinateException as e:
        e.print_()


main()
