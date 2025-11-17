from functions.menu import head_menu, main_menu, add_data_menu, edit_by_criteria, delete_data_menu, get_average_menu, search_by_criteria_menu, show_data_menu, finish_program
from utils.validations import validate_menu_option   


def menu():
    # Menu principal del programa. Muestra las opciones y ejecuta las funciones correspondientes.
    print(head_menu, main_menu, sep='\n') # Muestro las opciones del menú principal
    option = validate_menu_option() # Valido la opción ingresada por el usuario

    if option == 7: # Si se ingresa la opción 7, se finaliza el programa
        finish_program() 
        return # Salgo de la función para no ejecutar el resto del código

    match option: # Uso match-case para ejecutar la función correspondiente según la opción ingresada
        case 1:
            add_data_menu() # Llamada al menú de ingreso de datos
        case 2:
            edit_by_criteria() # Llamada al menú de edición de datos
        case 3:
            delete_data_menu() # Llamada al menú de borrado de datos                           
        case 4:
            get_average_menu() # Llamada al menú de gestión de promedios
        case 5:
            search_by_criteria_menu() # Llamada al menú de búsqueda por criterio
        case 6: 
            show_data_menu() # Llamada al menú de mostrar datos
            
    print("\nVolviendo al menú principal...\n")  
    menu() # Vuelvo a mostrar el menú principal después de ejecutar la opción seleccionada

# Ejecutamos el programa
if __name__ == '__main__':
    menu() 