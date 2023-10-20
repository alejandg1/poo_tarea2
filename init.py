import functions
import colorama
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
                functions.new_university()

            case "2":
                functions.new_career()

            case "3":
                functions.new_teacher()

            case "4":
                functions.new_student()

            case "5":
                functions.new_subject()

            case "6":
                functions.qualify()

            case "7":
                functions.visualize("subjects.json", "non_person")

            case "8":
                functions.visualize("careers.json", "non_person")

            case "9":
                functions.visualize("teachers.json", "person")

            case "10":
                functions.visualize("students.json", "person")

            case "11":
                functions.visualize("califications.json", "calification")

            case "12":
                functions.califications_filter()

            case "13":
                break

            case _:
                print(colorama.Fore.RED+"opción invalida"+colorama.Fore.RESET)
        functions.clear()


main()
