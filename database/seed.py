import argparse
from create_base import session
from create_tables import Teacher, Group, Student, Subject, Mark
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--action', type=str, required=True)
parser.add_argument('-m', '--models', type=str, required=True)
parser.add_argument('-n', '--name', type=str, nargs='*')
parser.add_argument('-i', '--id', type=int,)
parser.add_argument('-gi', '--group_id', type=int,)
parser.add_argument('-gn', '--group_number', type=int,)
parser.add_argument('-ti', '--teacher_id', type=int,)
parser.add_argument('-sbi', '--subject_id', type=int,)
parser.add_argument('-sti', '--student_id', type=int,)
parser.add_argument('-mk', '--mark', type=int,)
parser.add_argument('-d', '--date', type=int, nargs=3)

args = parser.parse_args()

def find_table(model: str):
    model = model.lower()
    if model == "teacher":
        return Teacher
    elif model == "student":
        return Student
    elif model == "group":
        return Group
    elif model == "subject":
        return Subject
    elif model == "mark":
        return Mark

def show_list(table):
    users = session.query(table).all()
    if table is Student:
        for user in users:
            print(user.id, user.student_name, user.group_id)
    elif table is Teacher:
        for user in users:
            print(user.id, user.teacher_name)
    elif table is Group:
        for user in users:
            print(user.id, user.group_number)
    elif table is Subject:
        for user in users:
            print(user.id, user.student_name, user.subject_id)
    elif table is Mark:
        for user in users:
            print(user.id, user.student_id, user.subject_id, user.mark, user.date_of)

def create(table, args):
    if table is Student:
        st_name = " ".join(args.name)
        user = table(id=args.id, student_name=st_name, group_id=args.group_id)
    elif table is Teacher:
        tr_name = " ".join(args.name)
        user = table(id=args.id, teacher_name=tr_name)
    elif table is Group:
        user = table(id=args.id, group_number=args.group_number)
    elif table is Subject:
        user = table(id=args.id, subject_name=args.name[0], teacher_id=args.teacher_id)
    elif table is Mark:
        date = datetime(int(args.date[0]), int(args.date[1]), int(args.date[2]))
        user = table(id=args.id, student_id=args.student_id, subject_id=args.subject_id, mark=args.mark, date_of=date)
    session.add(user)
    session.commit()


def update(table, args):
    data = session.query(table).get(args.id)
    if args.name:
        name = " ".join(args.name)
        if table == Student:
            data.student_name = name
        elif table == Teacher:
            data.teacher_name = name
        elif table == Subject:
            data.subject_name = name
    elif args.group_id:
        if table == Student:
            data.group_id = args.group_id
    elif args.student_id:
        if table == Mark:
            data.student_id = args.student_id
    elif args.subject_id:
        if table == Mark:
            data.subject_id = args.subject_id
    elif args.teacher_id:
        if table == Subject:
            data.teacher_id = args.teacher_id
    elif args.mark:
        if table == Mark:
            data.mark = args.mark
    elif args.date:
        if table == Mark:
            date = datetime(int(args.date[0]), int(args.date[1]), int(args.date[2]))
            data.date_of = date
    session.add(data)
    session.commit()

def remove(table, args):
    data = session.query(table).get(args.id)
    session.delete(data)
    session.commit()


if __name__== "__main__":
    table = find_table(args.models)
    if args.action == 'create':
        print(f"{args}, create")
        create(table, args)
    elif args.action == 'update':
        print(f"{args}, update") 
        update(table, args)   
    elif args.action == 'remove':
        print(f"{args}, remove")
        remove(table, args)
    elif args.action == 'list':
        print(f"{args}, list")
        show_list(table)