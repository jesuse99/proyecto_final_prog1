

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
    # Funcion para validar que el input sea un string no vacio y que solo contenga letras
    string_value = str(input(message))
    while string_value == "" or not string_value.isalpha():
        print(error)
        string_value = str(input(message))
    return string_value

""" ------------------------------------------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR QUE EL LEGAJO DE ALUMNO O EL CODIGO DE MATERIA EXISTA ############################### """
""" ------------------------------------------------------------------------------------------------------------------------------"""

def validate_identifier(data_list, identifier):
    # Funcion para validar que el id no se encuentre registrado en la lista de estudiantes o materias
    for data in data_list:
        if data[1] == str(identifier):
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


""" ---------------------------------------------------------------------------------------------------------------------"""
""" ############################### VALIDAR EXISTENCIA DE NOTA PARA UN ALUMNO POR LEGAJO ############################### """
""" ---------------------------------------------------------------------------------------------------------------------"""


def validate_existing_note(notes, student_identifier):
    # Funcion para validar que exista al menos una nota registrada para el alumno indicado
    for note in notes:
        if note[2] == student_identifier:
            return True
    return False
