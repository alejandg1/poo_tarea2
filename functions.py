from clases import Student, Career, calification, Subject, Teacher, University
import colorama
from tabulate import tabulate
import json
import os
import time
import platform


def is_an(value) -> bool:
    is_an: bool = False
    resp = value.isdigit()
    if (resp):
        is_an = True
    return (is_an)


def clear(t):
    sys = platform.system()
    time.sleep(t)
    if (sys == "Windows"):
        os.system("cls")
    else:
        os.system("clear")


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
            # instanciar
                career = Career(name, faculty, uni)
                file = read_json("careers.json")
                file.append(career.__repr__())
                write_json("careers.json", file)
            else:
                print(colorama.Fore.RED+"university not found"+colorama.Fore.RESET)
        else:
            print(colorama.Fore.RED+"enter numbers"+colorama.Fore.RESET)

    else:
        print(colorama.Fore.GREEN +
              "Oh, there are no universities"+colorama.Fore.RESET)


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
                print(colorama.Fore.RED+"teacher not found"+colorama.Fore.RESET)
    else:
        print(colorama.Fore.RED+"enter numbers"+colorama.Fore.RESET)


def new_teacher() -> Teacher:
    name = input("enter the teacher's name: ")
    last_name = input("enter the teacher's lastname: ")
    teacher = Teacher(name, last_name)
    file = read_json("teachers.json")
    file.append(teacher.__repr__())
    write_json("teachers.json", file)


def check_id(id: int, iterable: object) -> bool:
    found: bool = False
    for element in iterable:
        if (id == element["id"]):
            found = True
    return found


def print_table(iterable: object, entit: str):
    table = []
    match entit:
        case("person"):
            headers = ["ID", "Name", "Last name"]
            for element in iterable:
                table.append(
                    [element['id'], element['name'], element['lastname']])
        case("non_person"):
            headers = ["ID", "Name"]
            for element in iterable:
                table.append(
                    [element['id'], element['name']])
        case("calification"):
            headers = ["ID", "subject", "student", "P1", "P2", "RE", "FINAL"]
            for element in iterable:
                table.append([element['id'], element["subject"], element['student'],
                             element["P1"], element["P2"], element["RE"], element["FINAL"]])
    list = tabulate(table, headers, tablefmt="rounded_grid")
    print(list)


def obtain_element(id: int, iterable: object):
    found: object = {}
    for element in iterable:
        if (id == element["id"]):
            found = element
    return found


def read_json(file: str) -> None:
    with open(f"./data/{file}", "r") as file:
        return json.load(file)


def write_json(file: str, content: object) -> None:
    with open(f"./data/{file}", "w") as file:
        content = json.dumps(content)
        file.write(content)


def exist_obj(obj):
    exist = False
    if (len(obj) > 0):
        exist = True
    return exist


def qualify():
    students = read_json("students.json")
    if (len(students) < 1):
        print(colorama.Fore.GREEN+"Oh, there are no students"+colorama.Fore.RESET)
    else:
        # escojer estudiante a calificar
        print("Choose the ID of the student to be graded")
        print_table(students, "person")
        election: int = (input(">> "))
        if (election.isdigit()):
            election = int(election)
            found: bool = check_id(election, students)
            if (found):
                # escoger materia a calificar
                student = students[election-1]
                subjects = read_json("subjects.json")
                if (exist_obj(subjects)):
                    print("Choose the ID of the subject to be graded: ")
                    print_table(subjects, "non_person")
                    election: int = (input(">> "))
                    if (is_an(election) and check_id(election, subjects)):
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
                                name = student["name"]+" "+student["lastname"]
                                calific = calification(
                                    subject["name"], paralel, name, asistance, N1, N2, EX1, N3, N4, EX2, RE)
                                file = read_json("califications.json")
                                file.append(calific.__repr__())
                                write_json("califications.json", file)
                            else:
                                print(colorama.Fore.RED +
                                      "enter numbers" + colorama.Fore.RESET)
                        else:
                            print("subject not found")
                    else:
                        print(colorama.Fore.RED +
                              "incorrect data" + colorama.Fore.RESET)

                else:
                    print(colorama.Fore.GREEN +
                          "Oh, there are no subjects"+colorama.Fore.RESET)

            else:
                print("no found")
        else:
            print(colorama.Fore.RED + "enter numbers" + colorama.Fore.RESET)


def visualize(file, tipo):
    data = read_json(file)
    print_table(data, tipo)


def califications_filter():
    subjects = read_json("subjects.json")
    if (exist_obj(subjects)):
        print("Choose the ID of the subject: ")
        print_table(subjects, "non_person")
        election: int = (input(">> "))
        if (is_an(election)):
            election = int(election)
            found: bool = check_id(election, subjects)
            califications = read_json("califications.json")
            if (found):
                subject = subjects[election-1]
                table = []
                for element in califications:
                    if (element["subject"] == subject["name"]):
                        table.append(element)
                print_table(table, "calification")
            else:
                print(colorama.Fore.RED + "not found" + colorama.Fore.RESET)
        else:
            print(colorama.Fore.RED + "enter numbers" + colorama.Fore.RESET)
