from clases import Student, Career, calification, Subject, Teacher, University
from tabulate import tabulate
import json


def new_student() -> Student:
    name = input("Ingrese el nombre del estudiante: ")
    last_name = input("Ingrese el apellido del estudiante: ")
    student = Student(name, last_name)
    return student


def new_teacher() -> Teacher:
    name = input("Ingrese el nombre del estudiante: ")
    last_name = input("Ingrese el apellido del estudiante: ")
    teacher = Teacher(name, last_name)
    return teacher


# NOTE: posiblemente innecesario por q no se requiere actualizar datos
# def search(array: list, id: int) -> dict:
#     found = {}
#     if (array.__le__ > 0):
#         for element in array:
#             if (element.id == id):
#                 found = element
#     return found

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
            [element['id'], element['name'], element['last_name']])
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
        return json.loads(file.read())


def write_json(file: str, content: object) -> None:
    with open(f"./data/{file}", "w") as file:
        file.write(content)


def qualify():
    students = read_json("students.json")
    if (len(students) < 0):
        print("Oh, there are no students")
    else:
        # escojer estudiante a calificar
        print("Choose the ID of the student to be graded")
        print_table(students)
        election: int = int(input(">> "))
        found: bool = check_id(election, students)
        if (found):
            # escoger materia a calificar
            subjects = read_json("subjects.json")
            print("Choose the ID of the subject to be graded")
            print_table(subjects)
            election: int = int(input(">> "))
            found: bool = check_id(election, subjects)
            if (found):
                # TODO: continuar con el ingreso de datos
                pass
            else:
                print("subject not found")

        else:
            print("no found")
