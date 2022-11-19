'''📝 Example codes used in readme.md

✨ Run and check the output
'''

# Args


def add(a, b):
    return a + b


print(add(2, 3))


def add_numbers(*args):
    return sum(args)


print(add_numbers(2, 3, 4, 5, 6, 7, 8, 9, 11))

# Kwargs
student_marks = {}


def add_student_marks(name, marks):
    student_marks[name] = marks


add_student_marks('Rahul', 80)
add_student_marks('Arun', 85)
print(student_marks)

# modified with kwargs


def add_student_marks(**marks):
    for name, marks in marks.items():
        student_marks[name] = marks


add_student_marks(Rahul=80, Arun=85, Kishore=90, Anju=91)
print(student_marks)
