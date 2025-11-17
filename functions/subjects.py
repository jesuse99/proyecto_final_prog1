from utils.validations import validate_existing_subject, validate_string_input,validate_int_input, validate_identifier, validate_identifier_by_subject, validate_continue, validate_existing, validate_submenu_option
from utils.auxiliars import get_notes_by_subject, set_position, set_identifier, get_by_subject, get_notes_by_subject_student, get_average
from utils.filehandler import get_data, set_data

subjects = get_data('subjects')
notes = get_data('notes')
careers = get_data('careers')

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
        if not validate_existing_subject(subjects, subject_name, subject_degree):
            subjects.append({ "id": pos, "codigo": subject_code, "nombre": subject_name, "carrera": subject_degree }) # agregamos la materia a la lista
            set_data('subjects', subjects)
            print("\n [+] Materia agregada correctamente.\n")
        else:
            print("ATENCIÓN [!] No se puede añadir una materia que ya existe.")
    else:
        print("ERROR [!] No se puede añadir una materia para una carrera que no existe.")

def add_subjects(subjects):
    # funcion para agregar MULTIPLES materias a la lista subjects
    print(subject_menu) # Muestro el menú de agregar materias
    add_subject(subjects) # Llamada a la función para agregar una materia
    option = validate_continue("\nDesea ingresar otra materia? (s/n): \n") # Valido si el usuario quiere agregar otra materia
    if option == 's': # Si el usuario quiere agregar otra materia, entonces llamo a la función recursivamente
        add_subjects(subjects) # Llamada recursiva para agregar otra materia


menu_edit_subject = """
=== EDITAR MATERIA ===

=== Opciones de Edición ===

1. Editar nombre
2. Editar carrera
3. Volver
"""

""" -------------------------------------------------------------------------------"""
""" ############################### EDITAR NOMBRE ############################### """
""" -------------------------------------------------------------------------------"""

