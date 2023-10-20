from tabulate import tabulate
import colorama
import json
import os


def is_an(value) -> bool:
    is_an: bool = False
    resp = value.isdigit()
    if (resp):
        is_an = True
    return (is_an)


def clear():
    print("Presione una tecla para continuar...")
    input(">> ")
    sys = os.name
    if (sys == "nt"):
        os.system("cls")
    else:
        os.system("clear")


def check_id(id: int, iterable: object) -> bool:
    found: bool = False
    for element in iterable:
        if (id == element["id"]):
            found = True
    return found


def print_table(iterable: object, entit: str):
    table = []
    match entit:
        case("person"):
            headers = ["ID", "Name", "Last name"]
            for element in iterable:
                table.append(
                    [element['id'], element['name'], element['lastname']])
        case("non_person"):
            headers = ["ID", "Name"]
            for element in iterable:
                table.append(
                    [element['id'], element['name']])
        case("calification"):
            headers = ["ID", "subject", "student", "P1", "P2", "RE", "FINAL"]
            for element in iterable:
                table.append([element['id'], element["subject"], element['student'],
                             element["P1"], element["P2"], element["RE"], element["FINAL"]])
    list = tabulate(table, headers, tablefmt="rounded_grid")
    print(list)


def obtain_element(id: int, iterable: object):
    found: object = {}
    for element in iterable:
        if (id == element["id"]):
            found = element
    return found


def read_json(file: str) -> None:
    try:
        with open(f"./data/{file}", "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"error to read file {e} ")
    except FileNotFoundError as e:
        print(f"file not found. {e}")


def write_json(file: str, content: object) -> None:
    try:
        with open(f"./data/{file}", "w") as file:
            content = json.dumps(content)
            file.write(content)
    except Exception as e:
        print(f"error to write file. {e} ")
    except FileNotFoundError as e:
        print(f"file not found. {e}")


def exist_obj(obj):
    exist = False
    if (len(obj) > 0):
        exist = True
    return exist


def msg(msg: str, tipe: str):
    match tipe:
        case ("error"):
            print(colorama.Fore.RED + msg + colorama.Fore.RESET)
        case ("info"):
            print(colorama.Fore.BLUE + msg + colorama.Fore.RESET)
