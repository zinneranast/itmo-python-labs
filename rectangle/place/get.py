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
    for rect in rects:
        if rect['x1'] > area['width'] or rect['x2'] > area['width'] or rect['y1'] > area['height'] or rect['y2'] > area[
            'height']:
            raise CoordinateException
        canv.create_rectangle(rect['x1'], rect['y1'], rect['x2'], rect['y2'], outline="red")
    return canv


def fill(canv, rects, x, y, color="yellow"):
    print(y, "<", rects[1]['y1'])
    if rects[1]['x2'] > rects[0]['x2'] and rects[1]['y2'] > rects[0]['y2']:
        if y > rects[1]['y2'] and y < rects[1]['y1'] and x < rects[0]['x2'] and x > rects[0]['x1']:
            x1=rects[0]['x1']
            x2=rects[0]['y1']
            y1=rects[1]['x2']
            y2=rects[1]['y2']
            canv.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
    return canv


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
        canv = placer(canv, area, rects)
        canv = fill(canv, rects, 350, 460)
        canv.pack()
        root.mainloop()
    except CoordinateException as e:
        e.print()


main()
