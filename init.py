import functions
opciones = {
    1: "qualify",
    2: "new student",
    3: "new teacher"
}


def main():
    try:
        print("ingrese el numero de la función a ejecutar")
        for opcion in opciones:
            print(f"{opcion}) {opciones[opcion]}")
        option = int(input(">> "))
        if (option <= len(opciones)):
            match opciones[option]:
                case "qualify":
                    functions.qualify()
                case "new student":
                    pass
    except TypeError:
        print("ingrese números")


main()
