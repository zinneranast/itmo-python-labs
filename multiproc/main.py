from multiprocessing.dummy import Pool as ThreadPool
import random


def file_reader(file_path):
    with open(file_path, 'r') as txtfile:
        read_data = txtfile.readlines()
    return read_data


def file_writer(file_path):
    with open(file_path, 'w') as txtfile:
        for i in range(2000000):
            txtfile.write(str(random.randint(1, 100)) + " " + str(random.randint(1, 100)) + "\n")


def f1(a, b):
    return a - b


def f2(a, b):
    return a + b


def parse_line(line):
    a, b = line.split()
    a = int(a)
    b = int(b)
    return f1(a, b)


def main():
    #file_writer('input.txt')
    data = file_reader('input.txt')
    pool = ThreadPool()
    after_f1 = pool.map(lambda line: parse_line(line), data)

    def after_f2(array):
        temp = pool.map(lambda i: f2(array[i], array[i - 1]), range(1, len(array), 2))
        if len(array) % 2 != 0:
            temp += array[-1:]
        return temp

    while len(after_f1) > 1:
        after_f1 = after_f2(after_f1)

    pool.close()
    pool.join()

    return after_f1[len(after_f1) - 1]


print(main())
