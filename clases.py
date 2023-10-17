class University:
    __id = 0

    def __init__(self, name: str) -> None:
        self.name = name
        University.__id += 1
        self.id = University.__id

    @property
    def id(self):
        return self.__id


class User:
    __id = 0

    def __init__(self, nombre: str, last_name: str) -> None:
        User.__id += 1
        self.id = User.__id
        self.nombre = nombre
        self.last_name = last_name

    @property
    def id(self):
        return self.__id


class Career:
    __id = 0

    def __init__(self, name: str, Faculty: str, university: University) -> None:
        self.__id = Career.__id
        self.name = name
        self.faculty = Faculty
        self.university = university

    @property
    def id(self):
        return self.__id


class Teacher(User):
    __id = 0

    def __init__(self, nombre: str, apellido: str) -> None:
        super().__init__(nombre, apellido)
        self.__id = Teacher.__id
        self.subject = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def qualify(self):
        pass


class Subject:
    __id = 0

    def __init__(self, name: str, teacher: Teacher, level: int, paralell: str,
                 start: str, end: str) -> None:

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


class Student(User):
    def __init__(self, nombre: str, apellido: str) -> None:
        super().__init__(nombre, apellido)
        self.califications = []
        self.subjects = []

    def enroll(self, subject: Subject) -> None:
        if (subject):
            self.subjects.append(subject)
            self.califications.append(
                calification(subject.name, subject.paralell, 0, 0, 0, 0, 0, 0, 0, 0))

    # matricular carrera
    def enroll_career(self, career: Career) -> None:
        if (career):
            self.career = (career)


class calification:
    __id = 0

    def __init__(self, subject: str, paralell: str, student: str, assistance: int, N1: float, N2: float, EX1: float, N3: float, N4: float, EX2: float, RE: float = 0) -> None:
        calification.__id += 1
        self.id = calification.__id
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

    @property
    def id(self):
        return self.__id


class Grade:
    pass
