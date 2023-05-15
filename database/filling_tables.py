from create_base import session
from create_tables import Teacher, Group, Student, Subject, Mark
from datetime import datetime
import faker
from random import randint, choice


NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
SUBJECTS = [
    "Mathematics",
    "Physics",
    "English",
    "IT",
    "Economics",
    "Science",
    "Algebra",
    "Geometry",
]


def generate_fake_data(number_students, number_teachers) -> tuple():
    fake_students = []
    fake_teachers = []

    fake_data = faker.Faker()

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    return fake_students, fake_teachers


def prepare_data(students, teachers) -> tuple():
    for_teachers = []

    for teacher in teachers:
        for_teachers.append((teacher,))

    for_groups = []

    for group in range(1, NUMBER_GROUPS + 1):
        for_groups.append((group,))

    for_subjects = []  # для таблиці employees

    for sub in SUBJECTS:
        for_subjects.append((sub, randint(1, 5)))

    """
    Подібні операції виконаємо й у таблиці payments виплати зарплат. Приймемо, що виплата зарплати у всіх компаніях
    виконувалася з 10 по 20 числа кожного місяця. Вилку зарплат генеруватимемо в діапазоні від 1000 до 10000 у.о.
    для кожного місяця, та кожного співробітника.
    """
    for_students = []

    for student in students:
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_marks = []

    for st in range(1, NUMBER_STUDENTS + 1):
        for mark_count in range(randint(1, 20)):
            mark_date = datetime(2022, randint(1, 12), randint(1, 28)).date()
            for_marks.append((st, randint(1, 8), randint(1, 5), mark_date))

    return (for_students, for_teachers, for_groups, for_subjects, for_marks)


def insert_data_to_db(students, teachers, groups, subjects, marks) -> None:
    for group in groups:
        g = Group(group_number=group[0])
        print(g.id)
        session.add(g)
        session.flush()
        print(g.id)
    for teacher in teachers:
        t = Teacher(teacher_name=teacher[0])
        session.add(t)
        session.flush()
        print(t.id)
    for subject in subjects:
        sub = Subject(subject_name=subject[0], teacher_id=subject[1])
        session.add(sub)
        session.flush()
        print(sub.id)
    for student in students:
        st = Student(student_name=student[0], group_id=student[1])
        session.add(st)
        session.flush()
        print(st.id)
    for marking in marks:
        m = Mark(student_id=marking[0], subject_id=marking[1], mark=marking[2], date_of=marking[3])
        session.add(m)
        session.flush()
    


if __name__ == "__main__":
    students, teachers, groups, subjects, marks = prepare_data(
        *generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS)
    )
    insert_data_to_db(students, teachers, groups, subjects, marks)
    session.commit()