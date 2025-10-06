from functions.menu import main_menu, add_data_menu, finish_program, edit_by_criteria, show_data_menu, search_by_criteria_menu, get_average_menu
from functions.validations import validate_menu_option   

# Declaramos e inicializamos todas las variables 

# careers = []
# students = []
# subjects = []  
# notes = []

careers = [
    [1, "1010", "Ingeniería en Sistemas", "Facultad de Ingeniería"],          # id=1, codigo=1010, nombre=Ingeniería en Sistemas, facultad=Ingeniería
    [2, "2020", "Medicina", "Facultad de Ciencias Médicas"],                  # id=2, codigo=2020, nombre=Medicina, facultad=Ciencias Médicas
    [3, "3030", "Derecho", "Facultad de Ciencias Jurídicas"],                 # id=3, codigo=3030, nombre=Derecho, facultad=Ciencias Jurídicas
    [4, "4040", "Ciencias Económicas", "Facultad de Ciencias Económicas"],    # id=4, codigo=4040, nombre=Ciencias Económicas, facultad=Ciencias Económicas
    [5, "5050", "Psicología", "Facultad de Humanidades"],                     # id=5, codigo=5050, nombre=Psicología, facultad=Humanidades
    [6, "6060", "Arquitectura", "Facultad de Arquitectura"]                   # id=6, codigo=6060, nombre=Arquitectura, facultad=Arquitectura
]

students = [
    [1, "1111", "Sofía", "Ingeniería en Sistemas"],   # id=1, legajo=1111, nombre=Sofía, carrera=Ingeniería en Sistemas
    [2, "2222", "Marcos", "Medicina"],                # id=2, legajo=2222, nombre=Marcos, carrera=Medicina
    [3, "3333", "Lucía", "Ingeniería"],               # id=3, legajo=3333, nombre=Lucía, carrera=Ingeniería
    [4, "4444", "Tomás", "Arquitectura"],             # id=4, legajo=4444, nombre=Tomás, carrera=Arquitectura
    [5, "5555", "Ana", "Derecho"]                     # id=5, legajo=5555, nombre=Ana, carrera=Derecho
]

subjects = [
    [1, "1532", "Programación I", "Ingeniería en Sistemas"],     # id=1, codigo=1532, nombre=Programación I, carrera=Ingeniería en Sistemas
    [2, "2897", "Bases de Datos", "Ingeniería en Sistemas"],     # id=2, codigo=2897, nombre=Bases de Datos, carrera=Ingeniería en Sistemas
    [3, "4120", "Anatomía", "Medicina"],                        # id=3, codigo=4120, nombre=Anatomía, carrera=Medicina
    [4, "5784", "Derecho Penal", "Derecho"],                    # id=4, codigo=5784, nombre=Derecho Penal, carrera=Derecho
    [5, "6962", "Macroeconomía", "Ciencias Económicas"],         # id=5, codigo=6962, nombre=Macroeconomía, carrera=Ciencias Económicas
    [6, "8459", "Psicología Cognitiva", "Psicología"]            # id=6, codigo=8459, nombre=Psicología Cognitiva, carrera=Psicología
]

notes = [
    [1, "1532", "1111", 90],   # id=1, materia=1532 (Programación I), estudiante=1111 (Sofía), nota=90
    [2, "2897", "1111", 80],   # id=2, materia=2897 (Bases de Datos), estudiante=1111 (Sofía), nota=80
    [3, "4120", "2222", 70],   # id=3, materia=4120 (Anatomía), estudiante=2222 (Marcos), nota=70
    [4, "5784", "3333", 60],   # id=4, materia=5784 (Derecho Penal), estudiante=3333 (Lucía), nota=60
    [5, "1532", "4444", 100]   # id=5, materia=1532 (Programación I), estudiante=4444 (Tomás), nota=100
]


def menu():
    # Menu principal del programa. Muestra las opciones y ejecuta las funciones correspondientes.
    print(main_menu)
    option = validate_menu_option()
    while not option == 6:   
        match option:
            case 1:
                add_data_menu(students, subjects, notes)
            case 2:
                edit_by_criteria(students,notes, subjects)               
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
