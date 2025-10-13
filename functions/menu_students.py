from functions.validations import validate_string_input,validate_int_input, validate_identifier, validate_continue, validate_menu_option
from functions.auxiliars import set_position, set_identifier, get_by_record, get_students_by_career
from utils.data import students, careers
from utils.service import get_data, set_data


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

student_menu = """
=== AGREGAR ESTUDIANTES ===
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
    if validate_identifier(careers, degree): 
        students.append([ pos, identifier, name, degree ]) # agregamos el estudiante a la lista
        set_data('students.csv', students)
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

menu_edit_student = """
=== EDITAR ESTUDIANTE ===

=== Opciones de Edición ===

1. Editar nombre
2. Editar carrera
3. Volver
"""

""" -------------------------------------------------------------------------------"""
""" ############################### EDITAR NOMBRE ############################### """
""" -------------------------------------------------------------------------------"""

def edit_name(data_list, identifier):
    # funcion para editar el nombre de un estudiante de la lista si existe
    name = validate_string_input("- Ingrese el nuevo nombre: ", "ERROR [!] Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    for resource in data_list:
        if int(resource[1]) == int(identifier):
            resource[2] = name
    set_data('students.csv', data_list)
    print("\nNombre editado correctamente.\n")

""" -------------------------------------------------------------------------------"""
""" ############################### EDITAR CARRERA ############################### """
""" -------------------------------------------------------------------------------"""

def edit_degree(data_list, identifier): 
    # funcion para editar la carrera de un estudiante de la lista si existe
    degree = validate_int_input("- Ingrese la nueva carrera: ", "ERROR [!] Se ha ingresado una carrera inválida. La carrera solo debe contener letras y no puede estar vacía, intente nuevamente.")
    for resource in data_list:
        if int(resource[1]) == int(identifier):
            resource[3] = degree
    set_data('students.csv', students)
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

""" -----------------------------------------------------------------------------------------------"""
""" ############################### BUSCAR ESTUDIANTES POR CARRERA ############################### """
""" -----------------------------------------------------------------------------------------------"""

search_career_menu = """
=== BUSCAR ESTUDIANTES POR CARRERA ===
"""

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

""" ---------------------------------------------------------------------------------------------"""
""" ############################### BUSCAR ESTUDIANTE POR LEGAJO ############################### """
""" ---------------------------------------------------------------------------------------------"""

search_students_menu = """
=== BUSCAR ESTUDIANTE POR LEGAJO ===
"""

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
