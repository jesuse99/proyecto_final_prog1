from functions.menu import main_menu, add_data_menu, finish_program, edit_by_criteria, show_data_menu, search_by_criteria_menu, get_average_menu
from functions.validations import validate_menu_option   

# careers = []
careers = [
    [1, "1010", "Ingeniería en Sistemas", "Facultad de Ingeniería"],          # id=1, codigo=1010, nombre=Ingeniería en Sistemas, facultad=Ingeniería
    [2, "2020", "Medicina", "Facultad de Ciencias Médicas"],                  # id=2, codigo=2020, nombre=Medicina, facultad=Ciencias Médicas
    [3, "3030", "Derecho", "Facultad de Ciencias Jurídicas"],                 # id=3, codigo=3030, nombre=Derecho, facultad=Ciencias Jurídicas
    [4, "4040", "Ciencias Económicas", "Facultad de Ciencias Económicas"],    # id=4, codigo=4040, nombre=Ciencias Económicas, facultad=Ciencias Económicas
    [5, "5050", "Psicología", "Facultad de Humanidades"],                     # id=5, codigo=5050, nombre=Psicología, facultad=Humanidades
    [6, "6060", "Arquitectura", "Facultad de Arquitectura"]                   # id=6, codigo=6060, nombre=Arquitectura, facultad=Arquitectura
]

# students = []
students = [
    [1, "1111", "Sofía Fernandez", "1010"],   # id=1, legajo=1111, nombre=Sofía Fernandez, carrera_codigo=1010 (Ingenieria en Sistemas)
    [2, "2222", "Marcos Garcia", "2020"],     # id=2, legajo=2222, nombre=Marcos Garcia, carrera_codigo=2020 (Medicina)
    [3, "3333", "Lucía Lopez", "6060"],       # id=3, legajo=3333, nombre=Lucía Lopez, carrera_codigo=4040 (Arquitectura)
    [4, "4444", "Ana Diaz", "3030"]        # id=5, legajo=5555, nombre=Ana Diaz, carrera_codigo = 3030 (Derecho)
]

# subjects = []  
subjects = [
    [1, "1532", "Programación I", "1010"],     # id=1, codigo=1532, nombre=Programación I, carrera_codigo=1010
    [2, "2897", "Bases de Datos", "1010"],     # id=2, codigo=2897, nombre=Bases de Datos, carrera_codigo=1010
    [3, "4120", "Anatomía", "2020"],           # id=3, codigo=4120, nombre=Anatomía, carrera_codigo=2020
    [4, "5784", "Derecho Penal", "3030"],      # id=4, codigo=5784, nombre=Derecho Penal, carrera_codigo=3030
    [5, "6962", "Macroeconomía", "4040"],      # id=5, codigo=6962, nombre=Macroeconomía, carrera_codigo=4040
    [6, "8459", "Psicología Cognitiva", "5050"] # id=6, codigo=8459, nombre=Psicología Cognitiva, carrera_codigo=5050
]

# notes = []
notes = [
    [1, "1532", "1111", 90],   # id=1, materia=1532 (Programación I), estudiante=1111 (Sofía Fernandez), nota=90
    [2, "2897", "1111", 80],   # id=2, materia=2897 (Bases de Datos), estudiante=1111 (Sofía Fernandez), nota=80
    [3, "4120", "2222", 70],   # id=3, materia=4120 (Anatomía), estudiante=2222 (Marcos Garcia), nota=70
    [4, "5784", "4444", 60],   # id=4, materia=5784 (Derecho Penal), estudiante=4444 (Ana Diaz), nota=60
]


def menu():
    # Menu principal del programa. Muestra las opciones y ejecuta las funciones correspondientes.
    print(main_menu)
    option = validate_menu_option()
    while not option == 6:   
        match option:
            case 1:
                add_data_menu(students, subjects, notes, careers)
            case 2:
                edit_by_criteria(students,notes, subjects)               
            case 3:
                get_average_menu(notes, subjects) 
            case 4:
                search_by_criteria_menu(students, notes, subjects, careers)
            case 5: 
                show_data_menu(students, subjects, notes, careers)
        print("\nVolviendo al menú principal...\n")  
        print(main_menu) 
        option = validate_menu_option()
    finish_program()

# Ejecutamos el programa
if __name__ == '__main__':
    menu()
