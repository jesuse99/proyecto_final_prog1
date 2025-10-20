import random
from functions.validations import validate_identifier

""" -------------------------------------------------------------------------------------------------------"""
""" ############################### FUNCIÓN PARA DEFINIR POSICIÓN EN LISTA ############################### """
""" -------------------------------------------------------------------------------------------------------"""

def set_position(data_list):
    # funcion para definir la posición en la que se ingresó la información
    if len(data_list) == 0:
        position = 1
    else:
        position = int(data_list[-1][0])+1
    return position

""" -------------------------------------------------------------------------------------------------------------------------------"""
""" ############################### FUNCIÓN PARA OBTENER UN ID ALEATORIO QUE NO EXISTA EN LA LISTA ############################### """
""" -------------------------------------------------------------------------------------------------------------------------------"""

def set_identifier(data_list):
    identifier = str(random.randint(1, 9999)) #numero aleatorio generado del 1 al 9999
    while validate_identifier(data_list, identifier):
        # validamos que el identifier no se encuentre registrado en el sistema
        identifier = str(random.randint(1, 9999))
    return identifier

""" ------------------------------------------------------------------------------------------------------"""
""" ############################### OBTENER INFORMACIÓN POR LEGAJO/CODIGO ############################### """
""" ------------------------------------------------------------------------------------------------------"""
def get_by_record(data_list, identifier):
    # funcion para obtener un estudiante por su legajo
    for data in data_list:
        if data[1] == str(identifier):
            return data
    return None

""" ------------------------------------------------------------------------------------------------------"""
""" ############################### OBTENER NOTA DE ESTUDIANTE POR LEGAJO ############################### """
""" ------------------------------------------------------------------------------------------------------"""

def get_notes_by_student_record(notes, identifier):
    # funcion para obtener las notas de un estudiante por su legajo
    student_notes = []
    for note in notes:
        if note[2] == str(identifier):
            student_notes.append(note)
    return student_notes


def get_students_by_career(students, identifier):
    # funcion para obtener las notas de un estudiante por su legajo
    students_career = []
    for student in students:
        if student[3] == str(identifier):
            students_career.append(student)
    return students_career
""" ---------------------------------------------------------------------------------------------------------"""
""" ############################### OBTENER NOTAS POR LEGAJO Y ID DE MATERIA ############################### """
""" ---------------------------------------------------------------------------------------------------------"""

def get_notes_by_subject_student(notes, subject_id, student_id):
    # funcion para obtener las notas de una materia por su ID
    subject_notes = []
    for note in notes:
        if note[1] == str(subject_id) and note[2] == str(student_id):
            subject_notes.append(note)
    return subject_notes


""" ------------------------------------------------------------------------------------------"""
""" ############################### OBTENER PROMEDIO DE NOTAS ############################### """
""" ------------------------------------------------------------------------------------------"""

def get_average(notes):
    # función para obtener el promedio de unas notas pasadas como parametro
    total = 0
    amount = 0
    for note in notes:
        total += int(note[3])
        amount += 1
    if total > 0:
        average = total / amount
        return average
    return None

