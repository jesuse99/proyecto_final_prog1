def validate_menu_option():
    # Funcion para validar la opcion ingresada por el usuario en el menú. Debe ser un numero entre 1 y 8.
    option = input("Seleccione una opción: ")
    while not option.isdigit() or int(option) < 1 or int(option) > 8:
        print("Se ha ingresado una opción inválida. La opción no puede estar vacía o ser 0. Solo se permiten valores numéricos, intente nuevamente.")
        option = input("Seleccione una opción: ")
    return int(option)

def validate_int_input(message, error):
    # Funcion para validar que el input sea un numero entero mayor a 0
    int_value = input(message)
    while not int_value.isdigit() or int(int_value) < 0:
        print(error)
        int_value = input(message)
    return int(int_value)

def validate_string_input(message, error):
    # Funcion para validar que el input sea un string no vacio y que solo contenga letras
    string_value = str(input(message))
    while string_value == "" or not string_value.isalpha():
        print(error)
        string_value = str(input(message))
    return string_value

def validate_student(students, identifier):
    # Funcion para validar que el legajo no se encuentre registrado en la lista de estudiantes
    for student in students:
        if student[0] == identifier:
            print("El legajo ya existe. Ingrese otro legajo.")
            return True
    return False

def validate_continue(message):
    option = str(input(message)).lower()
    while option not in ('s', 'n'): # validamos que la opcion ingresada sea 's' o 'n'
        print("\nOpción inválida. Debe ser 's' o 'n'.\n")
        option = str(input(message)).lower()
    return option