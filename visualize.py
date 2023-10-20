import functions


def califications_filter():
    subjects = functions.read_json("subjects.json")
    if (functions.exist_obj(subjects)):
        print("Choose the ID of the subject: ")
        functions.print_table(subjects, "non_person")
        election: int = (input(">> "))
        if (functions.is_an(election)):
            election = int(election)
            found: bool = functions.check_id(election, subjects)
            califications = functions.read_json("califications.json")
            if (found):
                subject = subjects[election-1]
                table = [
                    element for element in califications if element['subject'] == subject['name']]
                # for element in califications:
                #     if (element["subject"] == subject["name"]):
                #         table.append(element)
                functions.print_table(table, "calification")
            else:
                functions.msg("not found", "error")
        else:
            functions.msg("enter numbers", "info")


def visualize(file, tipo):
    data = functions.read_json(file)
    functions.print_table(data, tipo)
