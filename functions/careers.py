from utils.validations import validate_identifier, validate_int_input, validate_menu_option, validate_string_input, validate_continue, validate_existing_career
from utils.auxiliars import set_position, set_identifier
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
    if not validate_existing_career(careers,career_name, career_org):
        careers.append({ "id": pos, "codigo": career_code, "nombre": career_name, "facultad": career_org })
        set_data('careers', careers)
        print("\n [+] Carrera agregada correctamente.\n")
    else:
        print("ATENCIÓN [!] No se puede añadir carrera que ya existe.")

def add_careers(careers):
    # funcion para añadir MULTIPLES carreras a la lista careers
    print(career_menu)
    option = 's'
    while option != 'n':
        add_career(careers)
        option = validate_continue("\nDesea ingresar otra carrera? (s/n): \n")


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
        option = validate_menu_option()
        while not option == 3:   
            match option:
                case 1:
                    edit_name(careers, code)
                case 2:
                    edit_faculty(careers, code)   
            print("\nVolviendo al menú de edición de carrera...\n")  
            print(menu_edit_career) 
            option = validate_menu_option() 
    else:
        print("ATENCIÓN [!] No se puede editar una carrera que no existe.")

