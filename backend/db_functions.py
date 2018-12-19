import os


def read_db(name):
    """
     Lee un csv, el formato de este es nombre, 0, 1,2 ...31 donde cada
     columna representa un modulo en donde es 1 si está disponible y 0 en
     otro caso
    """
    if os.path.exists(name):
        with open(name, "r") as file:
            file.readline()
            for i in file:
                yield i.strip().split(",")
    else:
        return []


def get_disponible_modules(name, response):
    for i in read_db(name):
        person_name = i[0]
        disponible_modules = [int(i) for i in i[1:]]
        response[person_name] = disponible_modules

def save_bd(dictionary_model):
    pass


def add_new_person(path, name, modules):
    if not exist_person(path, name):
        with open(path, "a+") as file:
            line = name + "," + modules + "\n"
            file.write(line)
            return True
    return False


def exist_person(path, name):
    return any(map(lambda x: name == x[0], read_db(path)))

