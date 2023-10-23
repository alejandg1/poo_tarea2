from functions import read_json, write_json, exist_obj, print_table, is_an, check_id, msg
from clases import Student, Career, calification, Subject, Teacher, University, acta


def new_student() -> None:
    name = input("enter student name: ")
    last_name = input("enter student lastname: ")
    student = Student(name, last_name)
    file = read_json("students.json")
    file.append(student.__repr__())
    write_json("students.json", file)


def new_university() -> None:
    name = input("enter university name: ")
    university = University(name)
    file = read_json("university.json")
    file.append(university.__repr__())
    write_json("university.json", file)


def new_career() -> None:
    universities = read_json("university.json")
    if (exist_obj(universities)):
        print("Choose the ID of the university of this career")
        print_table(universities, "non_person")
        election: int = (input(">> "))
        if (is_an(election)):
            election = int(election)
            found: bool = check_id(election, universities)
            if (found):
                uni = universities[election-1]
                name = input("enter career name: ")
                faculty = input("enter a faculty name: ")
                career = Career(name, faculty, uni)
                file = read_json("careers.json")
                file.append(career.__repr__())
                write_json("careers.json", file)
            else:
                msg("university not found", "error")
        else:
            msg("enter numbers", "info")
    else:
        msg("oh there are no universities", "info")


def new_subject() -> None:
    teachers = read_json("teachers.json")
    if (exist_obj(teachers)):
        print("Choose the ID of the teacher of this subject")
        print_table(teachers, "person")
        election: int = (input(">> "))
        if (election.isdigit()):
            election = int(election)
            found: bool = check_id(election, teachers)
            if (found):
                teacher = teachers[election-1]
                name = input("enter subject name: ")
                paralell = input("enter subject paralell: ")
                level = input("enter subject level: ")
                start = input("enter the subject start: ")
                end = input("enter the subject end: ")
        # instanciar
                subject = Subject(name, teacher, level, paralell, start, end)
                file = read_json("subjects.json")
                file.append(subject.__repr__())
                write_json("subjects.json", file)
            else:
                msg("teacher not found", "error")
    else:
        msg("enter numbers", "info")


def new_teacher():
    name = input("enter the teacher's name: ")
    last_name = input("enter the teacher's lastname: ")
    teacher = Teacher(name, last_name)
    file = read_json("teachers.json")
    file.append(teacher.__repr__())
    write_json("teachers.json", file)


def qualify():
    students = read_json("students.json")
    if (len(students) < 1):
        msg("oh, there are no students")
    else:
        print("Choose the ID of the student to be graded")
        print_table(students, "person")
        election: int = (input(">> "))
        if (election.isdigit()):
            election = int(election)
            found: bool = check_id(election, students)
            if (found):
                student = students[election-1]
                subjects = read_json("subjects.json")
                if (exist_obj(subjects)):
                    print("Choose the ID of the subject to be graded: ")
                    print_table(subjects, "non_person")
                    election: int = (input(">> "))
                    if (is_an(election)):
                        election = int(election)
                        found: bool = check_id(election, subjects)
                        subject = subjects[election-1]
                        if (found):
                            paralel = input("enter the paralell: ")
                            asistance = input(
                                "enter the asistance of the student: ")
                            N1 = (input("enter grade N1: "))
                            N2 = (input("enter grade N2: "))
                            EX1 = (input("enter grade EX1: "))
                            N3 = (input("enter grade N3: "))
                            N4 = (input("enter grade N4: "))
                            EX2 = (input("enter grade EX2: "))
                            RE = (input("enter grade RE: "))
                            continu = is_an(N1) and is_an(N2) and is_an(
                                EX1) and is_an(N3) and is_an(N4) and is_an(EX2) and is_an(RE)
                            if (continu):
                                N1 = int(N1)
                                N2 = int(N2)
                                EX1 = int(EX1)
                                N3 = int(N3)
                                N4 = int(N4)
                                EX2 = int(EX2)
                                RE = int(RE)
                                name = student["name"] + \
                                    " "+student["lastname"]
                                calific = calification(
                                    subject["name"], paralel, name, asistance, N1, N2, EX1, N3, N4, EX2, RE)
                                file = read_json("califications.json")
                                file.append(calific.__repr__())
                                write_json("califications.json", file)
                            else:
                                msg("enter numbers", "error")
                        else:
                            msg("subject not found", "error")
                    else:
                        msg("enter numbers", "error")
                else:
                    msg("oh, there are not subjects", "info")
            else:
                msg("not found", "error")
        else:
            msg("enter numbers", "error")


def generate_acta():
    subjects = read_json("subjects.json")
    if (exist_obj(subjects)):
        print("Choose the ID of the subject to generate a report: ")
        print_table(subjects, "non_person")
        election: int = (input(">> "))
        if (is_an(election)):
            election = int(election)
            found: bool = check_id(election, subjects)
            subject = subjects[election-1]
            if (found):
                calification = read_json("calification.json")
                if (exist_obj(calification)):
                    new_acta = acta(calification.end)
                    for each in calification:
                        if (calification.subject == subject.name):
                            new_acta.add_detail(calification)
                    new_acta.print()
                else:
                    msg("califications are empty")
        else:
            msg("enter numbers", "error")
    else:
        msg("oh, no subjects found", "info")
