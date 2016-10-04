import csv
from operator import itemgetter


def csvfileredear(file_path):
    with open(file_path, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        return [row for row in reader]


def get_marks(student_marks):
    marks = [int(mark) for mark in student_marks]
    marks += [2] * (5 - len(marks))
    marks.insert(0, [(sum(mark for mark in marks)) / len(marks)])
    return marks


def main():
    data = csvfileredear('marks.csv')
    groups = {}
    for row in data:
        marks = get_marks(row[2:])
        if not row[1] in groups:
            groups[row[1]] = []
        students = groups.get(row[1])
        students.append({'student': row[0], 'avg': marks[0], 'marks': marks[1:]})

    for group_key, group_value in groups.items():
        print('Группа%s:' % group_key)
        for student in sorted(group_value, key=itemgetter('avg')):
            print(student['student'], student['avg'], *student['marks'])


main()
