from clases import Student, Career, calification, Subject, Teacher, University


def new_student() -> Student:
    name = input("Ingrese el nombre del estudiante: ")
    last_name = input("Ingrese el apellido del estudiante: ")
    student = Student(name, last_name)
    return student


def new_teacher():
    name = input("Ingrese el nombre del estudiante: ")
    last_name = input("Ingrese el apellido del estudiante: ")
    teacher = Student(name, last_name)
    return teacher


def add_calification():
    pass
