from functions import print_table


class University:
    __id = 1

    def __init__(self, name: str) -> None:
        University.__id += 1
        self.name = name
        self.__id = University.__id

    @property
    def id(self):
        return self.__id

    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class User:
    def __init__(self, nombre: str, last_name: str) -> None:
        self.name = nombre
        self.lastname = last_name


class Career:
    __id = 0

    def __init__(self, name: str, Faculty: str, university: University = "UNEMI") -> None:
        Career.__id += 1
        self.__id = Career.__id
        self.name = name
        self.faculty = Faculty
        self.university = university

    @property
    def id(self):
        return self.__id

    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
            "faculty": self.faculty,
            "university": self.university,
        }


class Teacher(User):
    __id = 0

    def __init__(self, nombre: str, apellido: str) -> None:
        super().__init__(nombre, apellido)
        Teacher.__id += 1
        self.__id = Teacher.__id
        self.subject = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    @property
    def id(self):
        return self.__id

    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
        }


class Subject:
    __id = 0

    def __init__(self, name: str, teacher: Teacher, level: int, paralell: str,
                 start: str, end: str) -> None:

        Subject.__id += 1
        self.__id = Subject.__id
        self.name = name
        self.paralell = paralell
        self.teacher = teacher
        self.level = level
        self.start = start
        self.end = end

    @property
    def id(self):
        return self.__id

    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
            "teacher": self.teacher,
            "level": self.level,
            "paralell": self.level,
            "start": self.level,
            "end": self.level,
        }


class Student(User):
    __id = 0

    def __init__(self, nombre: str, apellido: str) -> None:
        super().__init__(nombre, apellido)
        Student.__id += 1
        self.__id = Student.__id
        self.subjects = []

    def enroll(self, subject: Subject) -> None:
        if (subject):
            self.subjects.append(subject)
    # matricular carrera

    def enroll_career(self, career: Career) -> None:
        if (career):
            self.career = (career)

    @property
    def id(self):
        return self.__id

    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
        }


class calification:
    __id = 0

    def __init__(self, subject: str, paralell: str, student: str, assistance: int, N1: float, N2: float, EX1: float, N3: float, N4: float, EX2: float, RE: float = 0) -> None:
        calification.__id += 1
        self.__id = calification.__id
        self.subject = subject
        self.student = student
        self.paralell = paralell
        self.assistance = assistance
        self.N1 = N1
        self.N2 = N2
        self.EX1 = EX1
        self.P1 = N1 + N2
        self.N3 = N3
        self.N4 = N4
        self.EX2 = EX2
        self.P2 = N3+N4
        self.RE = RE
        self.FINAL = self.P1+self.P2+self.RE

    @property
    def id(self):
        return self.__id

    def __repr__(self):
        return {
            "id": self.id,
            "subject": self.subject,
            "paralell": self.paralell,
            "student": self.student,
            "N1": self.N1,
            "N2": self.N2,
            "EX1": self.EX1,
            "P1": self.P1,
            "N3": self.N3,
            "N4": self.N4,
            "EX2": self.EX2,
            "P2": self.P2,
            "RE": self.RE,
            "FINAL": self.FINAL,
        }


class acta:
    __id = 0

    def __init__(self, subject: object, date: str):
        acta.__id += 1
        self.ID = acta.id
        self.subject = subject
        self.teacher = subject.teacher
        self.date: date

    def add_detail(self, iterable: object):
        calification = det_acta(iterable)
        self.califications.append(calification.__repr__())

    def __repr__(self) -> str:
        return {
            "subject": self.subject,
            "teacher": self.teacher,
            "date": self.date,
            "califications": self.califications
        }

    def print(self):
        print(f"subject: {self.subject}")
        print(f"teacher: {self.teacher}")
        print(f"date: {self.date}")
        print_table(self.califications, "calification")


class det_acta:
    def __init__(self, calification: object) -> None:
        self.calification = calification

    def __repr__(self):
        return {
            "student": self.calification.student,
            "N1": self.calification.N1,
            "N2": self.calification.N2,
            "EX1": self.calification.EX1,
            "P1": self.calification.P1,
            "N3": self.calification.N3,
            "N4": self.calification.N4,
            "EX2": self.calification.EX2,
            "P2": self.calification.P2,
            "RE": self.calification.RE,
            "FINAL": self.calification.FINAL,

        }
