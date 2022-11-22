from models import add_student, add_grade, create_student, edit_student, search_by_last_name
import messages as m

ROLE_TEACHER = "1"
ROLE_STUDENT = "2"
ROLE_EXIT = "3"

CMD_TEACHER_ADD_STUDENT = "1"
CMD_TEACHER_EDIT_STUDENT = "2"
CMD_TEACHER_ADD_GRADE = "3"
CMD_TEACHER_EXIT = "4"

def get_student_from_input():
        ln = input(m.ASK_LAST_NAME_MSG)
        fn = input(m.ASK_FIRST_NAME_MSG)
        cn = input(m.ASK_CLASS_NAME_MSG)
        return ln, fn, cn

def teacher_actions():
    global students
    while True:
        command = input(m.COMMAND_TEACHER_MSG)
        if command == CMD_TEACHER_ADD_STUDENT:
            new_student = create_student(*get_student_from_input())
            try:
                add_student(new_student)
            except Exception as e:
                print(e)
        elif command == CMD_TEACHER_EDIT_STUDENT:
            student = create_student(*get_student_from_input())
            edit_student(student)
        elif command == CMD_TEACHER_ADD_GRADE:
            student_name = input(m.ASK_LAST_NAME_MSG)
            subject_name = input(m.ASK_SUBJECT_MSG)
            grade = int(input(m.ASK_GRADE_MSG))
            add_grade(student_name, subject_name, grade)
        elif command == CMD_TEACHER_EXIT:
            print(m.ROLE_EXIT_MSG)
            break
        else:
            print(m.BAD_COMMAND_MSG)


def student_actions():
    global students
    student_name = input(m.ASK_LAST_NAME_MSG)
    grades = search_by_last_name(student_name)
    print(student_name, m.GRADES_FOR_STUDENT_MSG)
    print_grades(grades)

def print_grades(grades):
    for k, v in grades.items():
        print(f"{k}: {' '.join(str(i) for i in v)}")
    print("\n")

def run():
    print(m.HELLO_MSG)
    while True:
        role = input(m.LOGIN_MSG)
        if role == ROLE_TEACHER:
            teacher_actions()
        elif role == ROLE_STUDENT:
            student_actions()
        elif role == ROLE_EXIT:
            break
        else:
            print(m.BAD_COMMAND_MSG)
    print(m.END_MSG)

