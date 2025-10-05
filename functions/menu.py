from functions.validations import validate_string_input,validate_int_input, validate_identifier, validate_continue, validate_menu_option, validate_existing_note

main_menu = """
=== SISTEMA DE CALIFICACIONES UADE ===

1. Ingresar datos
2. Editar datos
3. Gestionar promedios
4. Buscar por criterio
5. Mostrar datos
6. Salir
"""

menu_add = """
=== INGRESAR DATOS === 
1. Agregar estudiantes
2. Agregar materias
3. Salir
"""

menu_edit = """
=== EDITAR DATOS === 
1. Editar estudiantes
2. Editar notas
3. Salir
"""

menu_edit_student_title = """
=== EDITAR ESTUDIANTE ===
"""

menu_edit_student = """
=== EDITAR ESTUDIANTE ===

=== Opciones de Edición ===

1. Editar nombre
2. Editar carrera
3. Salir
"""

menu_show_data = """
=== MENÚ MOSTRAR DATOS ===
    1. Mostrar Alumnos
    2. Mostrar Notas
    3. Volver
"""

menu_average = """
=== GESTIONAR PROMEDIOS ===
    1. Calcular promedio de notas de un estudiante en una materia
    2. Volver
"""

menu_search = """
=== BUSCAR POR CRITERIO ===
    1. Buscar estudiante por legajo
    2. Buscar notas por legajo de estudiante
    3. Volver
"""

student_menu = """
=== AGREGAR ESTUDIANTE ===
"""

subject_menu = """
=== AGREGAR MATERIA ===
"""

search_students_menu = """
=== BUSCAR ESTUDIANTE ===
"""

search_subjects_menu = """
=== BUSCAR MATERIA ===
"""


""" ########################################################### """
""" #################### 1. Ingresar datos #################### """
""" ###########################################################"""

""" -----------------------------------------------------------------------------------"""
""" ############################### AÑADIR ESTUDIANTES ############################### """
""" -----------------------------------------------------------------------------------"""

