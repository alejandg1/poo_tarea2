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
    7: "exit"
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
                break

            case _:
                print(colorama.Fore.RED+"opción invalida"+colorama.Fore.RESET)
        functions.clear()


main()
