from functions.menu import main_menu, add_students, add_subject, search_students, search_subjects, finish_program
from functions.validations import validate_menu_option   

# Declaramos e inicializamos todas las variables 
students = []
subjects = []
notes = []


def menu():
    # Menu principal del programa. Muestra las opciones y ejecuta las funciones correspondientes.
    print(main_menu)
    option = validate_menu_option()
    while not option == 8:   
        match option:
            case 1:
                add_students(students)
            case 2:
                add_subject(subjects)           
            case 3:
                print("Ingresar notas")        
            case 4:
                print("Mostrar promedio por materia")        
            case 5:
                print("Mostrar promedio por estudiante")      
            case 6:
                search_students(students)        
            case 7:
                search_subjects(subjects)        
        print("\nVolviendo al menú principal...\n")  
        print(main_menu) 
        option = validate_menu_option()
    finish_program()

# Ejecutamos el programa
if __name__ == '__main__':
    menu()