from functions.menu import main_menu, add_data_menu, finish_program, edit_by_criteria, show_data_menu, search_by_criteria_menu, get_average_menu
from functions.validations import validate_menu_option   

# Declaramos e inicializamos todas las variables 

# students = []
# subjects = []  
# notes = []

students = [
    [1, "Sofía", "Ingeniería en Sistemas"], # id=1, nombre=Sofía, carrera=Ingeniería en Sistemas
    [2, "Marcos", "Medicina"],  # id=2, nombre=Marcos, carrera=Medicina
    [3, "Lucía", "Ingeniería"],  # id=3, nombre=Lucía, carrera=Ingeniería
    [4, "Tomás", "Arquitectura"], # id=4, nombre=Tomás, carrera=Arquitectura
    [5, "Ana", "Derecho"]        # id=5, nombre=Ana, carrera=Derecho
]

subjects = [
    [1, "Programación I", "Ingeniería en Sistemas"], # id=1, nombre=Programación I, carrera=Ingeniería en Sistemas
    [2, "Bases de Datos", "Ingeniería en Sistemas"], # id =2, nombre=Bases de Datos, carrera=Ingeniería en Sistemas
    [3, "Anatomía", "Medicina"], # id=3, nombre=Anatomía, carrera=Medicina
    [4, "Derecho Penal", "Derecho"], # id=4, nombre=Derecho Penal, carrera=Derecho
    [5, "Macroeconomía", "Ciencias Económicas"], # id=5, nombre=Macroeconomía, carrera=Ciencias Económicas
    [6, "Psicología Cognitiva", "Psicología"] # id=6, nombre=Psicología Cognitiva, carrera=Psicología
]

notes = [
    [1, 1, 1, 9],   # id=1, materia=1 (Programación I), estudiante=1 (Sofía), nota=9
    [2, 2, 1, 8],   # id=2, materia=2 (Bases de Datos), estudiante=1 (Sofía), nota=8
    [3, 3, 2, 7],   # id=3, materia=3 (Anatomía), estudiante=2 (Marcos), nota=7
    [4, 4, 3, 6],   # id=4, materia=4 (Derecho Penal), estudiante=3 (Lucía), nota=6
    [5, 1, 4, 10]   # id=5, materia=1 (Programación I), estudiante=4 (Tomás), nota=10
]


def menu():
    # Menu principal del programa. Muestra las opciones y ejecuta las funciones correspondientes.
    print(main_menu)
    option = validate_menu_option()
    while not option == 6:   
        match option:
            case 1:
                add_data_menu(students, subjects)
            case 2:
                edit_by_criteria(students,notes)               
            case 3:
                get_average_menu(notes, subjects) 
            case 4:
                search_by_criteria_menu(students, notes, subjects)
            case 5: 
                show_data_menu(students, subjects, notes)
        print("\nVolviendo al menú principal...\n")  
        print(main_menu) 
        option = validate_menu_option()
    finish_program()

# Ejecutamos el programa
if __name__ == '__main__':
    menu()