def edit_name(data_list, code):
    # funcion para editar el nombre de una materia de la lista si existe
    name = validate_string_input("- Ingrese el nuevo nombre: ", "ERROR [!] Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    for resource in data_list:
        if int(resource["codigo"]) == int(code):
            resource["nombre"] = name
    set_data('subjects', data_list)
    print("\nNombre editado correctamente.\n")

""" -------------------------------------------------------------------------------"""
""" ############################### EDITAR CARRERA ############################### """
""" -------------------------------------------------------------------------------"""

def edit_degree(data_list, code): 
    # funcion para editar la carrera de una materia de la lista si existe
    degree = validate_int_input("- Ingrese la nueva carrera: ", "ERROR [!] Se ha ingresado una carrera inválida. La carrera solo debe contener letras y no puede estar vacía, intente nuevamente.")
    for resource in data_list:
        if int(resource["codigo"]) == int(code):
            resource["carrera"] = degree
    set_data('subjects', data_list)
    print("\nCarrera editada correctamente.\n")

""" ---------------------------------------------------------------------------------------"""
""" ############################### MENÚ EDITAR MATERIA ############################### """
""" ---------------------------------------------------------------------------------------"""

def edit_subject(subjects):
    # funcion para editar una materia de la lista de materia si existe
    code = validate_int_input("\n- Ingrese el codigo de la materia que desea editar: ", "ERROR [!] Se ha ingresado un codigo inválido. El codigo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_identifier(subjects, code): 
        # si el legajo existe, se procede a la edicion
        print(f"\nEditando materia con codigo: {code}")
        print(menu_edit_subject)
        option = validate_submenu_option()
        while not option == 3:   
            match option:
                case 1:
                    edit_name(subjects, code)
                case 2:
                    edit_degree(subjects, code)   
            print("\nVolviendo al menú de edición de materia...\n")  
            print(menu_edit_subject) 
            option = validate_submenu_option() 
    else:
        print("ATENCIÓN [!] No se puede editar una materia que no existe.")


menu_delete_subject = """
=== ELIMINAR MATERIA ===
"""

""" -----------------------------------------------------------------------------------"""
""" ############################### ELIMINAR MATERIA ################################# """
""" -----------------------------------------------------------------------------------"""

def delete_subject(subjects):
    # Funcion para eliminar una materia a la lista de materias
    subject_code = validate_int_input("\n- Ingrese el codigo de la materia que desea eliminar: ", "ERROR [!] Se ha ingresado un codigo inválido. El codigo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_identifier(subjects, subject_code): 
            subject = get_by_subject(subjects, subject_code) # obtenemos la materia por el codigo 
            subjects.remove(subject) # eliminamos la materia de la lista
            set_data('subjects', subjects)
            print("\n [x] Materia eliminada correctamente.\n")
    else:
        print("ATENCIÓN [!] No se puede eliminar una materia que no existe.")

def delete_subjects(subjects):
    # Funcion para eliminar MULTIPLES materias de la lista de materias
    print(menu_delete_subject) # Muestro el menú de eliminar materias
    delete_subject(subjects) # Llamada a la función para eliminar una materia
    option = validate_continue("\nDesea eliminar otra materia? (s/n): \n") 
    if option == 's': 
        delete_subject(subjects) # Llamada recursiva para eliminar otra materia 

""" ----------------------------------------------------------------------------------------------"""
""" ############################### CALCULAR PROMEDIO POR MATERIA ############################### """
""" ----------------------------------------------------------------------------------------------"""

menu_average_title = """
=== PROMEDIO POR MATERIA ===
"""

def average_subject(notes, subjects):
    # funcion para calcular el promedio de notas de una materia
    print(menu_average_title)
    subject_identifier = validate_int_input("- Ingrese el código de la materia para calcular el promedio de notas: ", "ERROR [!] Se ha ingresado un codigo inválido. El codigo debe ser un valor numérico, intente nuevamente.")
    if validate_identifier(subjects, subject_identifier):
        student_notes = get_notes_by_subject(notes, subject_identifier)
        subject_data = get_by_subject(subjects, subject_identifier)
        if student_notes:
            average = get_average(student_notes)
            if average:
                print(f"\nEl promedio de notas de la materia {subject_data["nombre"]} es: {average:.2f}\n")
        else:
            print(f"\nATENCIÓN [!] No se encontraron notas para la materia con ID {subject_identifier}.\n")
    else:
        print(f"\nATENCIÓN [!] No se encontro una materia con codigo {subject_identifier}.\n")


""" ----------------------------------------------------------------------------------------------"""
""" ############################### CALCULAR PROMEDIO DE ESTUDIANTE POR MATERIA ################# """
""" ----------------------------------------------------------------------------------------------"""

menu_student_average_title = """
=== PROMEDIO DE ESTUDIANTE POR MATERIA ===
"""

def student_average_subject(notes, subjects):
    # funcion para calcular el promedio de notas de un estudiante
    print(menu_student_average_title)
    identifier = validate_int_input("\n- Ingrese el legajo del estudiante para calcular el promedio de notas: ", "ERROR [!] Se ha ingresado un legajo inválido. El legajo debe ser un valor numérico, intente nuevamente.")
    if validate_existing(notes, identifier):
        subject_identifier = validate_int_input("- Ingrese el código de la materia para calcular el promedio de notas: ", "ERROR [!] Se ha ingresado un codigo inválido. El codigo debe ser un valor numérico, intente nuevamente.")
        if validate_identifier_by_subject(notes, subject_identifier):
            student_notes = get_notes_by_subject_student(notes, subject_identifier, identifier)
            subject_data = get_by_subject(subjects, subject_identifier)
            if student_notes:
                average = get_average(student_notes)
                if average:
                    print(f"\nEl promedio de notas del estudiante con legajo {identifier} en la materia {subject_data["nombre"]} es: {average:.2f}\n")
            else:
                print(f"\nATENCIÓN [!] No se encontraron notas para la materia {subject_identifier} del estudiante con legajo {identifier}.\n")
        else:
            print(f"\nATENCIÓN [!] No se encontro una materia con codigo {subject_identifier}.\n")
    else:
        print(f"\nATENCIÓN [!] No se encontro un estudiante con legajo {identifier}.\n")

