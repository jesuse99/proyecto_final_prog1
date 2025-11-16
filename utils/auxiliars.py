from utils.validations import validate_identifier, validate_identifier_by_student
import random

""" -------------------------------------------------------------------------------------------------------"""
""" ############################### FUNCIÓN PARA DEFINIR POSICIÓN EN LISTA ############################### """
""" -------------------------------------------------------------------------------------------------------"""

def set_position(data_list):
    # funcion para definir la posición en la que se ingresó la información
    if len(data_list) == 0:
        position = 1
    else:
        position = len(data_list)+1
    return position

""" -------------------------------------------------------------------------------------------------------------------------------"""
""" ############################### FUNCIÓN PARA OBTENER UN ID ALEATORIO QUE NO EXISTA EN LA LISTA ############################### """
""" -------------------------------------------------------------------------------------------------------------------------------"""

def set_identifier(data_list):
    identifier = random.randint(1, 9999) # numero aleatorio generado del 1 al 9999
    # validamos que el identifier no se encuentre registrado en el sistema
    return identifier if not validate_identifier(data_list, identifier) else set_identifier(data_list)

""" -------------------------------------------------------------------------------------------------------------------------------"""
""" ############################### FUNCIÓN PARA OBTENER UN LEGAJO ALEATORIO QUE NO EXISTA EN LA LISTA ############################### """
""" -------------------------------------------------------------------------------------------------------------------------------"""

def set_identifier_by_student(data_list):
    identifier = random.randint(1, 9999) # numero aleatorio generado del 1 al 9999
    # validamos que el identifier no se encuentre registrado en el sistema
    return identifier if not validate_identifier_by_student(data_list, identifier) else set_identifier(data_list)

""" ------------------------------------------------------------------------------------------------------"""
""" ############################### OBTENER INFORMACIÓN POR LEGAJO ############################### """
""" ------------------------------------------------------------------------------------------------------"""
def get_by_student(data_list, identifier):
    # funcion para obtener un estudiante por su legajo
    for data in data_list:
        if str(data["legajo"]) == str(identifier):
            return data
    return None

""" ------------------------------------------------------------------------------------------------------"""
""" ############################### OBTENER INFORMACIÓN POR CODIGO ############################### """
""" ------------------------------------------------------------------------------------------------------"""
def get_by_subject(data_list, identifier):
    # funcion para obtener un estudiante por su legajo
    for data in data_list:
        if str(data["codigo"]) == str(identifier):
            return data
    return None

""" ------------------------------------------------------------------------------------------------------"""
""" ############################### OBTENER INFORMACIÓN POR CARRERA ############################### """
""" ------------------------------------------------------------------------------------------------------"""
def get_by_career(data_list, identifier):
    # funcion para obtener un estudiante por su legajo
    for data in data_list:
        if str(data["codigo"]) == str(identifier):
            return data
    return None

""" ---------------------------------------------------------------------------------------------------------"""
""" ############################### OBTENER MATERIAS POR ID DE CARRERA  ############################### """
""" ---------------------------------------------------------------------------------------------------------"""

def get_subjects_by_career(subjects, career_id):
    # funcion para obtener las notas de una materia por su ID
    subjects_career = []
    for subject in subjects:
        if int(subject["carrera"]) == int(career_id):
            subjects_career.append(subject)
    return subjects_career


""" ------------------------------------------------------------------------------------------------------"""
""" ############################### OBTENER NOTA DE ESTUDIANTE POR LEGAJO ############################### """
""" ------------------------------------------------------------------------------------------------------"""

def get_notes_by_student_record(notes, identifier):
    # funcion para obtener las notas de un estudiante por su legajo
    student_notes = []
    for note in notes:
        if str(note["legajo"]) == str(identifier):
            student_notes.append(note)
    return student_notes


def get_students_by_career(students, identifier):
    # funcion para obtener las notas de un estudiante por su legajo
    students_career = []
    for student in students:
        if str(student["carrera"]) == str(identifier):
            students_career.append(student)
    return students_career

""" ---------------------------------------------------------------------------------------------------------"""
""" ############################### OBTENER NOTAS POR ID DE MATERIA ############################### """
""" ---------------------------------------------------------------------------------------------------------"""

def get_notes_by_subject(notes, subject_id):
    # funcion para obtener las notas de una materia por su ID
    subject_notes = []
    for note in notes:
        if str(note["materia"]) == str(subject_id):
            subject_notes.append(note)
    return subject_notes


""" ---------------------------------------------------------------------------------------------------------"""
""" ############################### OBTENER NOTAS POR LEGAJO Y ID DE MATERIA ############################### """
""" ---------------------------------------------------------------------------------------------------------"""

def get_notes_by_subject_student(notes, subject_id, student_id):
    # funcion para obtener las notas de una materia por su ID
    subject_notes = []
    for note in notes:
        if str(note["materia"]) == str(subject_id) and str(note["legajo"]) == str(student_id):
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
        total += int(note["nota"])
        amount += 1
    if total > 0:
        average = total / amount
        return average
    return None

