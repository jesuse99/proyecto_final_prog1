# Sistema de Calificaciones – Programación I (UADE)

**Materia:** Programación I  
**Universidad:** UADE  
**Docente:** Abel Israel Laime Huanca  
**Grupo 1 – Proyecto Final**

Integrante, Rol y Tareas 

- **Sofía Fernandez** : Team Leader > Desarrollo del sistema, testing y documentación 
- **Jesús Espinoza** : Project Manager > Desarrollo del sistema, testing y documentación 
- **Bárbara Coutinho** : Testing > Desarrollo del sistema, testing y documentación 



##  Introducción

En el ambiente educativo, la correcta administración y almacenamiento de las **notas** es fundamental para evaluar el rendimiento académico y facilitar la toma de decisiones pedagógicas.  
Este proyecto implementa un **sistema de calificaciones en consola**, desarrollado en **Python**, que permite registrar estudiantes, carreras, materias y notas, además de calcular promedios individuales y por materia.


## Objetivos

### Objetivo General
Desarrollar un sistema en consola que permita gestionar estudiantes y sus calificaciones de manera organizada, utilizando Python como herramienta principal.

### Objetivos Específicos
- Diseñar un menú interactivo que facilite la navegación por las distintas funcionalidades.  
- Permitir el registro, actualización y eliminación de estudiantes y materias.  
- Incorporar el ingreso de calificaciones en formato matricial.  
- Implementar funciones para calcular promedios individuales y globales.  
- Implementar validaciones para entradas del usuario.  
- Favorecer la comprensión y aplicación de **listas y diccionarios** en Python.  
- Iniciar el almacenamiento y persistencia de datos en archivo JSON.  


## Requisitos del proyecto

- [x] Mostrar, agregar, editar y eliminar estudiantes 
- [x] Mostrar, agregar, editar y eliminar materias 
- [x] Mostrar, agregar, editar y eliminar notas 
- [x] Mostrar, agregar, editar y eliminar carreras 
- [x] Buscar por estudiante o materia 
- [x] Calcular promedios por alumno y por materia 



##  Estructura del proyecto
```proyecto_final_prog1/
├── main.py
├── functions/
│   ├── menu.py
│   ├── auxiliars.py
│   └── validations.py
├── README.md
├── LICENSE
└── .gitignore
```


### Descripción de módulos

| Módulo | Descripción |
|--------|--------------|
| **main.py** | Punto de entrada del programa. Carga datos iniciales (carreras, materias, estudiantes y notas) y gestiona el flujo del menú principal. |
| **menu.py** | Contiene las funciones que implementan los menús interactivos de alta, edición, búsqueda, promedios y visualización. |
| **auxiliars.py** | Funciones de soporte: cálculo de promedios, filtros, generación de IDs, etc. |
| **validations.py** | Validaciones de datos: entradas del usuario, formatos, existencia de registros, etc. |



## Listas y estructuras en uso

El sistema utiliza **listas de diccionarios** como estructuras de datos temporales (simulación de base de datos):

| Entidad | Estructura | Ejemplo |
|----------|-------------|---------|
| **Students** | `{ id, legajo, nombre, carrera }` | `{ "id": 1, "legajo": 1111, "nombre": "Sofía Fernandez", "carrera": 1010 }` |
| **Subjects** | `{ id, codigo, nombre, carrera }` | `{ "id": 1, "codigo": 1532, "nombre": "Programación I", "carrera": 1010 }` |
| **Careers** | `{ id, codigo, nombre, facultad }` | `{ "id": 1, "codigo"; 1010, "nombre": "Ingeniería en Sistemas", "facultad": "Facultad de Ingeniería"]` |
| **Notes** | `{ id, materia, legajo, nota, fecha }` | `{ "id": 1, "materia": 1532, "legajo": 1111, "nota": 10, "fecha": "2025-11-02" }` |

---

## Lógica del programa

El flujo principal del sistema sigue el patrón:
Menú principal → Submenú → Acción → Validación → Resultado → Retorno al menú



##  Futuras mejoras

- Usar diccionarios para más claridad
- Guardar datos en archivos JSON   
- Agregar eliminación de registros  
- Crear interfaz gráfica  



##  Repositorio original

Proyecto base: [jesuse99/proyecto_final_prog1](https://github.com/jesuse99/proyecto_final_prog1)
