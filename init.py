import functions
import colorama
from tabulate import tabulate

options = {
    1: "new University",
    2: "new career",
    3: "new teacher",
    4: "new student",
    6: "new subject",
    7: "qualify",
    8: "visualize subjects",
    9: "visualize careers",
    10: "visualize teachers",
    11: "visualize students",
    12: "visualize ratings",
    13: "filter ratings",
    14: "exit"
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
                functions.clear(3)
            case "2":
                functions.new_career()
                functions.clear(3)
            case "3":
                functions.new_teacher()
                functions.clear(3)
            case "4":
                functions.new_student()
                functions.clear(3)
            case "6":
                functions.new_subject()
                functions.clear(3)
            case "7":
                functions.qualify()
                functions.clear(3)
            case "8":
                functions.visualize("subjects.json", "non_person")
                functions.clear(5)
            case "9":
                functions.visualize("careers.json", "person")
                functions.clear(5)
            case "10":
                functions.visualize("teachers.json", "person")
                functions.clear(5)
            case "11":
                functions.visualize("students.json", "person")
                functions.clear(5)
            case "12":
                functions.visualize("califications.json", "calification")
                functions.clear(5)
            case "13":
                functions.califications_filter()
                functions.clear(5)
            case "14":
                break

            case _:
                print(colorama.Fore.RED+"opción invalida"+colorama.Fore.RESET)
                functions.clear(3)


main()
