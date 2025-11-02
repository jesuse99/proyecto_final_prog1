from functions.validations import validate_string_input, validate_continue, validate_existing_career
from functions.auxiliars import set_position, set_identifier
from utils.data import careers
from utils.service import get_data, set_data


""" --------------------------------------------------------------------------------"""
""" ############################### MOSTRAR CARRERAS REGISTRADAS ################## """
""" --------------------------------------------------------------------------------"""

def show_careers(careers):
    # funcion para mostrar todas las carreras de la lista carreras
    print("\n=== MOSTRAR CARRERAS ===\n")
    for career in careers:
        # obtener el codigo, nombre y facultad de la carrera
        career_code = career["codigo"]
        career_name = career["nombre"]
        career_college = career["facultad"]

        print(f"Codigo: {career_code} - Nombre: {career_name} - Facultad: {career_college}")

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
        set_data('careers.json', careers)
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
