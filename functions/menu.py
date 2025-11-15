from functions.students import show_students, add_students, edit_student, search_students_by_career, search_student_by_record
from functions.subjects import average_subject, show_subjects, add_subjects, edit_subject, student_average_subject
from functions.notes import show_notes, add_notes, edit_notes, search_notes_by_student_id
from functions.careers import average_career, show_careers, add_careers, edit_career, student_average_career

from utils.validations import validate_menu_option
from utils.filehandler import get_data

students = get_data('students')
subjects = get_data('subjects')
notes = get_data('notes')
careers = get_data('careers')

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

""" --------------------------------------------------------------------------------------------"""
""" ############################### MENÚ CON OPCIONES DE AÑADIR ############################### """
""" --------------------------------------------------------------------------------------------"""

def add_data_menu():
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
2. Editar materias
3. Editar notas
4. Editar carreras
5. Volver
"""

""" ---------------------------------------------------------------------------------------------"""
""" ############################### MENÚ CON OPCIONES DE EDICIÓN ############################### """
""" ---------------------------------------------------------------------------------------------"""

def edit_by_criteria():
    # funcion para mostrar el menu de edicion y llamar a las funciones correspondientes segun sea estudiante o materia
    print(menu_edit)
    option = validate_menu_option()
    while not option == 5:   
        match option:
            case 1:
                edit_student(students)
            case 2:
                edit_subject(subjects)
            case 3:
                edit_notes(notes, subjects)
            case 4:
                edit_career(careers)

        print("\nVolviendo al menú de edición...\n")  
        print(menu_edit) 
        option = validate_menu_option()


""" #################################################################################### """
""" ############################## 3. Gestionar promedios ############################## """
""" #################################################################################### """

menu_average = """
=== GESTIONAR PROMEDIOS ===

1. Calcular promedio de notas de una materia
2. Calcular promedio de notas de una carrera
3. Calcular promedio de notas de un estudiante en una materia
4. Calcular promedio de notas de un estudiante en una carrera
5. Volver
"""

""" ----------------------------------------------------------------------------------------------"""
""" ############################### MENÚ PARA GESTIONAR PROMEDIOS ############################### """
""" ----------------------------------------------------------------------------------------------"""

def get_average_menu():
    # funcion para mostrar el menu de gestion de promedios y llamar a las funciones correspondientes
    print(menu_average)
    option = validate_menu_option()
    while not option == 5:   
        match option:
            case 1:
                average_subject(notes, subjects)
            case 2:
                average_career(notes, careers, subjects)
            case 3:
                student_average_subject(notes, subjects)
            case 4:
                student_average_career(notes, careers, subjects)
        print("\nVolviendo al menú de gestión de promedios...\n")  
        print(menu_average)
        option = validate_menu_option()


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

""" ----------------------------------------------------------------------------------------------"""
""" ############################### MENÚ PARA BUSCAR POR CRITERIO ############################### """
""" ----------------------------------------------------------------------------------------------"""

def search_by_criteria_menu():
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


""" ############################################################################## """
""" ############################## 5. Mostrar datos ############################## """
""" ############################################################################## """

menu_show_data = """
=== MENÚ MOSTRAR DATOS ===

1. Mostrar estudiantes
2. Mostrar notas
3. Mostrar materias
4. Mostrar carreras
5. Volver
"""

""" -----------------------------------------------------------------------------------"""
""" ############################### MENÚ MOSTRAR DATOS ############################### """
""" -----------------------------------------------------------------------------------"""

def show_data_menu():
    # funcion para mostrar el menu de mostrar datos y llamar a las funciones correspondientes segun sea estudiantes o notas
    print(menu_show_data)
    option = validate_menu_option()
    while not option == 5:
        match option:
            case 1:
                show_students(students, careers)
            case 2:
                show_notes(notes, subjects, students)
            case 3:
                show_subjects(subjects, careers)
            case 4:
                show_careers(careers)
        print("\nVolviendo al menú de edición de estudiantes...\n")  
        print(menu_show_data) 
        option = validate_menu_option()
    

""" ###################################################################### """
""" ############################## 5. Salir ############################## """
""" ###################################################################### """

""" ------------------------------------------------------------------------------"""
""" ############################### MENSAJE FINAL ############################### """
""" ------------------------------------------------------------------------------"""

def finish_program():
    print("Cerrando programa..")
    print("Programa finalizado")
