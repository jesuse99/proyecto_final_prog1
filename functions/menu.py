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

def validate_option():
    print(main_menu)
    option = int(input("Seleccione una opcion: "))
    while option < 1 or option > 8:
        print("Opcion incorrecta, intente nuevamente")
        print(main_menu)
        option = int(input("Seleccione una opcion: "))
    return option

# Creamos la funcion principal del programa
def menu():
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

# Creamos las funciones requeridas del programa
def add_student():
    print(student_menu)
    
    identifier = int(input("ingrese el legajo del estudiante: "))
    name = str(input("ingrese el nombre del estudiante: "))
    degree = str(input("ingrese la carrera del estudiante: "))
    
    students.append([ identifier, name, degree ])
    print("Estudiante agregado correctamente")

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