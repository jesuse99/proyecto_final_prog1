from functions.menu import main_menu, add_data_menu, finish_program, edit_by_criteria, show_data_menu, search_by_criteria_menu, get_average_menu
from utils.validations import validate_menu_option   


def menu():
    # Menu principal del programa. Muestra las opciones y ejecuta las funciones correspondientes.
    print(main_menu) # Muestro las opciones del menú principal
    option = validate_menu_option() # Valido la opción ingresada por el usuario

    if option == 6: # Si se ingresa la opción 6, se finaliza el programa
        finish_program() 
        return # Salgo de la función para no ejecutar el resto del código

    match option: # Uso match-case para ejecutar la función correspondiente según la opción ingresada
        case 1:
            add_data_menu() # Llamada al menú de ingreso de datos
        case 2:
            edit_by_criteria() # Llamada al menú de edición de datos              
        case 3:
            get_average_menu() # Llamada al menú de gestión de promedios
        case 4:
            search_by_criteria_menu() # Llamada al menú de búsqueda por criterio
        case 5: 
            show_data_menu() # Llamada al menú de mostrar datos
            
    print("\nVolviendo al menú principal...\n")  
    menu() # Vuelvo a mostrar el menú principal después de ejecutar la opción seleccionada

# Ejecutamos el programa
if __name__ == '__main__':
    menu() 