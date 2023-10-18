from clases import Student, Career, calification, Subject, Teacher, University
import colorama
from tabulate import tabulate
import json
import os
import time


def clear():
    time.sleep(3)
    os.system("clear")


def new_student() -> None:
    name = input("enter student name: ")
    last_name = input("enter student lastname: ")
    student = Student(name, last_name)
    file = read_json("students.json")
    file.append(student.__repr__())
    write_json("students.json", file)


def new_university() -> None:
    name = input("enter unviersity name: ")
    university = University(name)
    file = read_json("university.json")
    file.append(university.__repr__())
    write_json("university.json", file)


def new_career() -> None:
    universities = read_json("university.json")
    if (len(universities) < 1):
        print(colorama.Fore.GREEN +
              "Oh, there are no universities"+colorama.Fore.RESET)
    else:
        print("Choose the ID of the student to be graded")
        # ingreso de profesor
        headers = ["ID", "Nombre"]
        body = []
        for i in universities:
            body.append([i["id"], i["name"]])
        list = tabulate(body, headers, tablefmt="rounded_grid")
        print(list)
        election: int = int(input(">> "))
        found: bool = check_id(election, universities)
        if (found):
            uni = universities[election-1]
            name = input("enter career name")
            faculty = input("enter a faculty name")
        # instanciar
            career = Career(name, faculty, uni)
            file = read_json("careers.json")
            file.append(career.__repr__())
            write_json("careers.json", file)
        else:
            print(colorama.Fore.RED+"university not found"+colorama.Fore.RESET)


def new_subject() -> None:
    students = read_json("students.json")
    if (len(students) < 1):
        print(colorama.Fore.GREEN+"Oh, there are no teachers"+colorama.Fore.RESET)
    else:
        teachers = read_json("teachers.json")
        if (len(teachers) > 1):
            print("Choose the ID of the teacher of this subject")

            # ingreso de profesor
            print_table(teachers)
            election: int = int(input(">> "))
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
                write_json("students.json", file)
            else:
                print(colorama.Fore.RED+"teacher not found"+colorama.Fore.RESET)
        else:
            print(colorama.Fore.GREEN +
                  "Oh, there are no teachers"+colorama.Fore.RESET)


def new_teacher() -> Teacher:
    name = input("enter the teacher's name: ")
    last_name = input("enter the teacher's lastname: ")
    teacher = Teacher(name, last_name)
    file = read_json("teachers.json")
    file.append(teacher.__repr__())
    write_json("teachers.json", file)


def filter_data():
    pass


def check_id(id: int, iterable: object) -> bool:
    found: bool = False
    for element in iterable:
        if (id == element["id"]):
            found = True
    return found


def print_table(iterable):
    table = []
    headers = ["ID", "Name", "Last name"]
    for element in iterable:
        table.append(
            [element['id'], element['name'], element['lastname']])
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


def qualify():
    students = read_json("students.json")
    if (len(students) < 1):
        print(colorama.Fore.GREEN+"Oh, there are no students"+colorama.Fore.RESET)
    else:
        # escojer estudiante a calificar
        print("Choose the ID of the student to be graded")
        print_table(students)
        election: int = int(input(">> "))
        found: bool = check_id(election, students)
        if (found):
            # escoger materia a calificar
            student = students[election-1]
            subjects = read_json("subjects.json")
            if (len(subjects) > 1):
                print("Choose the ID of the subject to be graded: ")
                print_table(subjects)
                election: int = int(input(">> "))
                found: bool = check_id(election, subjects)
                subject = subjects[election]
                if (found):
                    try:
                        paralel = input("enter the paralell: ")
                        asistance = input(
                            "enter the asistance of the student: ")
                        N1 = int(input("enter grade N1: "))
                        N2 = int(input("enter grade N2: "))
                        EX1 = int(input("enter grade EX1: "))
                        N3 = int(input("enter grade N3: "))
                        N4 = int(input("enter grade N4: "))
                        EX2 = int(input("enter grade EX2: "))
                        calific = calification(
                            subject.name, paralel, (student.name+" "+student.last_name), asistance, N1, N2, EX1, N3, N4, EX2)
                        json = read_json("califications.json")
                        json.append(calific)
                        write_json("califications.json", json)
                    except TypeError:
                        print("enter numbers")
                else:
                    print("subject not found")
            else:
                print(colorama.Fore.GREEN +
                      "Oh, there are no subjects"+colorama.Fore.RESET)

        else:
            print("no found")
