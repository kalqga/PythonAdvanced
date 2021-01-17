n = int(input())


def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines


student_grades_lines = input_to_list(n)


def avg(values):
    return sum(values) / len(values)


students_grades = {}

for line in student_grades_lines:
    student, grade = line.split(' ')
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(float(grade))

for (student, grades) in students_grades.items():
    grades_string = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
    avg_grade = 0
    print(f"{student} -> {grades_string} (avg: {avg(grades):.2f})")
