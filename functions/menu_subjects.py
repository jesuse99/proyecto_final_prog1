from functions.validations import validate_string_input,validate_int_input, validate_identifier, validate_continue, validate_existing
from functions.auxiliars import set_position, set_identifier, get_by_record, get_notes_by_subject_student, get_average
from utils.data import subjects, notes, careers
from utils.service import get_data, set_data


""" ---------------------------------------------------------------------------------------------"""
""" ############################### MOSTRAR MATERIAS REGISTRADOS ############################### """
""" ---------------------------------------------------------------------------------------------"""

def show_subjects(subjects, careers):
    # funcion para mostrar todos los estudiantes de la lista de estudiantes
    print("\n=== MOSTRAR MATERIAS ===\n")
    for subject in subjects:
        subject_code = subject[1]
        subject_name = subject[2]
        subject_career = subject[3]

        # Buscar carrera por su codigo
        career_data = get_by_record(careers, subject_career)

        if career_data:
            career_name = career_data[2]
            career_building = career_data[3]
            print("Código de materia:",subject_code, " - Nombre:", subject_name, "- Carrera:", career_name, " - ", career_building)
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
        subjects.append([ pos, subject_code, subject_name, subject_degree ]) # agregamos la materia a la lista
        set_data('subjects.csv', subjects)
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
        if validate_identifier(notes, subject_identifier):
            student_notes = get_notes_by_subject_student(notes, subject_identifier, identifier)
            subject_data = get_by_record(subjects, subject_identifier)
            if student_notes:
                average = get_average(student_notes)
                if average:
                    print(f"\nEl promedio de notas del estudiante con legajo {identifier} en la materia {subject_data[1]} es: {average:.2f}\n")
            else:
                print(f"\nATENCIÓN [!] No se encontraron notas para la materia con ID {subject_identifier} del estudiante con legajo {identifier}.\n")
