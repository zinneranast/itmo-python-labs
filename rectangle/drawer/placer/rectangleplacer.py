from rectangle.drawer.filereader.txtfilereader import read
from rectangle.drawer.filler.drawer import *
import uuid


def place():
    try:
        data = read("input.txt")
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
