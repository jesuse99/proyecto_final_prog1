from utils.validations import validate_existing_note, validate_int_input, validate_identifier,validate_identifier_by_student, validate_continue, validate_existing, validate_date_input
from utils.auxiliars import set_position, get_by_student, get_by_subject, get_notes_by_student_record
from utils.filehandler import get_data, set_data

students = get_data('students')
subjects = get_data('subjects')
notes = get_data('notes')

""" ------------------------------------------------------------------------------------------"""
""" ############################### MOSTRAR NOTAS REGISTRADAS ############################### """
""" ------------------------------------------------------------------------------------------"""

def show_notes(notes, subjects, students):
    # funcion para mostrar todas las notas de la lista notes
    print("\n=== MOSTRAR NOTAS ===\n")
    formatted_row = '{:<22} {:<18} {:<8} {:<10}'
    print("================================"*2)
    print(formatted_row.format("Materia", "Estudiante", "Nota", "Fecha"))
    print("================================"*2)
    for note in notes:
        # Obtener los IDs de materia y estudiante
        subject_code = note["materia"]
        student_code = note["legajo"]
        # Obtener el valor de la nota
        note_value = note["nota"]

        # Obtener la fecha de la nota
        date_value = note["fecha"]

        # Buscar materia por su codigo
        subject_data = get_by_subject(subjects, subject_code)

        # Buscar el estudiante por su legajo
        student_data = get_by_student(students, student_code)

        # Mostrar la información de la nota si se encontraron la materia y el estudiante
        if subject_data and student_data:
            subject_name = subject_data["nombre"]
            student_name = student_data["nombre"]

            data_row = [subject_name, student_name, note_value, date_value]
            print(formatted_row.format(*data_row))

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
        if validate_identifier_by_student(students, student_identifier):
            note_value = get_note()
            date_value = get_date()
            if not validate_existing_note(notes, subject_code, student_identifier, note_value, date_value):
                notes.append({ "id": pos, "materia": subject_code, "legajo": student_identifier, "nota": note_value, "fecha": date_value })
                set_data('notes', notes)
                print("\n [+] Nota agregada correctamente.\n")
            else:
                print("ATENCIÓN [!] No se puede añadir una nota que ya existe.")
        else: 
            print("ATENCIÓN [!] No se puede añadir una nota para un estudiante que no existe.")
    else:
        print("ATENCIÓN [!] No se puede añadir una nota para una materia que no existe.")


def add_notes(notes, students, subjects):
    # funcion para añadir MULTIPLES notas a la lista notes
    print(note_menu) # Muestro el menú de agregar notas
    add_note(notes, students, subjects) # Llamada a la función para agregar una nota
    option = validate_continue("\nDesea ingresar otra nota? (s/n): \n") # Valido si el usuario quiere agregar otra nota
    if option == 's': # Si el usuario quiere agregar otra nota, entonces llamo a la función recursivamente
        add_notes(notes, students, subjects) # Llamada recursiva para agregar otra nota
    
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
        # Normalizar comparaciones a strings (las filas cargadas desde JSON son strings)
        if str(note["materia"]) == str(subject_identifier) and str(note["legajo"]) == str(student_identifier) and str(note["fecha"]) == str(note_date):
            note["nota"] = int(get_note())
            note["fecha"] = str(get_date())
            set_data('notes', notes)
            print("\nNota editada correctamente.\n")
            return True
    # Si no encontramos la nota con la materia, legajo y fecha indicados
    print("\nATENCIÓN [!] No se encontró una nota con la materia, legajo y fecha indicados.\n")
    return False

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
            # Validamos que la fecha exista asociada a alguna nota del estudiante y materia indicados
            # validate_date sólo comprueba existencia de la fecha en cualquier nota, por eso llamamos directamente a set_new_note
            print(f"\nEditando notas del estudiante con legajo: {identifier}")
            found = set_new_note(notes, identifier, subject_identifier, note_date)
            if not found:
                print("ATENCIÓN [!] No se pudo editar: no existe una nota con esa materia/legajo/fecha.")
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
    if validate_identifier_by_student(students, identifier):
        print("\nResultado de la búsqueda:\n")
        student_notes = get_notes_by_student_record(notes, identifier)
        if student_notes:
            student_data = get_by_student(students, identifier)
            print(f"Notas del estudiante {student_data["nombre"]} - Legajo: {identifier}")
            for note in student_notes:
                subject_id = note["materia"]
                subject_data = get_by_subject(subjects, subject_id)
                print(f"Materia: {subject_data["nombre"]} - Nota: {note["nota"]}")
        else:
            print("\nATENCIÓN [!] El estudiante no tiene notas registradas.\n")
    else:
        print("\nATENCIÓN [!] No se encontró un estudiante con el legajo ingresado.\n")
