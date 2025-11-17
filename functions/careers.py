from utils.validations import validate_existing, validate_identifier, validate_int_input, validate_submenu_option, validate_string_input, validate_continue, validate_existing_career
from utils.auxiliars import get_average, get_by_career, get_notes_by_career, get_notes_by_career_student, set_position, set_identifier
from utils.filehandler import get_data, set_data

careers = get_data('careers')

""" --------------------------------------------------------------------------------"""
""" ############################### MOSTRAR CARRERAS REGISTRADAS ################## """
""" --------------------------------------------------------------------------------"""

def show_careers(careers):
    # funcion para mostrar todas las carreras de la lista carreras
    print("\n=== MOSTRAR CARRERAS ===\n")
    formatted_row = '{:<8} {:<24} {:<30}'
    print("=================================="*2)
    print(formatted_row.format("Codigo", "Nombre","Facultad"))
    print("=================================="*2)
    for career in careers:
        # obtener el codigo, nombre y facultad de la carrera
        career_code = career["codigo"]
        career_name = career["nombre"]
        career_college = career["facultad"]

        data_row = [career_code, career_name, career_college]
        print(formatted_row.format(*data_row))

""" --------------------------------------------------------------------------------"""
""" ############################### AÑADIR CARRERAS ############################### """
""" --------------------------------------------------------------------------------"""

career_menu = """
=== AGREGAR CARRERAS ===
"""

