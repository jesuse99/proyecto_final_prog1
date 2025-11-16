from utils.validations import validate_existing_student, validate_string_input,validate_int_input,validate_identifier, validate_identifier_by_student, validate_continue, validate_menu_option
from utils.auxiliars import set_position, set_identifier_by_student, get_by_student, get_by_career, get_students_by_career
from utils.filehandler import get_data, set_data

students = get_data('students')
careers = get_data('careers')

""" ------------------------------------------------------------------------------------------------"""
""" ############################### MOSTRAR ESTUDIANTES REGISTRADOS ############################### """
""" ------------------------------------------------------------------------------------------------"""

def show_students(students, careers):
    # funcion para mostrar todos los estudiantes de la lista de estudiantes
    print("\n=== MOSTRAR ALUMNOS ===\n")
    formatted_row = '{:<8} {:<18} {:<24} {:<36}'
    print("==========================================="*2)
    print(formatted_row.format("Legajo", "Nombre", "Carrera", "Facultad"))
    print("==========================================="*2)
    for student in students:
        student_identifier = student["legajo"]
        student_name = student["nombre"]
        student_grade = student["carrera"]

        # Buscar carrera por su codigo
        career_data = get_by_career(careers, student_grade)

        if career_data:
            career_name = career_data["nombre"]
            career_building = career_data["facultad"]
            
            data_row = [student_identifier, student_name, career_name, career_building]
            print(formatted_row.format(*data_row))

student_menu = """
=== AGREGAR ESTUDIANTES ===
"""

""" -----------------------------------------------------------------------------------"""
""" ############################### AÑADIR ESTUDIANTES ############################### """
""" -----------------------------------------------------------------------------------"""

def add_student(students):
    # Funcion para agregar un estudiante a la lista de estudiantes
    pos =  set_position(students)
    identifier = set_identifier_by_student(students)
    student_name = validate_string_input("- Ingrese el nombre del estudiante: ", "ERROR [!] Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    student_degree = validate_int_input("- Ingrese el código de carrera del estudiante:", "ERROR [!] Se ha ingresado un codigo inválido. El código solo puede contener números y no puede estar vacío, intente nuevamente.")
    if validate_identifier(careers, student_degree): 
        if not validate_existing_student(students, student_name):
            students.append({ "id": pos, "legajo": identifier, "nombre": student_name, "carrera": student_degree }) # agregamos el estudiante a la lista
            set_data('students', students)
            print("\n [+] Estudiante agregado correctamente.\n")
        else:
            print("ATENCIÓN [!] No se puede añadir un estudiante que ya existe.")
    else:
        print("ERROR [!] No se puede añadir un estudiante para una carrera que no existe.")

def add_students(students):
    # Funcion para agregar MULTIPLES estudiantes a la lista de estudiantes
    print(student_menu) # Muestro el menú de agregar estudiantes
    add_student(students) # Llamada a la función para agregar un estudiante
    option = validate_continue("\nDesea ingresar otro estudiante? (s/n): \n") 
    if option == 's': 
        add_students(students) # Llamada recursiva para agregar otro estudiante 

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
        if int(resource["legajo"]) == int(identifier):
            resource["nombre"] = name
    set_data('students', data_list)
    print("\nNombre editado correctamente.\n")

""" -------------------------------------------------------------------------------"""
""" ############################### EDITAR CARRERA ############################### """
""" -------------------------------------------------------------------------------"""

def edit_degree(data_list, identifier): 
    # funcion para editar la carrera de un estudiante de la lista si existe
    degree = validate_int_input("- Ingrese la nueva carrera: ", "ERROR [!] Se ha ingresado una carrera inválida. La carrera solo debe contener letras y no puede estar vacía, intente nuevamente.")
    for resource in data_list:
        if int(resource["legajo"]) == int(identifier):
            resource["carrera"] = degree
    set_data('students', data_list)
    print("\nCarrera editada correctamente.\n")


""" ---------------------------------------------------------------------------------------"""
""" ############################### MENÚ EDITAR ESTUDIANTE ############################### """
""" ---------------------------------------------------------------------------------------"""

def edit_student(students):
    # funcion para editar un estudiante de la lista de estudiantes si existe
    identifier = validate_int_input("\n- Ingrese el legajo del estudiante que desea editar: ", "ERROR [!] Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_identifier_by_student(students, identifier): 
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
            student_name = student["nombre"]
            student_indentifier = student["legajo"]
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
    if validate_identifier_by_student(students, identifier):
        print("\nResultado de la búsqueda:\n")
        student = get_by_student(students, identifier)
        if student:
            student_name = student["nombre"]
            student_career = student["carrera"]
            # Buscar carrera por su codigo
            career_data = get_by_career(careers, student_career)

            if career_data:
                career_name = career_data["nombre"]
                career_building = career_data["facultad"]
                print("Legajo:",identifier, " - Nombre:", student_name, "- Carrera:", career_name, " - ", career_building)
    else:
        print("\nATENCIÓN [!] No se encontró un estudiante con el legajo ingresado.\n")
