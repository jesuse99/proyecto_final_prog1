from functions.students import show_students, add_students, edit_student, delete_student, search_students_by_career, search_student_by_record
from functions.subjects import average_subject, show_subjects, add_subjects, edit_subject, delete_subject, student_average_subject
from functions.notes import show_notes, add_notes, edit_notes, delete_notes, search_notes_by_student_id
from functions.careers import average_career, show_careers, add_careers, edit_career, delete_career, student_average_career

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
3. Eliminar datos
4. Gestionar promedios
5. Buscar por criterio
6. Mostrar datos
7. Salir
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
    print(menu_add) # Muestro las opciones del menú de ingreso de datos
    option = validate_menu_option() # Valido la opción ingresada por el usuario

    match option:
        case 1:
            add_students(students) # Llamada a la función para agregar estudiantes
        case 2:
            add_subjects(subjects) # Llamada a la función para agregar materias
        case 3: 
            add_notes(notes, students, subjects) # Llamada a la función para agregar notas   
        case 4:
            add_careers(careers) # Llamada a la función para agregar carreras
        case 5:
            return # Si se ingresa la opción 5, se vuelve al menú principal 
        case _:
            print("\nSe ha ingresado una opción inválida. \n")

    print("\nVolviendo al menú de ingreso de datos...\n")  
    add_data_menu() # Llamada recursiva para mostrar el menú hasta que el usuario decida volver al menú principal ingresando la opción 5



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
    print(menu_edit) # Muestro las opciones del menú de edición
    option = validate_menu_option() # Valido la opción ingresada por el usuario

    match option: # Uso match-case para ejecutar la función correspondiente según la opción ingresada
        case 1:
            edit_student(students) # Llamada a la función para editar estudiantes
        case 2:
            edit_subject(subjects) # Llamada a la función para editar materias
        case 3:
            edit_notes(notes, subjects) # Llamada a la función para editar notas
        case 4:
            edit_career(careers) # Llamada a la función para editar carreras
        case 5:
            return # Si se ingresa la opción 5, se vuelve al menú principal 
        case _:
            print("\nSe ha ingresado una opción inválida. \n")

    print("\nVolviendo al menú de edición...\n")  
    edit_by_criteria() # Llamada recursiva para mostrar el menú hasta que el usuario decida volver al menú principal ingresando la opción 5


menu_delete = """
=== ElLIMINAR DATOS === 

1. Eliminar estudiantes
2. Eliminar materias
3. Eliminar notas
4. Eliminar carreras
5. Volver
"""

""" ---------------------------------------------------------------------------------------------"""
""" ############################### MENÚ CON OPCIONES DE ELIMINAR ############################### """
""" ---------------------------------------------------------------------------------------------"""

def delete_data_menu():
    # funcion para mostrar el menu de borrado y llamar a las funciones correspondientes segun sea estudiante o materia 
    print(menu_delete) # Muestro las opciones del menú de borrado
    option = validate_menu_option() # Valido la opción ingresada por el usuario

    match option: # Uso match-case para ejecutar la función correspondiente según la opción ingresada
        case 1:
            delete_student(students) # Llamada a la función para borrado de estudiantes
        case 2:
            delete_subject(subjects) # Llamada a la función para borrado de materias
        case 3:
            delete_notes(notes) # Llamada a la función para borrado de notas
        case 4:
            delete_career(careers) # Llamada a la función para borrado de carreras
        case 5:
            return # Si se ingresa la opción 5, se vuelve al menú principal 
        case _:
            print("\nSe ha ingresado una opción inválida. \n")
              
    print("\nVolviendo al menú de borrado...\n")  
    delete_data_menu() # Llamada recursiva para mostrar el menú hasta que el usuario decida volver al menú principal ingresando la opción 5


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
    print(menu_average) # Muestro las opciones del menú de gestión de promedios
    option = validate_menu_option() # Valido la opción ingresada por el usuario
    
    if option == 5: # Si se ingresa la opción 5, se vuelve al menú principal
        return

    match option: # Uso match-case para ejecutar la función correspondiente según la opción ingresada
        case 1:
            average_subject(notes, subjects) # Llamada a la función para calcular promedio de notas de una materia
        case 2:
            average_career(notes, careers, subjects) # Llamada a la función para calcular promedio de notas de una carrera
        case 3:
            student_average_subject(notes, subjects) # Llamada a la función para calcular promedio de notas de un estudiante en una materia
        case 4:
            student_average_career(notes, careers, subjects) # Llamada a la función para calcular promedio de notas de un estudiante en una carrera
    
    print("\nSe ha ingresado una opción inválida. \n")          
    print("\nVolviendo al menú de gestión de promedios...\n")  
    get_average_menu() # Llamada recursiva para mostrar el menú hasta que el usuario decida volver al menú principal ingresando la opción 5


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
    print(menu_search) # Muestro las opciones del menú de búsqueda por criterio
    option = validate_menu_option() # Valido la opción ingresada por el usuario

    if option == 4: # Si se ingresa la opción 4, se vuelve al menú principal
        return

    match option: # Uso match-case para ejecutar la función correspondiente según la opción ingresada
        case 1:
            search_student_by_record(students, careers) # Llamada a la función para buscar estudiante por legajo
        case 2:
            search_notes_by_student_id(notes, students, subjects) # Llamada a la función para buscar notas por legajo de estudiante
        case 3:
            search_students_by_career(careers, students) # Llamada a la función para buscar estudiantes por carrera
            
    print("\nSe ha ingresado una opción inválida. \n")          
    print("\nVolviendo al menú de búsqueda por criterio...\n")  
    search_by_criteria_menu() # Llamada recursiva para mostrar el menú hasta que el usuario decida volver al menú principal ingresando la opción 4


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
    print(menu_show_data) # Muestro las opciones del menú de mostrar datos
    option = validate_menu_option() # Valido la opción ingresada por el usuario
    
    if option == 5: # Si se ingresa la opción 5, se vuelve al menú principal
        return

    match option: # Uso match-case para ejecutar la función correspondiente según la opción ingresada
        case 1:
            show_students(students, careers) # Llamada a la función para mostrar estudiantes
        case 2:
            show_notes(notes, subjects, students) # Llamada a la función para mostrar notas
        case 3:
            show_subjects(subjects, careers) # Llamada a la función para mostrar materias
        case 4:
            show_careers(careers) # Llamada a la función para mostrar carreras

    print("\nSe ha ingresado una opción inválida. \n")          
    print("\nVolviendo al menú de edición de estudiantes...\n")  
    show_data_menu() # Llamada recursiva para mostrar el menú hasta que el usuario decida volver al menú principal ingresando la opción 5
    

""" ###################################################################### """
""" ############################## 5. Salir ############################## """
""" ###################################################################### """

""" ------------------------------------------------------------------------------"""
""" ############################### MENSAJE FINAL ############################### """
""" ------------------------------------------------------------------------------"""

def finish_program():
    print("Cerrando programa..")
    print("Programa finalizado")
    exit()