def add_student(students):
    # Funcion para agregar un estudiante a la lista de estudiantes
    identifier = validate_int_input("\nIngrese el legajo del estudiante: ", "Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    while validate_identifier(students, identifier):
        # validamos que el legajo no se encuentre registrado en el sistema
        # si el legajo es valido, se sale del while y se pide que se ingrese el nombre y la carrera
        print("El legajo ingresado ya se encuentra registrado en el sistema. Intente nuevamente.")
        identifier = validate_int_input("\nIngrese el legajo del estudiante: ", "Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    name = validate_string_input("Ingrese el nombre del estudiante: ", "Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    degree = validate_string_input("Ingrese la carrera del estudiante: ", "Se ha ingresado una carrera inválida. La carrera solo debe contener letras y no puede estar vacía, intente nuevamente.")
    students.append([ identifier, name, degree ]) # agregamos el estudiante a la lista
    print("\nEstudiante agregado correctamente.\n")

def add_students(students):
    # Funcion para agregar MULTIPLES estudiantes a la lista de estudiantes
    print(student_menu)
    option = 's'
    while option != 'n':
        add_student(students)
        option = validate_continue("Desea ingresar otro estudiante? (s/n): \n")

""" -------------------------------------------------------------------------------"""
""" ############################### AÑADIR MATERIAS ############################### """
""" -------------------------------------------------------------------------------"""

## pendiente hacer las validaciones y comprobar que funcione todo bien
def add_subject(subjects):
    print(subject_menu)
    subject_identifier = validate_int_input("\nIngrese el ID de la materia: ", "Se ha ingresado un ID inválido. El ID no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    while validate_identifier(subjects, subject_identifier):
        # validamos que el ID no se encuentre registrado en el sistema
        # si el ID es valido, se sale del while y se pide que se ingrese el nombre y la carrera de la materia
        print("El ID ingresado ya se encuentra registrado en el sistema. Intente nuevamente.")
        subject_identifier = validate_int_input("\nIngrese el ID de la materia: ", "Se ha ingresado un ID inválido. El ID no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    subject_name = validate_string_input("Ingrese el nombre de la materia: ", "Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    subject_degree = validate_string_input("Ingrese la carrera de la materia: ", "Se ha ingresado una carrera inválida. La carrera solo debe contener letras y no puede estar vacía, intente nuevamente.")
    subjects.append([ subject_identifier, subject_name, subject_degree ]) # agregamos la materia a la lista
    print("\nMateria agregada correctamente.\n")


""" --------------------------------------------------------------------------------------------"""
""" ############################### MENÚ CON OPCIONES DE AÑADIR ############################### """
""" --------------------------------------------------------------------------------------------"""

def add_data_menu(students, subjects):
    # funcion para mostrar el menu de ingreso de datos y llamar a las funciones correspondientes segun sea estudiante o materia
    print(menu_add)
    option = validate_menu_option()
    while not option == 3:   
        match option:
            case 1:
                add_students(students)
            case 2:
                add_subject(subjects)               

        print("\nVolviendo al menú de ingreso de datos...\n")  
        print(menu_add) 
        option = validate_menu_option()



""" ############################################################################# """
""" ############################## 2. Editar datos ############################## """
""" ############################################################################# """

""" ---------------------------------------------------------------------------------------------"""
""" ############################### MENÚ CON OPCIONES DE EDICIÓN ############################### """
""" ---------------------------------------------------------------------------------------------"""

def edit_by_criteria(students, notes):
    # funcion para mostrar el menu de edicion y llamar a las funciones correspondientes segun sea estudiante o materia
    print(menu_edit)
    option = validate_menu_option()
    while not option == 3:   
        match option:
            case 1:
                print(menu_edit_student_title)
                edit_student(students)
            case 2:
                edit_notes(notes)      

        print("\nVolviendo al menú de edición...\n")  
        print(menu_edit) 
        option = validate_menu_option()

""" -------------------------------------------------------------------------------"""
""" ############################### EDITAR NOMBRE ############################### """
""" -------------------------------------------------------------------------------"""
def edit_name(data_list, identifier):
    # funcion para editar el nombre de un estudiante de la lista si existe
    name = validate_string_input("Ingrese el nuevo nombre: ", "Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    for resource in data_list:
        if resource[0] == identifier:
            resource[1] = name
    print("\nNombre editado correctamente.\n")

""" -------------------------------------------------------------------------------"""
""" ############################### EDITAR CARRERA ############################### """
""" -------------------------------------------------------------------------------"""

def edit_degree(data_list, identifier): 
    # funcion para editar la carrera de un estudiante de la lista si existe
    degree = validate_string_input("Ingrese la nueva carrera: ", "Se ha ingresado una carrera inválida. La carrera solo debe contener letras y no puede estar vacía, intente nuevamente.")
    for resource in data_list:
        if resource[0] == identifier:
            resource[2] = degree
    print("\nCarrera editada correctamente.\n")

""" -----------------------------------------------------------------------------"""
""" ############################### EDITAR NOTAS ############################### """
""" -----------------------------------------------------------------------------"""

def edit_notes(notes):
    # funcion para editar las notas de un estudiante de la lista de notas si existe
    # pendiente añadir que se ingrese la fecha en que se rindio la materia 
    identifier = validate_int_input("\nIngrese el legajo del estudiante cuyas notas desea editar: ", "Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_identifier(notes, identifier):
        # si el legajo existe, se procede a la edicion
        subject_identifier = validate_int_input("Ingrese el ID de la materia cuya nota desea editar: ", "Se ha ingresado un ID inválido. El ID no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
        if validate_existing_note(notes, subject_identifier):
            # si el ID de la materia existe en las notas, se procede a buscar la nota correspondiente al estudiante y a la materia
            print(f"Editando notas del estudiante con legajo: {identifier}")
            # buscamos la nota correspondiente al estudiante y a la materia
            for note in notes: 
                if note[2] == identifier and note[1] == subject_identifier:
                    new_note = validate_int_input("Ingrese la nueva nota: ", "Se ha ingresado una nota inválida. La nota debe ser un número entre 0 y 100, intente nuevamente.")
                    while new_note < 0 or new_note > 100:
                        print("Se ha ingresado una nota inválida. La nota debe ser un número entre 0 y 100, intente nuevamente.")
                        new_note = validate_int_input("Ingrese la nueva nota: ", "Se ha ingresado una nota inválida. La nota debe ser un número entre 0 y 100, intente nuevamente.")
                    note[3] = new_note
                    print("\nNota editada correctamente.\n")
                    return
        else:         
            print("No se encontró una nota para la materia del estudiante especificado.")
    else:
        print("No se puede editar las notas de un estudiante que no existe.")

""" ---------------------------------------------------------------------------------------"""
""" ############################### MENÚ EDITAR ESTUDIANTE ############################### """
""" ---------------------------------------------------------------------------------------"""

def edit_student(students):
    # funcion para editar un estudiante de la lista de estudiantes si existe
    identifier = validate_int_input("\nIngrese el legajo del estudiante que desea editar: ", "Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_identifier(students, identifier): 
        # si el legajo existe, se procede a la edicion
        print(f"\nEditando estudiante con legajo: {identifier}")
        print(menu_edit_student)
        option = validate_menu_option()
        while not option == 4:   
            match option:
                case 1:
                    edit_name(students, identifier)
                case 2:
                    edit_degree(students, identifier)   
            print("\nVolviendo al menú de edición de estudiantes...\n")  
            print(menu_edit_student) 
            option = validate_menu_option() 
    else:
        print("No se puede editar un estudiante que no existe.")


""" #################################################################################### """
""" ############################## 3. Gestionar promedios ############################## """
""" #################################################################################### """

def get_average_menu(notes,subjects):
    # funcion para mostrar el menu de gestion de promedios y llamar a las funciones correspondientes
    print(menu_average)
    option = validate_menu_option()
    while not option == 2:   
        match option:
            case 1:
                student_average_notes(notes, subjects)
        print("\nVolviendo al menú de gestión de promedios...\n")  
        print(menu_average)
        option = validate_menu_option()



def student_average_notes(notes, subjects):
    # funcion para calcular el promedio de notas de un estudiante
    total = 0
    amount = 0
    identifier = validate_int_input("\nIngrese el legajo del estudiante para calcular su promedio de notas: ", "Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_identifier(notes, identifier):
        subject_identifier = validate_int_input("Ingrese el ID de la materia para calcular el promedio de notas: ", "Se ha ingresado un ID inválido. El ID no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
        if validate_existing_note(notes, subject_identifier):
            student_notes = get_notes_by_subject_student(notes, subject_identifier, identifier)
            subject_data = get_subject_by_id(subjects, subject_identifier)
            if student_notes:
                for note in student_notes:
                    total += note[3]
                    amount += 1
                if total > 0:
                    average = total / amount
                    print(f"\nEl promedio de notas del estudiante con legajo {identifier} en la materia {subject_data[1]} es: {average:.2f}\n")
            else:
                print(f"\nNo se encontraron notas para la materia con ID {subject_identifier} del estudiante con legajo {identifier}.\n")


def get_notes_by_subject_student(notes, subject_id, student_id):
    # funcion para obtener las notas de una materia por su ID
    subject_notes = []
    for note in notes:
        if note[1] == subject_id and note[2] == student_id:
            subject_notes.append(note)
    return subject_notes



""" #################################################################################### """
""" ############################## 4. Buscar por criterio ############################## """
""" #################################################################################### """

def search_by_criteria_menu(students, notes, subjects):
    # funcion para mostrar el menu de busqueda por criterio y llamar a las funciones correspondientes segun sea estudiante o materia
    print(menu_search)
    option = validate_menu_option()
    while not option == 3:
        match option:
            case 1:
                search_student_by_id(students)
            case 2:
                search_notes_by_student_id(notes, students, subjects)
        print("\nVolviendo al menú de búsqueda por criterio...\n")  
        print(menu_search)
        option = validate_menu_option()


def get_student_by_id(students, identifier):
    # funcion para obtener un estudiante por su legajo
    for student in students:
        if student[0] == identifier:
            return student
    return None

def get_notes_by_student_id(notes, identifier):
    # funcion para obtener las notas de un estudiante por su legajo
    student_notes = []
    for note in notes:
        if note[2] == identifier:
            student_notes.append(note)
    return student_notes

def get_subject_by_id(subjects, subject_id):
    # Buscar la materia por su ID
    for subject in subjects:
        if subject[0] == subject_id:
            return subject
    return None

def search_student_by_id(students):
    # funcion para buscar un estudiante por su legajo
    identifier = validate_int_input("\nIngrese el legajo del estudiante que desea buscar: ", "Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")  
    if validate_identifier(students, identifier):
        print("\nResultado de la búsqueda:\n")
        student = get_student_by_id(students, identifier)
        if student:
            print("Legajo:", student[0], " - Nombre:", student[1], "- Carrera:", student[2])
    else:
        print("\nNo se encontró un estudiante con el legajo ingresado.\n")

def search_notes_by_student_id(notes, students, subjects):
    # funcion para buscar las notas de un estudiante por su legajo
    identifier = validate_int_input("\nIngrese el legajo del estudiante cuyas notas desea buscar: ", "Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")  
    if validate_identifier(students, identifier):
        print("\nResultado de la búsqueda:\n")
        student_notes = get_notes_by_student_id(notes, identifier)
        if student_notes:
            student_data = get_student_by_id(students, identifier)
            print(f"Notas del estudiante {student_data[1]} - Legajo: {identifier}")
            for note in student_notes:
                subject_id = note[1]
                subject_data = get_subject_by_id(subjects, subject_id)
                print(f"Materia: {subject_data[1]} - Nota: {note[3]}")
        else:
            print("\nEl estudiante no tiene notas registradas.\n")
    else:
        print("\nNo se encontró un estudiante con el legajo ingresado.\n")


""" ############################################################################## """
""" ############################## 5. Mostrar datos ############################## """
""" ############################################################################## """


def show_students(students):
    # funcion para mostrar todos los estudiantes de la lista de estudiantes
    print("\n=== MOSTRAR ALUMNOS ===\n")
    for student in students:
        print("Legajo:",student[0], " - Nombre:", student[1], "- Carrera:", student[2])
    print()

def show_notes(notes, subjects, students):
    # funcion para mostrar todas las notas de la lista de notas
    print("\n=== MOSTRAR NOTAS ===\n")
    for note in notes:
        # Obtener los IDs de materia y estudiante
        subject_id = note[1]
        student_id = note[2]
        note = note[3]

        # Buscar la materia por su ID
        subject_data = get_subject_by_id(subjects, subject_id)

        # Buscar el estudiante por su legajo
        student_data = get_student_by_id(students, student_id)
        
        # Mostrar la información de la nota si se encontraron la materia y el estudiante
        if subject_data and student_data:
            print(f"Materia: {subject_data[1]} - Estudiante: {student_data[1]} - Nota: {note}")
        

def show_data_menu(students, subjects, notes):
    # funcion para mostrar el menu de mostrar datos y llamar a las funciones correspondientes segun sea estudiantes o notas
    print(menu_show_data)
    option = validate_menu_option()
    while not option == 3:
        match option:
            case 1:
                show_students(students)
            case 2:
                show_notes(notes, subjects, students)
        print("\nVolviendo al menú de edición de estudiantes...\n")  
        print(menu_show_data) 
        option = validate_menu_option()






def finish_program():
    print("Cerrando programa..")
    print("Programa finalizado")
