def validate_option():
    # Funcion para validar la opcion ingresada por el usuario. Debe ser un numero entre 1 y 8.
    option = input("Seleccione una opcion: ")
    while not option.isdigit() or option < 1 or option > 8:
        print("Opcion incorrecta, intente nuevamente")
        option = input("Seleccione una opcion: ")
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

def existing_student(students, identifier):
    # Funcion para validar que el legajo no se encuentre registrado en la lista de estudiantes
    for student in students:
        if student[0] == identifier:
            print("El legajo ya existe. Ingrese otro legajo.")
            return True
    return False