def add_career(careers):
    # Función para añadir UNA carrera a la lista careers
    pos = set_position(careers)
    career_code = set_identifier(careers)
    career_name = validate_string_input("- Ingrese el nombre de la carrera: ", "ERROR [!]Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    career_org = validate_string_input("- Ingrese el nombre de la facultad: ", "ERROR [!]Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    if not validate_existing_career(careers, career_name):
        careers.append({ "id": pos, "codigo": career_code, "nombre": career_name, "facultad": career_org })
        set_data('careers', careers)
        print("\n [+] Carrera agregada correctamente.\n")
    else:
        print("ATENCIÓN [!] No se puede añadir carrera que ya existe.")

def add_careers(careers):
    # funcion para añadir MULTIPLES carreras a la lista careers
    print(career_menu) # Muestro el menú de agregar carreras
    add_career(careers) # Llamada a la función para agregar una carrera
    option = validate_continue("\nDesea ingresar otra carrera? (s/n): \n") # Valido si el usuario quiere agregar otra carrera
    if option == 's': # Si el usuario quiere agregar otra carrera, entonces llamo a la función recursivamente
        add_careers(careers) # Llamada recursiva para agregar otra carrera

menu_edit_career = """
=== EDITAR CARRERA ===

=== Opciones de Edición ===

1. Editar nombre
2. Editar facultad
3. Volver
"""

""" -------------------------------------------------------------------------------"""
""" ############################### EDITAR NOMBRE ############################### """
""" -------------------------------------------------------------------------------"""

def edit_name(data_list, code):
    # funcion para editar el nombre de una carrera de la lista si existe
    name = validate_string_input("- Ingrese el nuevo nombre: ", "ERROR [!] Se ha ingresado un nombre inválido. El nombre solo debe contener letras y no puede estar vacío, intente nuevamente.")
    for resource in data_list:
        if int(resource["codigo"]) == int(code):
            resource["nombre"] = name
    set_data('careers', data_list)
    print("\nNombre editado correctamente.\n")

""" -------------------------------------------------------------------------------"""
""" ############################### EDITAR FACULTAD ############################### """
""" -------------------------------------------------------------------------------"""

def edit_faculty(data_list, code): 
    # funcion para editar la carrera de una carrera de la lista si existe
    degree = validate_string_input("- Ingrese la nueva facultad: ", "ERROR [!] Se ha ingresado una facultad inválida. La facultad solo debe contener letras y no puede estar vacía, intente nuevamente.")
    for resource in data_list:
        if int(resource["codigo"]) == int(code):
            resource["facultad"] = degree
    set_data('careers', data_list)
    print("\nFacultad editada correctamente.\n")

""" ---------------------------------------------------------------------------------------"""
""" ############################### MENÚ EDITAR CARRERA ############################### """
""" ---------------------------------------------------------------------------------------"""

def edit_career(careers):
    # funcion para editar una carrera de la lista de carrera si existe
    code = validate_int_input("\n- Ingrese el codigo de la carrera que desea editar: ", "ERROR [!] Se ha ingresado un codigo inválido. El codigo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_identifier(careers, code): 
        # si el legajo existe, se procede a la edicion
        print(f"\nEditando carrera con codigo: {code}")
        print(menu_edit_career)
        option = validate_submenu_option()
        while not option == 3:   
            match option:
                case 1:
                    edit_name(careers, code)
                case 2:
                    edit_faculty(careers, code)   
            print("\nVolviendo al menú de edición de carrera...\n")  
            print(menu_edit_career) 
            option = validate_submenu_option() 
    else:
        print("ATENCIÓN [!] No se puede editar una carrera que no existe.")


menu_delete_career = """
=== ELIMINAR CARRERA ===
"""

""" -----------------------------------------------------------------------------------"""
""" ############################### ELIMINAR CARRERA ################################# """
""" -----------------------------------------------------------------------------------"""

def delete_career(careers):
    # Funcion para eliminar una carrera a la lista de carreras
    career_code = validate_int_input("\n- Ingrese el codigo de la carrera que desea eliminar: ", "ERROR [!] Se ha ingresado un codigo inválido. El codigo no puede ser 0 y solo se permiten valores numéricos, intente nuevamente.")
    if validate_identifier(careers, career_code): 
            career = get_by_career(careers, career_code) # obtenemos la carrera por el codigo 
            careers.remove(career) # eliminamos la carrera de la lista
            set_data('careers', careers)
            print("\n [x] Carrera eliminada correctamente.\n")
    else:
        print("ATENCIÓN [!] No se puede eliminar una carrera que no existe.")

def delete_careers(careers):
    # Funcion para eliminar MULTIPLES carreras de la lista de carreras
    print(menu_delete_career) # Muestro el menú de eliminar carreras
    delete_career(careers) # Llamada a la función para eliminar una carrera
    option = validate_continue("\nDesea eliminar otra carrera? (s/n): \n") 
    if option == 's': 
        delete_career(careers) # Llamada recursiva para eliminar otra carrera 

""" ----------------------------------------------------------------------------------------------"""
""" ############################### CALCULAR PROMEDIO POR CARRERA ############################### """
""" ----------------------------------------------------------------------------------------------"""

menu_average_title = """
=== PROMEDIO POR CARRERA ===
"""

def average_career(notes, careers, subjects):
    # funcion para calcular el promedio de notas de una carrera
    print(menu_average_title)
    career_identifier = validate_int_input("- Ingrese el código de la carrera para calcular el promedio de notas: ", "ERROR [!] Se ha ingresado un codigo inválido. El codigo debe ser un valor numérico, intente nuevamente.")
    if validate_identifier(careers, career_identifier):
        career_notes = get_notes_by_career(subjects, notes, career_identifier)
        career_data = get_by_career(careers, career_identifier)
        if career_notes:
            average = get_average(career_notes)
            if average:
                print(f"\nEl promedio de notas de la carrera {career_data["nombre"]} es: {average:.2f}\n")
        else:
            print(f"\nATENCIÓN [!] No se encontraron notas para la carrera con ID {career_identifier}.\n")
    else:
        print(f"\nATENCIÓN [!] No se encontro una carrera con codigo {career_identifier}.\n")


""" ----------------------------------------------------------------------------------------------"""
""" ############################### CALCULAR PROMEDIO DE ESTUDIANTE POR CARRERA ################# """
""" ----------------------------------------------------------------------------------------------"""

menu_student_average_title = """
=== PROMEDIO DE ESTUDIANTE POR CARRERA ===
"""

def student_average_career(notes, careers, subjects):
    # funcion para calcular el promedio de notas de un estudiante por carrera
    print(menu_student_average_title)
    identifier = validate_int_input("\n- Ingrese el legajo del estudiante para calcular su promedio de notas: ", "ERROR [!] Se ha ingresado un legajo inválido. El legajo debe ser un valor numérico, intente nuevamente.")
    if validate_existing(notes, identifier):
        career_identifier = validate_int_input("- Ingrese el código de la carrera para calcular el promedio de notas: ", "ERROR [!] Se ha ingresado un codigo inválido. El codigo debe ser un valor numérico, intente nuevamente.")
        if validate_identifier(careers, career_identifier):
            career_notes = get_notes_by_career_student(subjects, notes, career_identifier, identifier)
            career_data = get_by_career(careers, career_identifier)
            if career_notes:
                average = get_average(career_notes)
                if average:
                    print(f"\nEl promedio de notas del estudiante con legajo {identifier} en la carrera {career_data["nombre"]} es: {average:.2f}\n")
            else:
                print(f"\nATENCIÓN [!] No se encontraron notas para la carrera  {career_identifier} del estudiante con legajo {identifier}.\n")
        else:
            print(f"\nATENCIÓN [!] No se encontro una carrera con codigo {career_identifier}.\n")
    else:
        print(f"\nATENCIÓN [!] No se encontro un estudiante con legajo {identifier}.\n")

