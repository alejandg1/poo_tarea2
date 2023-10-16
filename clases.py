class University:
    def __init__(self, name: str) -> None:
        self.name = name


# class Faculty:
#     def __init__(self, name: str, university: University):
#         self.name = name
#         self.university = university
#
#
class User:
    def __init__(self, nombre: str, apellido: str) -> None:
        self.nombre = nombre
        self.apellido = apellido


class Career:
    def __init__(self, name: str, Faculty: str, university: University) -> None:
        self.name = name
        self.faculty = Faculty
        self.university = university


class Teacher(User):
    def __init__(self, nombre: str, apellido: str) -> None:
        super().__init__(nombre, apellido)


class Subject:
    def __init__(self, name: str, teacher: Teacher, level: int,
                 start: str, end: str) -> None:

        self.name = name
        self.teacher = teacher
        self.level = level
        self.start = start
        self.end = end


class calification:
    def __init__(self, subject: Subject, paralell: str, assistance: int, N1: float, N2: float, EX1: float, N3: float, N4: float, EX2: float, RE: float = 0) -> None:
        self.subject = subject
        self.paralell = paralell
        self.assistance = assistance
        self.N1 = N1
        self.N2 = N2
        self.EX1 = EX1
        self.P1 = (N1 + N2) + EX1
        self.N3 = N3
        self.N4 = N4
        self.EX2 = EX2
        self.P2 = (N3 + N4) + EX2
        self.RE = RE
        self.FINAL = (self.P1 + self.P2 + self.RE)


class Student(User):
    def __init__(self, nombre: str, apellido: str):
        super().__init__(nombre, apellido)
        self.califications = []

    def add_calification(self, calification: calification):
        self.califications.append(calification)


class Grade:
    pass
