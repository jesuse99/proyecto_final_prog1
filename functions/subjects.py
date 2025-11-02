from functions.validations import validate_string_input,validate_int_input, validate_identifier, validate_identifier_by_subject, validate_continue, validate_existing
from functions.auxiliars import set_position, set_identifier, get_by_subject, get_notes_by_subject_student, get_average
from utils.data import subjects, notes, careers
from utils.service import get_data, set_data


""" ---------------------------------------------------------------------------------------------"""
""" ############################### MOSTRAR MATERIAS REGISTRADOS ############################### """
""" ---------------------------------------------------------------------------------------------"""

def show_subjects(subjects, careers):
    # funcion para mostrar todos los estudiantes de la lista de estudiantes
    print("\n=== MOSTRAR MATERIAS ===\n")
    formatted_row = '{:<10} {:<24} {:<24} {:<28}'
    print("==============================================="*2)
    print(formatted_row.format("Codigo", "Nombre", "Carrera", "Facultad"))
    print("==============================================="*2)
    for subject in subjects:
        subject_code = subject["codigo"]
        subject_name = subject["nombre"]
        subject_career = subject["carrera"]

        # Buscar carrera por su codigo
        career_data = get_by_subject(careers, subject_career)

        if career_data:
            career_name = career_data["nombre"]
            career_building = career_data["facultad"]

            data_row = [subject_code, subject_name, career_name, career_building]
            print(formatted_row.format(*data_row))
    print()

""" --------------------------------------------------------------------------------"""
""" ############################### AÑADIR MATERIAS ############################### """
""" --------------------------------------------------------------------------------"""

subject_menu = """
=== AGREGAR MATERIAS ===
"""

def add_subject(subjects):
    # función para agregar una materia a la lista subjects
    print(subject_menu)
    subject_code = set_identifier(subjects)
    pos = set_position(subjects)   
    subject_name = validate_string_input("- Ingrese el nombre de la materia: ", "ERROR [!]Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    subject_degree = validate_int_input("- Ingrese el código de carrera de la materia:", "ERROR [!] Se ha ingresado un codigo inválido. El código solo puede contener números y no puede estar vacío, intente nuevamente.")
    if validate_identifier(careers, subject_degree):
        subjects.append({ "id": pos, "codigo": subject_code, "nombre": subject_name, "carrera": subject_degree }) # agregamos la materia a la lista
        set_data('subjects.json', subjects)
        print("\n [+] Materia agregada correctamente.\n")
    else:
        print("ERROR [!] No se puede añadir una materia para una carrera que no existe.")

def add_subjects(subjects):
    # funcion para agregar MULTIPLES materias a la lista subjects
    print(subject_menu)
    option = 's'
    while option != 'n':
        add_subject(subjects)
        option = validate_continue("\nDesea ingresar otra materia? (s/n): \n")

""" ----------------------------------------------------------------------------------------------"""
""" ############################### CALCULAR PROMEDIO POR MATERIA ############################### """
""" ----------------------------------------------------------------------------------------------"""

menu_average_title = """
=== PROMEDIO POR MATERIA ===
"""

def student_average_notes(notes, subjects):
    # funcion para calcular el promedio de notas de un estudiante
    print(menu_average_title)
    identifier = validate_int_input("\n- Ingrese el legajo del estudiante para calcular su promedio de notas: ", "ERROR [!] Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_existing(notes, identifier):
        subject_identifier = validate_int_input("- Ingrese el código de la materia para calcular el promedio de notas: ", "ERROR [!] Se ha ingresado un ID inválido. El ID no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
        if validate_identifier_by_subject(notes, subject_identifier):
            student_notes = get_notes_by_subject_student(notes, subject_identifier, identifier)
            subject_data = get_by_subject(subjects, subject_identifier)
            if student_notes:
                average = get_average(student_notes)
                if average:
                    print(f"\nEl promedio de notas del estudiante con legajo {identifier} en la materia {subject_data["codigo"]} es: {average:.2f}\n")
            else:
                print(f"\nATENCIÓN [!] No se encontraron notas para la materia con ID {subject_identifier} del estudiante con legajo {identifier}.\n")
