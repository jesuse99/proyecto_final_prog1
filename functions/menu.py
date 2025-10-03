from functions.validations import validate_string_input,validate_int_input, validate_identifier, validate_continue, validate_menu_option, exists_identifier

main_menu = """
=== SISTEMA DE CALIFICACIONES UADE ===

1. Agregar estudiantes
2. Agregar profesores
3. Agregar materias
3. Gestionar notas
4. Gestionar promedios
5. Buscar por criterio
6. Editar por criterio
7. Salir
"""

menu_edit = """
=== EDITAR POR CRITERIO ===

1. Editar estudiantes
2. Editar profesores
3. Salir
"""

menu_edit_student_title = """
=== EDITAR ESTUDIANTE ===
"""

menu_edit_professor_title = """
=== EDITAR PROFESOR ===         
"""

menu_edit_student = """
=== EDITAR ESTUDIANTE ===

=== Opciones de Edición ===

1. Editar nombre
2. Editar carrera
3. Editar notas
4. Salir
"""

menu_edit_professor = """
=== EDITAR PROFESOR ===

=== Opciones de Edición ===

1. Editar nombre
2. Editar carrera
3. Editar materia
4. Salir
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

""" ######################################################################################################### """
""" #################### FUNCIONES PARA AÑADIR ESTUDIANTES, PROFESORES, MATERIAS Y NOTAS #################### """
""" ######################################################################################################### """

""" -----------------------------------------------------------------------------------"""
""" ############################### AÑADIR ESTUDIANTES ############################### """
""" -----------------------------------------------------------------------------------"""

