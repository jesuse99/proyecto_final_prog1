import json

def get_data(filename):
    try:
        data_json = []
        with open(f'data/{filename}.json', mode='r', encoding='UTF-8', newline='') as file:
            data_json = json.load(file)
        return data_json
    except:
        print("Ocurrio un error al leer datos del archivo", filename)

def set_data(filename, data):
    try:
        with open(f'data/{filename}.json', mode='w', encoding='UTF-8', newline='') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except:
        print("Ocurrio un error al leer datos del archivo", filename)
