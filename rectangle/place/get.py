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
        canv.create_rectangle(rect['x1'], rect['y1'], rect['x2'], rect['y2'], fill="white", outline="red")
    return canv


def fill(canv, x, y, color="yellow"):
    canv.create_line(x, y)
    return canv


def main():
    try:
        data = filereader("input.txt")
    except FileNotFoundError:
        print("Error: File does not exist.")
    except Exception:
        print("Error: Something was going wrong while reading the file.")

    data = data.split()
    area = {'width': data[0], 'height': data[1]}
    rects = []
    if not len(data[2:]) % 4:
        number_of_rects = int(len(data[2:]) / 4)
        i = 2
        for rect in range(number_of_rects):
            rects.append({'x1': data[i], 'y1': data[i + 1], 'x2': data[i + 2], 'y2': data[i + 3]})
            i += 4

    try:
        root = Tk()
        canv = Canvas(root, width=area['width'], height=area['height'], bg="lightblue",
                      cursor="pencil")
        canv = placer(canv, area, rects)
        canv = fill(canv, 300, 300)
        canv.pack()
        root.mainloop()
    except CoordinateException as e:
        e.print()


main()
