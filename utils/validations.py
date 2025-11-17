from datetime import datetime
import re


""" --------------------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR OPCIÓN INGRESADA PARA LOS MENÚS ############################### """
""" --------------------------------------------------------------------------------------------------------"""

def validate_menu_option():
    # Funcion para validar la opcion ingresada por el usuario en el menú. Debe ser un numero entre 1 y 7. 
    option = input("Seleccione una opción: ") # Solicito la opción al usuario

    if option.isdigit() and 1 <= int(option) <= 7: # Si la opción es un número entre 1 y 7, la retorno
        return int(option)
    
    # Si la opción no es válida, muestro un mensaje de error y solicito la opción nuevamente
    print("Se ha ingresado una opción inválida. La opción no puede estar vacía o ser 0. Solo se permiten valores numéricos, intente nuevamente.")
    return validate_menu_option() # Llamada recursiva para solicitar la opción nuevamente si la opción ingresada no es válida

""" --------------------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR OPCIÓN INGRESADA PARA LOS SUBMENÚS ############################### """
""" --------------------------------------------------------------------------------------------------------"""

def validate_submenu_option():
    # Funcion para validar la opcion ingresada por el usuario en los submenús. Debe ser un numero entre 1 y 5. 
    option = input("Seleccione una opción: ") # Solicito la opción al usuario

    if option.isdigit() and 1 <= int(option) <= 5: # Si la opción es un número entre 1 y 5, la retorno
        return int(option)
    
    # Si la opción no es válida, muestro un mensaje de error y solicito la opción nuevamente
    print("Se ha ingresado una opción inválida. La opción no puede estar vacía o ser 0. Solo se permiten valores numéricos, intente nuevamente.")
    return validate_submenu_option() # Llamada recursiva para solicitar la opción nuevamente si la opción ingresada no es válida


""" --------------------------------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR QUE EL VALOR INGRESADO SEA ENTERO MAYOR A 0 ############################### """
""" --------------------------------------------------------------------------------------------------------------------"""

def validate_int_input(message, error):
    # Funcion para validar que el input sea un numero entero mayor o igual a 0
    int_value = input(message) # Solicito el valor al usuario
    
    if int_value.isdigit() and int(int_value) >= 0: # Si el valor es un numero entero mayor o igual a 0, lo retorno
        return int(int_value)
    
    print(error) # Si el valor no es valido, muestro el mensaje de error
    return validate_int_input(message, error) # Llamada recursiva para solicitar el valor nuevamente si el valor ingresado no es valido

""" -------------------------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR QUE EL VALOR INGRESADO SEA UN STRING ############################### """
""" -------------------------------------------------------------------------------------------------------------"""
def validate_string_input(message, error):
    # función para validar que el input sean caracteres excepto dígitos y que no sea vacío
    string_value = input(message).strip() # Solicito el valor al usuario y elimino espacios en blanco al inicio y al final

    # Expresión regular: rechaza si hay números (0-9)
    if string_value != "" and not re.search(r"\d", string_value) and len(string_value) > 3: # Si el valor no está vacío y no contiene números, lo retorno
        return string_value
    
    print(error) # Si el valor ingresado no es valido, muestro el mensaje de error
    return validate_string_input(message, error) # Llamada recursiva para solicitar el valor nuevamente si el valor ingresado no es valido

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
    option = str(input(message)).lower() # Solicito la opción al usuario y la convierto a minúsculas
    
    if option in ('s', 'n'): # Si la opción es 's' o 'n', la retorno
        return option
        
    print("\nOpción inválida. Debe ser 's' (sí) o 'n' (no).\n") # Si la opción no es válida, muestro un mensaje de error
    return validate_continue(message) # Llamada recursiva para solicitar la opción nuevamente si la opción ingresada no es válida


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

def validate_existing_note(notes, subject_code, student_identifier, date_value):
    # función para verificar que una nota está registrada en notes
    for note in notes:
        if int(note["materia"]) == int(subject_code) and int(note["legajo"]) == int(student_identifier) and note["fecha"].upper() == date_value.upper():
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
    # función para validar que el input sea una fecha válida
    string_value = input(message).strip() # Solicito el valor al usuario y elimino espacios en blanco al inicio y al final
    
    try: # Intento convertir el valor a una fecha con el formato YYYY-MM-DD
        datetime.strptime(string_value, r'%Y-%m-%d') # Si el valor es una fecha válida, la retorno
        return string_value # Retorno la fecha válida
    
    except ValueError:  # Si el valor no es una fecha válida, muestro un error y vuelvo a pedir el valor
        print(error) # Muestro el mensaje de error
        return validate_date_input(message, error) # Llamada recursiva para solicitar el valor nuevamente si el valor ingresado no es valido

""" ----------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR QUE EXISTA LA FECHA EN NOTA ######################### """
""" ----------------------------------------------------------------------------------------------"""

def validate_date(notes, note_date):
    # función para verificar que una fecha está registrada en notas
    for note in notes:
        if note[4] == note_date:
            return True
    return False

