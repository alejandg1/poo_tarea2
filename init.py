from visualize import visualize, califications_filter
from create import qualify, new_career, new_student, new_subject, new_teacher, exist_obj, new_university
from functions import msg
from tabulate import tabulate

options = {
    1: "new University",
    2: "new career",
    3: "new teacher",
    4: "new student",
    5: "new subject",
    6: "qualify",
    7: "visualize subjects",
    8: "visualize careers",
    9: "visualize teachers",
    10: "visualize students",
    11: "visualize ratings",
    12: "filter ratings",
    13: "exit"
}

headers = ["Choose an option: "]
content = []
for i in options:
    content.append([f"{i}) {options[i]}"])
list = tabulate(content, headers, tablefmt="rounded_grid")


def main():
    while True:
        print(list)
        opt = input(">> ")
        match opt:
            case "1":
                new_university()

            case "2":
                new_career()

            case "3":
                new_teacher()

            case "4":
                new_student()

            case "5":
                new_subject()

            case "6":
                qualify()

            case "7":
                visualize("subjects.json", "non_person")

            case "8":
                visualize("careers.json", "non_person")

            case "9":
                visualize("teachers.json", "person")

            case "10":
                visualize("students.json", "person")

            case "11":
                visualize("califications.json", "calification")

            case "12":
                califications_filter()

            case "13":
                break

            case _:
                msg("opcion invalida", "error")


main()
