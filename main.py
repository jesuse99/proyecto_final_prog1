from functions.menu import main_menu, add_students, add_professors, add_subject, finish_program, edit_by_criteria
from functions.validations import validate_menu_option   

# Declaramos e inicializamos todas las variables 

#students = []
#professors = []
#degrees = []
#subjects = []  

students = [
    [1, "Sofía", "Ingeniería en Sistemas"],
    [2, "Marcos", "Medicina"],
    [3, "Lucía", "Ingeniería"],
    [4, "Tomás", "Arquitectura"],
    [5, "Ana", "Derecho"]
]

professors = [
    [1, "Carlos Gómez", "Ingeniería", "Programación I"],
    [2, "Laura Fernández", "Derecho", "Introducción al Derecho"],
    [3, "Martín López", "Medicina", "Anatomía"],
    [4, "Ana Martínez", "Arquitectura", "Historia del Arte"],
    [5, "Sofía Ramírez", "Sistemas", "Bases de Datos"]
]

subjects = [
    [1, "Programación I", "Ingeniería en Sistemas"],
    [2, "Bases de Datos", "Ingeniería en Sistemas"],
    [3, "Anatomía", "Medicina"],
    [4, "Derecho Penal", "Derecho"],
    [5, "Macroeconomía", "Ciencias Económicas"],
    [6, "Psicología Cognitiva", "Psicología"]
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
    while not option == 7:   
        match option:
            case 1:
                add_students(students)
            case 2:
                add_professors(professors)
            case 3:
                add_subject(subjects)                
            case 4:
                print("Gestionar promedios")    
            case 5:
                print("Buscar por criterio:")  
            case 6:
                edit_by_criteria(students, professors)

        print("\nVolviendo al menú principal...\n")  
        print(main_menu) 
        option = validate_menu_option()
    finish_program()

# Ejecutamos el programa
if __name__ == '__main__':
    menu()