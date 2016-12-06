from multiprocessing.dummy import Pool as ThreadPool
import random


def file_reader(file_path):
    with open(file_path, 'r') as txtfile:
        read_data = txtfile.readlines()
    return read_data


def file_writer(file_path):
    with open(file_path, 'w') as txtfile:
        for i in range(2000000):
            print(random.randint(1, 100), random.randint(1, 100), file=txtfile)


def f1(a, b):
    return a - b


def f2(a, b):
    return a + b


def parse_line(line):
    a, b = line.split()
    a = int(a)
    b = int(b)
    return f1(a, b)


def after_f2(after_f1, i):
    if i % 2 == 0:
        after_f1[i + 2] = f2(f2(after_f1[i], after_f1[i + 1]), after_f1[i + 2])
    return after_f1


def main():
    data = file_reader('input.txt')
    pool = ThreadPool()
    after_f1 = pool.map(lambda line: parse_line(line), data)
    pool.map(lambda i: after_f2(after_f1, i), range(len(after_f1) - 2))
    pool.close()
    pool.join()

    return after_f1[len(after_f1) - 1]


print(main())
