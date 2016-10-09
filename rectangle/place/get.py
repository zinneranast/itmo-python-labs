from tkinter import *


class CoordinateException(Exception):
    def print(self):
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


def placer(canv, area, rects):
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
        canv.create_rectangle(rect['x1'], rect['y1'], rect['x2'], rect['y2'], outline="red")
        canv.create_line(0, rect['y1'], rect['x1'], rect['y1'], fill="white")
        canv.create_line(rect['x1'], 0, rect['x1'], rect['y1'], fill="white")
        canv.create_line(area["width"], rect['y1'], rect['x2'], rect['y1'], fill="white")
        canv.create_line(rect['x2'], 0, rect['x2'], rect['y1'], fill="white")
        canv.create_line(rect['x1'], rect['y2'], 0, rect['y2'], fill="white")
        canv.create_line(rect['x1'], rect['y2'], rect['x1'], area["height"], fill="white")
        canv.create_line(rect['x2'], rect['y2'], area["width"], rect['y2'], fill="white")
        canv.create_line(rect['x2'], rect['y2'], rect['x2'], area["height"], fill="white")
    return canv, xx, yy


def find_closest_lines(area, xx, yy, x, y):
    minx = area["width"]
    for i in xx:
        if i < minx and i > x:
            minx = i
    miny = area["height"]
    for i in yy:
        if i < miny and i > y:
                miny = i
    maxx = 0
    for i in xx:
        if i > maxx and i < x:
                maxx = i
    maxy = 0
    for i in yy:
        if i > maxy and i < y:
                maxy = i
    return minx, miny, maxx, maxy


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
    if not len(data[2:]) % 4:
        number_of_rects = int(len(data[2:]) / 4)
        i = 2
        for rect in range(number_of_rects):
            rects.append({'x1': int(data[i]), 'y1': int(data[i + 1]), 'x2': int(data[i + 2]), 'y2': int(data[i + 3])})
            i += 4

    try:
        root = Tk()
        canv = Canvas(root, width=area['width'], height=area['height'], bg="white",
                      cursor="pencil")
        canv, xx, yy = placer(canv, area, rects)
        x1, y1, x2, y2 = find_closest_lines(area, xx, yy, 460, 460)
        canv.create_rectangle(x1, y1, x2, y2, fill="yellow")
        # canv = fill(canv, rects, 300, 300)
        canv.pack()
        root.mainloop()
    except CoordinateException as e:
        e.print()


main()
