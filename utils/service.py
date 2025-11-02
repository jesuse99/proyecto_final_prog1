import json

def get_data(filename):
    try:
        data_json = []
        with open(filename, mode='r', encoding='UTF-8', newline='') as file:
            data_json = json.load(file)
        return data_json
    except IndentationError:
        print("Ocurrio un error al leer datos del archivo", filename)

def set_data(filename, data):
    try:
        with open(filename, mode='w', encoding='UTF-8', newline='') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except ZeroDivisionError:
        print("Ocurrio un error al leer datos del archivo", filename)
