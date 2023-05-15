from sqlalchemy import func, desc

from create_base import session
from create_tables import Teacher, Group, Student, Subject, Mark


def query_1():
    q = session.query(Student.student_name, func.round(func.avg(Mark.mark), 2).label('avg_grade'))\
        .select_from(Mark).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return q

def query_2():
    q = session.query(Student.student_name, func.round(func.avg(Mark.mark), 2)\
        .label('avg_grade'), Subject.subject_name).select_from(Student).join(Mark)\
        .join(Subject).filter(Subject.subject_name=='English').group_by(Student.student_name, Subject.subject_name)\
        .order_by(desc('avg_grade')).limit(1).all()
    return q


def query_3():
    q = session.query(Group.group_number\
        .label("Group`s number"), Subject.subject_name\
        .label("Subject`s name"), func.round(func.avg(Mark.mark), 2).label('avg_grade'))\
        .select_from(Student).filter(Student.group_id==Group.id).join(Mark)\
        .filter(Mark.student_id==Student.id).join(Subject)\
        .filter(Mark.subject_id==Subject.id)\
        .filter(Subject.subject_name=='Algebra').group_by(Group.group_number, Subject.subject_name)\
        .all()
    return q


def query_4():
    q = session.query(func.round(func.avg(Mark.mark), 2).label("Average mark")).all()
    return q


def query_5():
    q = session.query(Teacher.teacher_name.label("Teacher`s name"), Subject.subject_name\
        .label("Subject name")).select_from(Teacher).join(Subject)\
        .filter(Subject.teacher_id==Teacher.id).filter(Teacher.teacher_name=='Brent Rodriguez').all()
    return q


def query_6():
    q = session.query(Student.student_name.label("Student`s name"), Group.group_number\
        .label("Group`s number")).select_from(Student).join(Group)\
        .filter(Group.id==Student.group_id).filter(Group.group_number==2).all()
    return q


def query_7():
    q = session.query(Group.group_number\
        .label("Group`s number"), Student.student_name\
        .label("Student`s name"), Subject.subject_name\
        .label("Subject`s name"), Mark.mark\
        .label("Mark"), Mark.date_of\
        .label("Date")).select_from(Student).join(Group)\
        .filter(Group.id==Student.group_id).join(Mark)\
        .filter(Student.id==Mark.student_id).join(Subject)\
        .filter(Subject.id==Mark.subject_id)\
        .filter(Group.group_number==2).filter(Subject.subject_name=="Algebra").all()
    return q


def query_8():
    q = session.query(Teacher.teacher_name.label("Teacher`s name"), Subject.subject_name\
        .label("Subject`s name"), func.round(func.avg(Mark.mark), 2).label("Average mark"))\
        .select_from(Teacher).join(Subject)\
        .filter(Subject.teacher_id==Teacher.id).join(Mark).filter(Mark.subject_id==Subject.id)\
        .group_by(Teacher.teacher_name, Subject.subject_name).all()
    return q


def query_9():
    q = session.query(Student.student_name\
        .label("Student`s name"), Subject.subject_name\
        .label("Subject`s name"))\
        .select_from(Student).join(Mark)\
        .filter(Mark.student_id==Student.id).filter(Student.student_name=="Nicholas Obrien")\
        .group_by(Subject.subject_name, Student.student_name).all()
    return q


def query_10():
    pass
    q = session.query(Student.student_name.label("Student`s name"),Teacher.teacher_name\
        .label("Teacher`s name"), Subject.subject_name\
        .label("Subject`s name"))\
        .select_from(Student).join(Mark)\
        .filter(Mark.subject_id==Subject.id).join(Subject).filter(Subject.id==Mark.subject_id)\
        .join(Teacher).filter(Teacher.id==Subject.teacher_id)\
        .filter(Teacher.teacher_name == 'Brent Rodriguez').filter(Student.student_name == 'Kevin Powell')\
        .all()
    return q


def add_query_1():
    pass
    q = session.query(Student.student_name.label("Student`s name"),Teacher.teacher_name\
        .label("Teacher`s name"), func.round(func.avg(Mark.mark), 2).label("Average mark"))\
        .select_from(Student).join(Mark)\
        .filter(Mark.student_id==Student.id).join(Subject).filter(Subject.id==Mark.subject_id)\
        .join(Teacher).filter(Teacher.id==Subject.teacher_id)\
        .filter(Teacher.teacher_name == 'Brent Rodriguez').filter(Student.student_name == 'Monique Blair')\
        .group_by(Student.student_name, Teacher.teacher_name).all()
    return q


def add_query_2():
    pass
    q = session.query(Group.group_number\
        .label("Group`s number"), Student.student_name.label("Student`s name")\
        ,Subject.subject_name.label("Subject`s name")\
        ,Mark.mark.label("Mark")\
        ,func.max(Mark.date_of).label("Max date"))\
        .select_from(Student).join(Mark)\
        .filter(Mark.student_id==Student.id).join(Group).filter(Group.id==Student.group_id)\
        .join(Subject).filter(Subject.id==Mark.subject_id)\
        .filter(Subject.subject_name == 'Geometry').filter(Group.group_number == 2)\
        .group_by(Group.group_number, Student.student_name, Subject.subject_name, Mark.mark)\
        .all()
    return q

if __name__ == '__main__':
    print(155*"-")
    print(query_1())
    print(155*"-")
    print(query_2())
    print(155*"-")
    print(query_3())
    print(155*"-")
    print(query_4())
    print(155*"-")
    print(query_5())
    print(155*"-")
    print(query_6())
    print(155*"-")
    print(query_7())
    print(155*"-")
    print(query_8())
    print(155*"-")
    print(query_9())
    print(155*"-")
    print(query_10())
    print(155*"-")
    print(add_query_1())
    print(155*"-")
    print(add_query_2())
    print(155*"-")

