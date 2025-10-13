import csv

def get_data(filename):
    data_csv = []
    with open(filename, mode='r', encoding='UTF-8', newline='') as file:
        reader = list(csv.reader(file, delimiter=','))
        for row in reader[1:]:
            data_csv.append(row)
    return data_csv

def set_data(filename, data):
    with open(filename, mode='w', encoding='UTF-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)




