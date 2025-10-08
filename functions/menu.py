import random
from functions.validations import validate_string_input,validate_int_input, validate_identifier, validate_continue, validate_menu_option, validate_existing, validate_existing_career
from functions.auxiliars import set_position, set_identifier, get_by_record, get_notes_by_student_record, get_notes_by_subject_student, get_average, get_students_by_career


main_menu = """
=== SISTEMA DE CALIFICACIONES UADE ===

1. Ingresar datos
2. Editar datos
3. Gestionar promedios
4. Buscar por criterio
5. Mostrar datos
6. Salir
"""

""" ########################################################### """
""" #################### 1. Ingresar datos #################### """
""" ###########################################################"""

menu_add = """
=== INGRESAR DATOS === 

1. Agregar estudiantes
2. Agregar materias
3. Agregar notas
4. Agregar carreras
5. Volver
"""

student_menu = """
=== AGREGAR ESTUDIANTES ===
"""

subject_menu = """
=== AGREGAR MATERIAS ===
"""

note_menu = """
=== AGREGAR NOTAS ===
"""

career_menu = """
=== AGREGAR CARRERAS ===
"""

""" -----------------------------------------------------------------------------------"""
""" ############################### AÑADIR ESTUDIANTES ############################### """
""" -----------------------------------------------------------------------------------"""

