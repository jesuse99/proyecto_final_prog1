from functions.validations import validate_string_input,validate_int_input, validate_option, existing_student

# Declaramos e inicializamos todas las variables 
students = []
subjects = []
notes = []

main_menu = """
=== SISTEMA DE CALIFICACIONES UADE ===

1. Agregar estudiantes
2. Agregar materias
3. Ingresar notas
4. Mostrar promedio por materia
5. Mostrar promedio por estudiante
6. Buscar estudiante
7. Buscar materias
8. Salir
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

# Creamos la funcion principal del programa
def menu():
    # Menu principal del programa. Muestra las opciones y ejecuta las funciones correspondientes.
    option = validate_option()
    while not option == 8:
        match option:
            case 1:
                add_student()
                continue
            case 2:
                add_subject()
                continue            
            case 3:
                print("Ingresar notas")
                continue            
            case 4:
                print("Mostrar promedio por materia")
                continue            
            case 5:
                print("Motrar promedio por estudiante")
                continue            
            case 6:
                search_students()
                continue            
            case 7:
                search_subjects()
                continue            
            case 8:
                finish_program()
                continue            
        option = validate_option()

def add_students(students):
    # Funcion para agregar estudiantes a la lista de estudiantes
    print(student_menu)
    option = ''
    while option != 'n':
        add_student(students)
        option = str(input("Desea ingresar otro estudiante? (s/n): ")).lower()
        while option not in ('s', 'n'): # validamos que la opcion ingresada sea 's' o 'n'
            print("Opción inválida. Debe ser 's' o 'n'.")
            option = str(input("Desea ingresar otro estudiante? (s/n): ")).lower()
        
def add_student(students):
    # Funcion para agregar un estudiante a la lista de estudiantes
    identifier = validate_int_input("Ingrese el legajo del estudiante: ", "Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    while existing_student(students, identifier):
        # validamos que el legajo no se encuentre registrado en el sistema
        # si el legajo es valido, se sale del while y se pide que se ingrese el nombre y la carrera
        identifier = validate_int_input("Ingrese el legajo del estudiante: ", "Se ha ingresado un legajo inválido. El legajo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    name = validate_string_input("Ingrese el nombre del estudiante: ", "Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    degree = validate_string_input("Ingrese la carrera del estudiante: ", "Se ha ingresado una carrera inválida. La carrera solo debe contener letras y no puede estar vacía, intente nuevamente.")
    students.append([ identifier, name, degree ]) # agregamos el estudiante a la lista
    print("Estudiante agregado correctamente.")


def add_subject():
    print(subject_menu)

    identifier = int(input("ingrese el numero de materia: "))
    name = str(input("ingrese el nombre de la materia: "))
    degree = str(input("ingrese la carrera de la materia: "))
    
    subjects.append([ identifier, name, degree ])
    print("Materia agregada correctamente")

def search_for_name(value, list_search):
    result_search = []
    for item in list_search:
        if str(item[1]).upper() == str(value).upper():
            result_search.append(item)
    return result_search

def search_students():
    print(search_students_menu)
    
    name = str(input("Ingrese el nombre del estudiante: "))
    
    search = search_for_name(name, students)
    print("Resultado de la busqueda:")
    for item in search:
        print(str(item[0]).ljust(4), str(item[1]).ljust(4), str(item[2]).ljust(4))
        print("-"*40)

def search_subjects():
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
    input("Presione cualquier tecla para finalizar")