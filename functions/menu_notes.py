from functions.validations import validate_int_input, validate_identifier, validate_continue, validate_existing, validate_date_input, validate_date
from functions.auxiliars import set_position, get_by_record, get_notes_by_student_record
from utils.data import students, subjects, notes
from utils.service import get_data, set_data


""" ------------------------------------------------------------------------------------------"""
""" ############################### MOSTRAR NOTAS REGISTRADAS ############################### """
""" ------------------------------------------------------------------------------------------"""

def show_notes(notes, subjects, students):
    # funcion para mostrar todas las notas de la lista notes
    print("\n=== MOSTRAR NOTAS ===\n")
    for note in notes:
        # Obtener los IDs de materia y estudiante
        subject_code = note[1]
        student_code = note[2]
        # Obtener el valor de la nota
        note_value = note[3]

        # Obtener la fecha de la nota
        date_value = note[4]

        # Buscar materia por su codigo
        subject_data = get_by_record(subjects, subject_code)

        # Buscar el estudiante por su legajo
        student_data = get_by_record(students, student_code)

        # Mostrar la información de la nota si se encontraron la materia y el estudiante
        if subject_data and student_data:
            subject_name = subject_data[2]
            student_name = student_data[2]
            print(f"Materia: {subject_name} - Estudiante: {student_name} - Nota: {note_value} - Fecha: {date_value}")

""" -----------------------------------------------------------------------------"""
""" ############################### AÑADIR NOTAS ############################### """
""" -----------------------------------------------------------------------------"""

note_menu = """
=== AGREGAR NOTAS ===
"""

def add_note(notes, students, subjects):
    #funcion para añadir una nota a la lista notes
    pos = set_position(notes)
    subject_code = validate_int_input("- Ingrese el código de la materia: ", "ERROR [!] Se ha ingresado un ID inválido. El ID no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_identifier(subjects,subject_code):
        student_identifier = validate_int_input("\n- Ingrese el legajo del estudiante: ", "ERROR [!] Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
        if validate_identifier(students, student_identifier):
            note_value = get_note()
            date_value = get_date()
            notes.append([pos, subject_code, student_identifier,note_value,date_value])
            set_data('notes.csv', notes)
            print("\nNota agregada correctamente.\n")
        else: 
            print("ATENCIÓN [!] No se puede añadir una nota para un estudiante que no existe.")
    else:
        print("ATENCIÓN [!] No se puede añadir una nota para una materia que no existe.")

def add_notes(notes, students, subjects):
    # funcion para añadir MULTIPLES notas a la lista notes
    print(note_menu)
    option = 's'
    while option != 'n':
        add_note(notes, students, subjects)
        option = validate_continue("\nDesea ingresar otra nota? (s/n): \n")
    
""" ----------------------------------------------------------------------------------"""
""" ############################### SETEAR NUEVA NOTA ############################### """
""" ----------------------------------------------------------------------------------"""

def get_note():
    new_note = validate_int_input("- Ingrese la nueva nota: ", "ERROR [!] Se ha ingresado una nota inválida. La nota debe ser un número entre 0 y 100, intente nuevamente.")
    while new_note < 0 or new_note > 100:
        print("ERROR [!] Se ha ingresado una nota inválida. La nota debe ser un número entre 0 y 100, intente nuevamente.")
        new_note = validate_int_input("- Ingrese la nueva nota: ", "ERROR [!] Se ha ingresado una nota inválida. La nota debe ser un número entre 0 y 100, intente nuevamente.")
    return new_note

def get_date():
    new_date = validate_date_input("- Ingrese la fecha: ", "ERROR [!] Se ha ingresado una fecha inválida. La fecha debe tener el formato yyyy-MM-dd, intente nuevamente.")
    return new_date

def set_new_note(notes, student_identifier, subject_identifier, note_date):
    # funcion para editar una nota con una nueva nota ingresada por consola 
    for note in notes:
        if note[1] == str(subject_identifier) and note[2] == str(student_identifier) and note[4] == str(note_date):
            note[3] = get_note()
            note[4] = get_date()
            set_data('notes.csv', notes)
            print("\nNota editada correctamente.\n")
            return True

""" ----------------------------------------------------------------------------"""
""" ############################### EDITAR NOTA ############################### """
""" ----------------------------------------------------------------------------"""

def edit_notes(notes, subjects):
    # funcion para editar las notas de un estudiante de la lista de notas si existe
    # pendiente añadir que se ingrese la fecha en que se rindio la materia 
    identifier = validate_int_input("\n- Ingrese el legajo del estudiante cuyas notas desea editar: ", "ERROR [!] Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_existing(notes, identifier):
        subject_identifier = validate_int_input("- Ingrese el código de la materia cuya nota desea editar: ", "ERROR [!] Se ha ingresado un ID inválido. El ID no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
        if validate_identifier(subjects, subject_identifier):
            note_date = get_date()
            if validate_date(notes, note_date):
                # si el ID de la materia existe, se procede a buscar la nota correspondiente al estudiante y a la materia
                print(f"\nEditando notas del estudiante con legajo: {identifier}")
                # buscamos la nota correspondiente al estudiante y a la materia
                set_new_note(notes,identifier,subject_identifier, note_date)
        else:         
            print("ATENCIÓN [!] No se editar una nota para una materia que no existe.")
    else:
        print("ATENCIÓN [!] No se puede editar las notas de un estudiante que no existe.")

""" ----------------------------------------------------------------------------------------"""
""" ############################### BUSCAR NOTAS POR LEGAJO ############################### """
""" ----------------------------------------------------------------------------------------"""

search_notes_menu = """
=== BUSCAR NOTAS ===
"""

def search_notes_by_student_id(notes, students, subjects):
    print(search_notes_menu)
    # funcion para buscar las notas de un estudiante por su legajo
    identifier = validate_int_input("\n- Ingrese el legajo del estudiante cuyas notas desea buscar: ", "ERROR [!] Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_identifier(students, identifier):
        print("\nResultado de la búsqueda:\n")
        student_notes = get_notes_by_student_record(notes, identifier)
        if student_notes:
            student_data = get_by_record(students, identifier)
            print(f"Notas del estudiante {student_data[2]} - Legajo: {identifier}")
            for note in student_notes:
                subject_id = note[1]
                subject_data = get_by_record(subjects, subject_id)
                print(f"Materia: {subject_data[2]} - Nota: {note[3]}")
        else:
            print("\nATENCIÓN [!] El estudiante no tiene notas registradas.\n")
    else:
        print("\nATENCIÓN [!] No se encontró un estudiante con el legajo ingresado.\n")
