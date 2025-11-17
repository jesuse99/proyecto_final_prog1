░█████╗░░█████╗░██╗░░░░░██╗███████╗██╗░█████╗░░█████╗░
██╔══██╗██╔══██╗██║░░░░░██║██╔════╝██║██╔══██╗██╔══██╗ 
██║░░╚═╝███████║██║░░░░░██║█████╗░░██║██║░░╚═╝███████║
██║░░██╗██╔══██║██║░░░░░██║██╔══╝░░██║██║░░██╗██╔══██║ 
╚█████╔╝██║░░██║███████╗██║██║░░░░░██║╚█████╔╝██║░░██║  
░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝ 

## Sistema de Calificaciones – Programación I (UADE)

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
│   ├── careers.py
│   ├── notes.py
│   ├── students.py
│   └── subjects.py
├── utils/
│   ├── auxiliars.py
│   ├── filehandler.py
│   └── validations.py
├── data/
│   ├── careers.json
│   ├── notes.json
│   ├── students.json
│   └── subjects.json
├── README.md
├── LICENSE
└── .gitignore
```






## Lógica del programa

El flujo principal del sistema sigue el patrón:
Menú principal → Submenú → Acción → Validación → Resultado → Retorno al menú



##  Mejoras agregadas

- Diccionarios para más claridad
- Guardar datos en archivos JSON   
- Eliminación de registros  


##  Repositorio original

Proyecto base: [jesuse99/proyecto_final_prog1](https://github.com/jesuse99/proyecto_final_prog1)
