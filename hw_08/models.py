import messages as m

students = {}


def create_student(last_name, first_name, class_name):
    student = {
        "last_name": last_name,
        "first_name": first_name,
        "class_name": class_name,
        "grade_storage": {}
    }
    return student


def add_student(student):
    global students
    student_name = student["last_name"]
    if students.get(student_name, None):
        raise Exception(m.EXCEPTION_STUDENT_EXISTS_MSG)
    students[student_name] = student
    print(m.ADDED_STUDENT_MSG)


def edit_student(student):
    global students
    student_name = student["last_name"]
    if not students.get(student_name, None):
        print(m.STUDENT_ADD_ON_EDIT_NO_EXISTS_MSG)
        add_student(student)
    students[student_name] = student
    print(m.EDITED_STUDENT_MSG)


def add_grade(student_name, subject, grade):
    global students
    current_student = students.get(student_name, None)
    if current_student:
        current_subject = current_student["grade_storage"].get(subject, None)
        if current_subject:
            current_subject.append(grade)
        else:
            current_student["grade_storage"][subject] = [grade,]
        print(m.ADDED_GRADE_MSG)
    else:
        print(m.STUDENT_NOT_FOUND_MSG)


def search_by_last_name(last_name, lesson=None):
    global students
    found_student = students.get(last_name, None)
    if found_student:
        student_grade_storage = found_student["grade_storage"]
        if lesson:
            return student_grade_storage.get(lesson, m.GRADES_NOT_FOUND_MSG)
        return student_grade_storage if student_grade_storage else m.GRADES_NOT_FOUND_MSG
    return m.STUDENT_NOT_FOUND_MSG