def add_student(students):
    # Funcion para agregar un estudiante a la lista de estudiantes
    identifier = set_identifier(students)
    pos =  set_position(students)
    name = validate_string_input("- Ingrese el nombre del estudiante: ", "ERROR [!] Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    degree = validate_int_input("- Ingrese el código de carrera del estudiante:", "ERROR [!] Se ha ingresado un codigo inválido. El código solo puede contener números y no puede estar vacío, intente nuevamente.")
    if validate_identifier(students, identifier): 
        degree = validate_string_input("- Ingrese la carrera del estudiante: ", "ERROR [!] Se ha ingresado una carrera inválida. La carrera solo debe contener letras y no puede estar vacía, intente nuevamente.")
        students.append([ pos, identifier, name, degree ]) # agregamos el estudiante a la lista
        print("\n [+] Estudiante agregado correctamente.\n")
    else:
        print("ERROR [!] No se puede añadir un estudiante para una carrera que no existe.")

def add_students(students):
    # Funcion para agregar MULTIPLES estudiantes a la lista de estudiantes
    print(student_menu)
    option = 's'
    while option != 'n':
        add_student(students)
        option = validate_continue("\nDesea ingresar otro estudiante? (s/n): \n")

""" --------------------------------------------------------------------------------"""
""" ############################### AÑADIR MATERIAS ############################### """
""" --------------------------------------------------------------------------------"""

def add_subject(subjects, careers):
    # función para agregar una materia a la lista subjects
    print(subject_menu)
    subject_code = set_identifier(subjects)
    pos = set_position(subjects)   
    subject_name = validate_string_input("- Ingrese el nombre de la materia: ", "ERROR [!]Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    subject_degree = validate_int_input("- Ingrese el código de carrera de la materia:", "ERROR [!] Se ha ingresado un codigo inválido. El código solo puede contener números y no puede estar vacío, intente nuevamente.")
    if validate_identifier(careers, subject_degree):
        subjects.append([ pos, subject_code, subject_name, subject_degree ]) # agregamos la materia a la lista
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



""" -----------------------------------------------------------------------------"""
""" ############################### AÑADIR NOTAS ############################### """
""" -----------------------------------------------------------------------------"""

def add_note(notes, students, subjects):
    #funcion para añadir una nota a la lista notes
    pos = set_position(notes)
    subject_code = validate_int_input("- Ingrese el código de la materia: ", "ERROR [!] Se ha ingresado un ID inválido. El ID no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_identifier(subjects,subject_code):
        student_identifier = validate_int_input("\n- Ingrese el legajo del estudiante: ", "ERROR [!] Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
        if validate_identifier(students, student_identifier):
            note_value = get_note()
            notes.append([pos, subject_code, student_identifier,note_value])
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
    


""" --------------------------------------------------------------------------------"""
""" ############################### AÑADIR CARRERAS ############################### """
""" --------------------------------------------------------------------------------"""

def add_career(careers):
    # Función para añadir UNA carrera a la lista careers
    pos = set_position(careers)
    career_code = set_identifier(careers)
    career_name = validate_string_input("- Ingrese el nombre de la carrera: ", "ERROR [!]Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    career_org = validate_string_input("- Ingrese el nombre de la facultad: ", "ERROR [!]Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    if not validate_existing_career(careers,career_name, career_org):
        careers.append([pos, career_code, career_name, career_org])
        print("\n [+] Carrera agregada correctamente.\n")
    else:
        print("ATENCIÓN [!] No se puede añadir carrera que ya existe.")

def add_careers(careers):
    # funcion para añadir MULTIPLES carreras a la lista careers
    print(career_menu)
    option = 's'
    while option != 'n':
        add_career(careers)
        option = validate_continue("\nDesea ingresar otra carrera? (s/n): \n")



""" --------------------------------------------------------------------------------------------"""
""" ############################### MENÚ CON OPCIONES DE AÑADIR ############################### """
""" --------------------------------------------------------------------------------------------"""

def add_data_menu(students, subjects, notes, careers):
    # funcion para mostrar el menu de ingreso de datos y llamar a las funciones correspondientes segun sea estudiante o materia
    print(menu_add)
    option = validate_menu_option()
    while not option == 5:   
        match option:
            case 1:
                add_students(students)
            case 2:
                add_subjects(subjects)   
            case 3: 
                add_notes(notes, students, subjects)    
            case 4:
                add_careers(careers)       

        print("\nVolviendo al menú de ingreso de datos...\n")  
        print(menu_add) 
        option = validate_menu_option()


""" ############################################################################# """
""" ############################## 2. Editar datos ############################## """
""" ############################################################################# """

menu_edit = """
=== EDITAR DATOS === 

1. Editar estudiantes
2. Editar notas
3. Volver
"""

menu_edit_student = """
=== EDITAR ESTUDIANTE ===

=== Opciones de Edición ===

1. Editar nombre
2. Editar carrera
3. Volver
"""

""" ---------------------------------------------------------------------------------------------"""
""" ############################### MENÚ CON OPCIONES DE EDICIÓN ############################### """
""" ---------------------------------------------------------------------------------------------"""

def edit_by_criteria(students, notes, subjects):
    # funcion para mostrar el menu de edicion y llamar a las funciones correspondientes segun sea estudiante o materia
    print(menu_edit)
    option = validate_menu_option()
    while not option == 3:   
        match option:
            case 1:
                print(menu_edit_student)
                edit_student(students)
            case 2:
                edit_notes(notes, subjects)      

        print("\nVolviendo al menú de edición...\n")  
        print(menu_edit) 
        option = validate_menu_option()

""" -------------------------------------------------------------------------------"""
""" ############################### EDITAR NOMBRE ############################### """
""" -------------------------------------------------------------------------------"""
def edit_name(data_list, identifier):
    # funcion para editar el nombre de un estudiante de la lista si existe
    name = validate_string_input("- Ingrese el nuevo nombre: ", "ERROR [!] Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    for resource in data_list:
        if resource[1] == identifier:
            resource[2] = name
    print("\nNombre editado correctamente.\n")

""" -------------------------------------------------------------------------------"""
""" ############################### EDITAR CARRERA ############################### """
""" -------------------------------------------------------------------------------"""

def edit_degree(data_list, identifier): 
    # funcion para editar la carrera de un estudiante de la lista si existe
    degree = validate_string_input("- Ingrese la nueva carrera: ", "ERROR [!] Se ha ingresado una carrera inválida. La carrera solo debe contener letras y no puede estar vacía, intente nuevamente.")
    for resource in data_list:
        if resource[1] == identifier:
            resource[3] = degree
    print("\nCarrera editada correctamente.\n")


""" ---------------------------------------------------------------------------------------"""
""" ############################### MENÚ EDITAR ESTUDIANTE ############################### """
""" ---------------------------------------------------------------------------------------"""

def edit_student(students):
    # funcion para editar un estudiante de la lista de estudiantes si existe
    identifier = validate_int_input("\n- Ingrese el legajo del estudiante que desea editar: ", "ERROR [!] Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_identifier(students, identifier): 
        # si el legajo existe, se procede a la edicion
        print(f"\nEditando estudiante con legajo: {identifier}")
        print(menu_edit_student)
        option = validate_menu_option()
        while not option == 3:   
            match option:
                case 1:
                    edit_name(students, identifier)
                case 2:
                    edit_degree(students, identifier)   
            print("\nVolviendo al menú de edición de estudiantes...\n")  
            print(menu_edit_student) 
            option = validate_menu_option() 
    else:
        print("ATENCIÓN [!] No se puede editar un estudiante que no existe.")





""" ----------------------------------------------------------------------------------"""
""" ############################### SETEAR NUEVA NOTA ############################### """
""" ----------------------------------------------------------------------------------"""
def get_note():
    new_note = validate_int_input("- Ingrese la nueva nota: ", "ERROR [!] Se ha ingresado una nota inválida. La nota debe ser un número entre 0 y 100, intente nuevamente.")
    while new_note < 0 or new_note > 100:
        print("ERROR [!] Se ha ingresado una nota inválida. La nota debe ser un número entre 0 y 100, intente nuevamente.")
        new_note = validate_int_input("- Ingrese la nueva nota: ", "ERROR [!] Se ha ingresado una nota inválida. La nota debe ser un número entre 0 y 100, intente nuevamente.")
    return new_note


def set_new_note(notes, student_identifier, subject_identifier):
    # funcion para editar una nota con una nueva nota ingresada por consola 
    for note in notes: 
        if note[2] == student_identifier and note[1] == subject_identifier:
            note[3] = get_note()
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
            # si el ID de la materia existe, se procede a buscar la nota correspondiente al estudiante y a la materia
            print(f"\nEditando notas del estudiante con legajo: {identifier}")
            # buscamos la nota correspondiente al estudiante y a la materia
            set_new_note(notes,identifier,subject_identifier)
        else:         
            print("ATENCIÓN [!] No se editar una nota para una materia que no existe.")
    else:
        print("ATENCIÓN [!] No se puede editar las notas de un estudiante que no existe.")


""" #################################################################################### """
""" ############################## 3. Gestionar promedios ############################## """
""" #################################################################################### """

menu_average = """
=== GESTIONAR PROMEDIOS ===

    1. Calcular promedio de notas de un estudiante en una materia
    2. Volver
"""

menu_average_title = """
=== PROMEDIO POR MATERIA ===
"""


""" ----------------------------------------------------------------------------------------------"""
""" ############################### MENÚ PARA GESTIONAR PROMEDIOS ############################### """
""" ----------------------------------------------------------------------------------------------"""

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

""" ----------------------------------------------------------------------------------------------"""
""" ############################### CALCULAR PROMEDIO POR MATERIA ############################### """
""" ----------------------------------------------------------------------------------------------"""

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


""" #################################################################################### """
""" ############################## 4. Buscar por criterio ############################## """
""" #################################################################################### """

menu_search = """
=== BUSCAR POR CRITERIO ===

    1. Buscar estudiante por legajo
    2. Buscar notas por legajo de estudiante
    3. Buscar estudiantes por carrera
    4. Volver
"""

search_students_menu = """
=== BUSCAR ESTUDIANTE ===
"""

search_notes_menu = """
=== BUSCAR NOTAS ===
"""

search_career_menu = """
=== BUSCAR ESTUDIANTES POR CARRERA ===
"""

""" ----------------------------------------------------------------------------------------------"""
""" ############################### MENÚ PARA BUSCAR POR CRITERIO ############################### """
""" ----------------------------------------------------------------------------------------------"""

def search_by_criteria_menu(students, notes, subjects, careers):
    # funcion para mostrar el menu de busqueda por criterio y llamar a las funciones correspondientes segun sea estudiante o materia
    print(menu_search)
    option = validate_menu_option()
    while not option == 4:
        match option:
            case 1:
                search_student_by_record(students, careers)
            case 2:
                search_notes_by_student_id(notes, students, subjects)
            case 3:
                search_students_by_career(careers, students)
        print("\nVolviendo al menú de búsqueda por criterio...\n")  
        print(menu_search)
        option = validate_menu_option()

""" ---------------------------------------------------------------------------------------------"""
""" ############################### BUSCAR ESTUDIANTE POR LEGAJO ############################### """
""" ---------------------------------------------------------------------------------------------"""

def search_student_by_record(students, careers):
    # funcion para buscar un estudiante por su legajo
    print(search_students_menu)
    identifier = validate_int_input("\n- Ingrese el legajo del estudiante que desea buscar: ", "ERROR [!] Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_identifier(students, identifier):
        print("\nResultado de la búsqueda:\n")
        student = get_by_record(students, identifier)
        if student:
            student_name = student[2]
            student_career = student[3]
            # Buscar carrera por su codigo
            career_data = get_by_record(careers, student_career)

            if career_data:
                career_name = career_data[2]
                career_building = career_data[3]
                print("Legajo:",identifier, " - Nombre:", student_name, "- Carrera:", career_name, " - ", career_building)
    else:
        print("\nATENCIÓN [!] No se encontró un estudiante con el legajo ingresado.\n")

""" ----------------------------------------------------------------------------------------"""
""" ############################### BUSCAR NOTAS POR LEGAJO ############################### """
""" ----------------------------------------------------------------------------------------"""

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


""" -----------------------------------------------------------------------------------------------"""
""" ############################### BUSCAR ESTUDIANTES POR CARRERA ############################### """
""" -----------------------------------------------------------------------------------------------"""

def search_students_by_career(careers, students):
    # funcion para buscar estudiantes por su codigo de carrera
    print(search_career_menu)
    career_code = validate_int_input("\n- Ingrese el codigo de carrera de los estudiantes que desea buscar: ", "ERROR [!] Se ha ingresado un codigo de carrera. El codigo de carrera no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_identifier(careers, career_code):
        print("\nResultado de la búsqueda:\n")
        students_data = get_students_by_career(students, career_code)
        print(f"Estudiantes para la carrera codigo {career_code}")
        for student in students_data:
            student_name = student[2]
            student_indentifier = student[1]
            print("Nombre: ", student_name, " - Legajo: ", student_indentifier)
    else:
        print("\nATENCIÓN [!] No se encontró una carrera con el código ingresado.\n")
            









""" ############################################################################## """
""" ############################## 5. Mostrar datos ############################## """
""" ############################################################################## """

menu_show_data = """
=== MENÚ MOSTRAR DATOS ===

    1. Mostrar Alumnos
    2. Mostrar Notas
    3. Mostrar Materias
    4. Volver
"""

""" -----------------------------------------------------------------------------------"""
""" ############################### MENÚ MOSTRAR DATOS ############################### """
""" -----------------------------------------------------------------------------------"""

def show_data_menu(students, subjects, notes, careers):
    # funcion para mostrar el menu de mostrar datos y llamar a las funciones correspondientes segun sea estudiantes o notas
    print(menu_show_data)
    option = validate_menu_option()
    while not option == 4:
        match option:
            case 1:
                show_students(students, careers)
            case 2:
                show_notes(notes, subjects, students)
            case 3:
                show_subjects(subjects, careers)
        print("\nVolviendo al menú de edición de estudiantes...\n")  
        print(menu_show_data) 
        option = validate_menu_option()


""" ------------------------------------------------------------------------------------------------"""
""" ############################### MOSTRAR ESTUDIANTES REGISTRADOS ############################### """
""" ------------------------------------------------------------------------------------------------"""

def show_students(students, careers):
    # funcion para mostrar todos los estudiantes de la lista de estudiantes
    print("\n=== MOSTRAR ALUMNOS ===\n")
    for student in students:
        student_identifier = student[1]
        student_name = student[2]
        student_grade = student[3]

        # Buscar carrera por su codigo
        career_data = get_by_record(careers, student_grade)

        if career_data:
            career_name = career_data[2]
            career_building = career_data[3]
            print("Legajo:",student_identifier, " - Nombre:", student_name, "- Carrera:", career_name, " - ", career_building)
        


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

        # Buscar materia por su codigo
        subject_data = get_by_record(subjects, subject_code)

        # Buscar el estudiante por su legajo
        student_data = get_by_record(students, student_code)

        # Mostrar la información de la nota si se encontraron la materia y el estudiante
        if subject_data and student_data:
            subject_name = subject_data[2]
            student_name = student_data[2]
            print(f"Materia: {subject_name} - Estudiante: {student_name} - Nota: {note_value}")
        

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

""" ###################################################################### """
""" ############################## 5. Salir ############################## """
""" ###################################################################### """

""" ------------------------------------------------------------------------------"""
""" ############################### MENSAJE FINAL ############################### """
""" ------------------------------------------------------------------------------"""

def finish_program():
    print("Cerrando programa..")
    print("Programa finalizado")
