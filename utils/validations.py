from datetime import datetime
import re


""" --------------------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR OPCIÓN INGRESADA PARA LOS MENÚS ############################### """
""" --------------------------------------------------------------------------------------------------------"""

def validate_menu_option():
    # Funcion para validar la opcion ingresada por el usuario en el menú. Debe ser un numero entre 1 y 5.
    option = input("Seleccione una opción: ")
    while not option.isdigit() or int(option) < 1 or int(option) > 6:
        print("Se ha ingresado una opción inválida. La opción no puede estar vacía o ser 0. Solo se permiten valores numéricos, intente nuevamente.")
        option = input("Seleccione una opción: ")
    return int(option)


""" --------------------------------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR QUE EL VALOR INGRESADO SEA ENTERO MAYOR A 0 ############################### """
""" --------------------------------------------------------------------------------------------------------------------"""

def validate_int_input(message, error):
    # Funcion para validar que el input sea un numero entero mayor a 0
    int_value = input(message)
    while not int_value.isdigit() or int(int_value) < 0:
        print(error)
        int_value = input(message)
    return int(int_value)

""" -------------------------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR QUE EL VALOR INGRESADO SEA UN STRING ############################### """
""" -------------------------------------------------------------------------------------------------------------"""
def validate_string_input(message, error):
    # función para validar que el input sean caracteres excepto dígitos y que no sea vacío
    string_value = input(message).strip()
    # Expresión regular: rechaza si hay números (0-9)
    while string_value == "" or re.search(r"\d", string_value):
        print(error)
        string_value = input(message).strip()
    return string_value

""" ------------------------------------------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR QUE EL CODIGO EXISTA EN LA LISTA ############################### """
""" ------------------------------------------------------------------------------------------------------------------------------"""

def validate_identifier(data_list, identifier):
    # Funcion para validar que el id no se encuentre registrado en la lista de estudiantes o materias
    for data in data_list:
        if str(data["codigo"]) == str(identifier):
            return True
    return False

""" ------------------------------------------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR QUE EL CODIGO EXISTA EN LA LISTA ############################### """
""" ------------------------------------------------------------------------------------------------------------------------------"""

def validate_identifier_by_subject(data_list, identifier):
    # Funcion para validar que el id no se encuentre registrado en la lista de estudiantes o materias
    for data in data_list:
        if str(data["materia"]) == str(identifier):
            return True
    return False

""" ------------------------------------------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR QUE EL LEGAJO DE ALUMNO EXISTA ############################### """
""" ------------------------------------------------------------------------------------------------------------------------------"""

def validate_identifier_by_student(data_list, identifier):
    # Funcion para validar que el id no se encuentre registrado en la lista de estudiantes o materias
    for data in data_list:
        if str(data["legajo"]) == str(identifier):
            return True
    return False

""" --------------------------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR QUE LA OPCIÓN DE CONTINUAR SEA VÁLIDA ############################### """
""" --------------------------------------------------------------------------------------------------------------"""

def validate_continue(message):
    # Funcion para validar que la opcion ingresada sea 's' o 'n'
    option = str(input(message)).lower()
    while option not in ('s', 'n'): # validamos que la opcion ingresada sea 's' o 'n'
        print("\nOpción inválida. Debe ser 's' (sí) o 'n' (no).\n")
        option = str(input(message)).lower()
    return option


""" --------------------------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR EXISTENCIA POR LEGAJO O IDENTIFICADOR ############################### """
""" --------------------------------------------------------------------------------------------------------------"""

def validate_existing(data_list, code_value):
    # Funcion para validar que exista al menos una nota registrada para el alumno indicado
    for data in data_list:
        if str(data["legajo"]) == str(code_value):
            return True
    return False


""" ----------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR EXISTENCIA DE CARRERA ############################### """
""" ----------------------------------------------------------------------------------------------"""

def validate_existing_career(careers, career_name):
    # función para verificar que una carrera está registrada en careers
    for career in careers:
        if career["nombre"].upper() == career_name.upper():
            return True
    return False

""" ----------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR EXISTENCIA DE NOTA ############################### """
""" ----------------------------------------------------------------------------------------------"""

def validate_existing_note(notes, subject_code, student_identifier, note_value, date_value):
    # función para verificar que una nota está registrada en notes
    for note in notes:
        if int(note["materia"]) == int(subject_code) and int(note["legajo"]) == int(student_identifier) and int(note["nota"]) == int(note_value) and note["fecha"].upper() == date_value.upper():
            return True
    return False

""" ----------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR EXISTENCIA DE ESTUDIANTE ############################### """
""" ----------------------------------------------------------------------------------------------"""

def validate_existing_student(students, student_name):
    # función para verificar que un estudiante está registrada en students
    for student in students:
        if student["nombre"].upper() == student_name.upper():
            return True
    return False

""" ----------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR EXISTENCIA DE MATERIA ############################### """
""" ----------------------------------------------------------------------------------------------"""

def validate_existing_subject(subjects, subject_name, subject_degree):
    # función para verificar que una materia está registrada en subjects
    for subject in subjects:
        if subject["nombre"].upper() == subject_name.upper() and int(subject["carrera"]) == int(subject_degree):
            return True
    return False


""" ----------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR QUE EL VALOR INGRESADO SEA UNA FECHA ################ """
""" ----------------------------------------------------------------------------------------------"""

def validate_date_input(message, error):
    # función para validar que el input sean caracteres excepto dígitos y que no sea vacío
    string_value = input(message).strip()
    date_valid = False
    while not date_valid:
        try:
            # valida que la fecha es valida y tiene el formato correcto
            datetime.strptime(string_value, r'%Y-%m-%d')
            date_valid = True
        except ValueError: 
            print(error)
            string_value = input(message).strip()
            date_valid = False
    return string_value

""" ----------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR QUE EXISTA LA FECHA EN NOTA ######################### """
""" ----------------------------------------------------------------------------------------------"""

def validate_date(notes, note_date):
    # función para verificar que una fecha está registrada en notas
    for note in notes:
        if note[4] == note_date:
            return True
    return False

