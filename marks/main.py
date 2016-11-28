# get list of students (for subject)
def get_students(subject):
    return list(map(lambda student: tuple(student)[0], tuple(subject)[1]))


# get list of students and their final exam marks
def get_exam_mark(data):
    if tuple(data)[1] != 0:
        if tuple(tuple(data)[0])[1] / tuple(data)[1] > 0.8:
            return (tuple(tuple(data)[0])[0], '5')
        elif tuple(tuple(data)[0])[1] / tuple(data)[1] >= 0.6:
            return (tuple(tuple(data)[0])[0], '4')
        elif tuple(tuple(data)[0])[1] / tuple(data)[1] >= 0.4:
            return (tuple(tuple(data)[0])[0], '3')
        else:
            return (tuple(tuple(data)[0])[0], '2')
    else:
        return (tuple(tuple(data)[0])[0], '2')


# get list of unique students
def get_unique_students(data):
    try:
        unique_students = get_students(list(data)[0])
        map(lambda k:
            list(map(lambda student:
                     unique_students.append(student) if not student in unique_students else student,
                     get_students(k))),
            list(data)[1:])
        return unique_students
    except:
        return None


# check if student has a mark on the subject or not
def check_if_student_in_list(data):
    try:
        return tuple(list(data)[0])[1]
    except:
        return 0


# get list of students and their sum of marks
def get_results(data):
    if not get_unique_students(data) is None:
        return list(map(lambda student:
                        (student, sum(list(map(
                            lambda subject:
                            check_if_student_in_list(filter(lambda x:
                                                            tuple(x)[0] == student, tuple(subject)[1])),
                            list(data))))),
                        get_unique_students(data)))


# get result list of pairs 'student - mark'
def get_final_marks(data):
    return list(map(lambda result:
                    get_exam_mark((result,
                                   # get max mark on the subject
                                   max(list(map(lambda x:
                                                tuple(x)[1], get_results(data)))))),
                    get_results(data)))


def main(input_data):
    return get_final_marks(input_data)


print(main([('Мат. Анализ', [('Иванов', 15), ('Петров', 13), ('Сидоров', 2), ('Васильев', 10), ('Жуков', 6)]),
            ('Алгебра', [('Петров', 24), ('Иванов', 20), ('Васильев', 11), ('Жуков', 12)]),
            ('Логика', [('Иванов', 10), ('Петров', 15), ('Сидоров', 6), ('Жуков', 15)])]))
