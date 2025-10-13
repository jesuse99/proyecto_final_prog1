import csv
import os

def get_data(filename):
    data_csv = []
    with open(filename, mode='r', encoding='UTF-8', newline='') as file:
        reader = list(csv.reader(file, delimiter=','))
        for row in reader[1:]:
            data_csv.append(row)
    return data_csv

def set_data(filename, data):
    # Preservar la primera línea (encabezado) del CSV si existe.
    header_line = None
    if os.path.exists(filename):
        try:
            with open(filename, mode='r', encoding='UTF-8', newline='') as f:
                first = f.readline()
                if first:
                    header_line = first.rstrip('\n')
        except Exception:
            header_line = None

    with open(filename, mode='w', encoding='UTF-8', newline='') as file:
        # Si había una cabecera original, la reescribimos tal cual (preservando formato)
        if header_line:
            file.write(header_line + "\n")
        writer = csv.writer(file)
        writer.writerows(data)