def add_student(students):
    # Funcion para agregar un estudiante a la lista de estudiantes
    identifier = validate_int_input("\nIngrese el legajo del estudiante: ", "Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    while validate_identifier(students, identifier):
        # validamos que el legajo no se encuentre registrado en el sistema
        # si el legajo es valido, se sale del while y se pide que se ingrese el nombre y la carrera
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

""" ----------------------------------------------------------------------------------"""
""" ############################### AÑADIR PROFESORES ############################### """
""" ----------------------------------------------------------------------------------"""

def add_professor(professors):
    # funcion para agregar un profesor a la lista de profesores
    identifier = validate_int_input("\nIngrese el legajo del profesor: ", "Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    while validate_identifier(professors, identifier):
        # validamos que el legajo no se encuentre registrado en el sistema
        # si el legajo es valido, se sale del while y se pide que se ingrese el nombre y la carrera
        identifier = validate_int_input("\nIngrese el legajo del estudiante: ", "Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    name = validate_string_input("Ingrese el nombre del profesor: ", "Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    degree = validate_string_input("Ingrese la carrera del profesor: ", "Se ha ingresado una carrera inválida. La carrera solo debe contener letras y no puede estar vacía, intente nuevamente.")
    subject_id = validate_int_input("Ingrese la materia del profesor: ", "Se ha ingresado una materia inválida. La materia solo debe contener letras y no puede estar vacía, intente nuevamente.")
    professors.append([ identifier, name, degree, subject_id ]) # agregamos el profesor a la lista
    print("\nProfesor agregado correctamente.\n")

def add_professors(professors):
    # funcion para agregar MULTIPLES profesores a the lista de profesores
    print("=== AGREGAR PROFESOR ===")
    option = 's'
    while option != 'n':
        add_professor(professors)
        option = validate_continue("Desea ingresar otro profesor? (s/n): \n")


""" -------------------------------------------------------------------------------"""
""" ############################### AÑADIR MATERIAS ############################### """
""" -------------------------------------------------------------------------------"""


## pendiente hacer las validaciones y comprobar que funcione todo bien
def add_subject(subjects):
    print(subject_menu)

    identifier = int(input("ingrese el numero de materia: "))
    name = str(input("ingrese el nombre de la materia: "))
    degree = str(input("ingrese la carrera de la materia: "))
    
    subjects.append([ identifier, name, degree ])
    print("Materia agregada correctamente")



""" ############################################################################################################ """
""" ############################## FUNCIONES PARA EDITAR ESTUDIANTES Y PROFESORES ############################## """
""" ############################################################################################################ """

""" ---------------------------------------------------------------------------------------------"""
""" ############################### MENÚ CON OPCIONES DE EDICIÓN ############################### """
""" ---------------------------------------------------------------------------------------------"""

def edit_by_criteria(students,professors):
    # funcion para mostrar el menu de edicion y llamar a las funciones correspondientes segun sea estudiante o profesor
    print(menu_edit)
    option = validate_menu_option()
    while not option == 3:   
        match option:
            case 1:
                print(menu_edit_student_title)
                edit_student(students)
            case 2:
                print(menu_edit_professor_title)
                edit_professor(professors)       

        print("\nVolviendo al menú de edición...\n")  
        print(menu_edit) 
        option = validate_menu_option()

""" -------------------------------------------------------------------------------"""
""" ############################### EDITAR NOMBRE ############################### """
""" -------------------------------------------------------------------------------"""
def edit_name(data_list, identifier):
    # funcion para editar el nombre de un estudiante o profesor de la lista si existe
    name = validate_string_input("Ingrese el nuevo nombre: ", "Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    for resource in data_list:
        if resource[0] == identifier:
            resource[1] = name
    print("\nNombre editado correctamente.\n")

""" -------------------------------------------------------------------------------"""
""" ############################### EDITAR CARRERA ############################### """
""" -------------------------------------------------------------------------------"""

def edit_degree(data_list, identifier): 
    # funcion para editar la carrera de un estudiante o profesor de la lista si existe
    degree = validate_string_input("Ingrese la nueva carrera: ", "Se ha ingresado una carrera inválida. La carrera solo debe contener letras y no puede estar vacía, intente nuevamente.")
    for resource in data_list:
        if resource[0] == identifier:
            resource[2] = degree
    print("\nCarrera editada correctamente.\n")

""" -----------------------------------------------------------------------------"""
""" ############################### EDITAR NOTAS ############################### """
""" -----------------------------------------------------------------------------"""

def edit_notes(notes, students, student_identifier, subject_identifier):
    # funcion para editar las notas de un estudiante de la lista de notas si existe
    identifier = validate_int_input("\nIngrese el legajo del estudiante que desea editar: ", "Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if exists_identifier(students, identifier): 
        # si el legajo existe, se procede a la edicion
        print(f"Editando notas del estudiante con legajo: {identifier}")
        for note in notes:
            if note[1] == student_identifier and note[0] == subject_identifier:
                new_note = validate_int_input("Ingrese la nueva nota: ", "Se ha ingresado una nota inválida. La nota debe ser un número entre 0 y 100, intente nuevamente.")
                while new_note < 0 or new_note > 100:
                    print("Se ha ingresado una nota inválida. La nota debe ser un número entre 0 y 100, intente nuevamente.")
                    new_note = validate_int_input("Ingrese la nueva nota: ", "Se ha ingresado una nota inválida. La nota debe ser un número entre 0 y 100, intente nuevamente.")
                note[3] = new_note
                print("\nNota editada correctamente.\n")
                return
        print("No se encontró la materia para el estudiante especificado.")
    else:
        print("No se puede editar un estudiante que no existe.")

""" ---------------------------------------------------------------------------------------"""
""" ############################### MENÚ EDITAR ESTUDIANTE ############################### """
""" ---------------------------------------------------------------------------------------"""

def edit_student(students):
    # funcion para editar un estudiante de la lista de estudiantes si existe
    identifier = validate_int_input("\nIngrese el legajo del estudiante que desea editar: ", "Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if exists_identifier(students, identifier): 
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
                case 3:
                    edit_notes(students)
            print("\nVolviendo al menú de edición de estudiantes...\n")  
            print(menu_edit_student) 
            option = validate_menu_option() 
    else:
        print("No se puede editar un estudiante que no existe.")

""" -------------------------------------------------------------------------------------"""
""" ############################### MENÚ EDITAR PROFESOR ############################### """
""" -------------------------------------------------------------------------------------"""

def edit_professor(professors):
    # funcion para editar un profesor de la lista de profesores si existe
    identifier = validate_int_input("\nIngrese el legajo del profesor que desea editar: ", "Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if exists_identifier(professors, identifier):   
        # si el legajo existe, se procede a la edicion
        print(f"\nEditando profesor con legajo: {identifier}")
        print(menu_edit_professor)
        option = validate_menu_option()
        while not option == 4:   
            match option:
                case 1:
                    edit_name(professors, identifier)
                case 2:
                    edit_degree(professors, identifier)   
                case 3:
                    print("Editar materia") 
            print("\nVolviendo al menú de edición de profesores...\n")  
            print(menu_edit_professor) 
            option = validate_menu_option()
    else:
        print("No se puede editar un profesor que no existe.")



""" ################################################################################### """
""" ############################## FUNCIONES DE BÚSQUEDA ############################## """
""" ################################################################################### """


def search_for_name(value, list_search):
    result_search = []
    for item in list_search:
        if str(item[1]).upper() == str(value).upper():
            result_search.append(item)
    return result_search

def search_students(students):
    print(search_students_menu)
    
    name = str(input("Ingrese el nombre del estudiante: "))
    
    search = search_for_name(name, students)
    print("Resultado de la busqueda:")
    for item in search:
        print(str(item[0]).ljust(4), str(item[1]).ljust(4), str(item[2]).ljust(4))
        print("-"*40)

def search_subjects(subjects):
    print(search_subjects_menu)
    
    name = str(input("Ingrese el nombre de la materia: "))
    
    search = search_for_name(name, subjects)
    print("Resultado de la busqueda:")
    for item in search:
        print(str(item[0]).ljust(4), str(item[1]).ljust(4), str(item[2]).ljust(4))
        print("-"*40)

def finish_program():
    print("Cerrando programa..")
    print("Programa finalizado")