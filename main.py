from functions.menu import main_menu, add_data_menu, finish_program, edit_by_criteria, show_data_menu, search_by_criteria_menu, get_average_menu
from functions.validations import validate_menu_option   


def menu():
    # Menu principal del programa. Muestra las opciones y ejecuta las funciones correspondientes.
    print(main_menu)
    option = validate_menu_option()
    while not option == 6:   
        match option:
            case 1:
                add_data_menu()
            case 2:
                edit_by_criteria()               
            case 3:
                get_average_menu() 
            case 4:
                search_by_criteria_menu()
            case 5: 
                show_data_menu()
        print("\nVolviendo al menú principal...\n")  
        print(main_menu) 
        option = validate_menu_option()
    finish_program()

# Ejecutamos el programa
if __name__ == '__main__':
    menu()
