import csv


def get_data(filename):
    try:
        data_csv = []
        with open(filename, mode='r', encoding='UTF-8', newline='') as file:
            reader = list(csv.reader(file, delimiter=','))
            for row in reader[1:]:
                data_csv.append(row)
        return data_csv
    except:
        print("Ocurrio un error al leer datos del archivo", filename)


def set_data(filename, data):
    try:
        with open(filename, mode='w', encoding='UTF-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(get_head(filename))
            writer.writerows(data)
    except: 
        print("Ocurrio un error al guardar datos en el archivo", filename)

def get_head(filename):
    head = None
    match filename:
        case 'students.csv':
            head = ['Id','Legajo','Nombre','Carrera']
        case 'subjects.csv':
            head = ['Id','Codigo','Nombre','Carrera']
        case 'careers.csv':
            head = ['Id','Codigo','Nombre','Facultad']
        case 'notes.csv':
            head = ['Id','Materia','Legajo','Nota', 'Fecha']
    return head

