# Sistema de Calificaciones – Programación I (UADE)

**Materia:** Programación I  
**Universidad:** UADE  
**Docente:** Abel Israel Laime Huanca  
**Grupo 1 – Proyecto Final**

Integrante, Rol y Tareas 

**Sofía Fernandez** : Team Leader > Desarrollo del sistema, testing y documentación 
**Jesús Espinoza** : Project Manager > Desarrollo del sistema, testing y documentación 
**Bárbara Coutinho** : Testing > Desarrollo del sistema, testing y documentación 



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
- Iniciar el almacenamiento y persistencia de datos en archivo CSV o JSON.  


## Requisitos del proyecto

 Mostrar, agregar, editar y eliminar estudiantes 
 Mostrar, agregar, editar y eliminar materias 
 Mostrar, agregar, editar y eliminar notas 
 Mostrar, agregar, editar y eliminar carreras 
 Buscar por estudiante o materia 
 Calcular promedios por alumno y por materia 



##  Estructura del proyecto
proyecto_final_prog1/
├── main.py
├── functions/
│   ├── menu.py
│   ├── auxiliars.py
│   └── validations.py
├── README.md
├── LICENSE
└── .gitignore



### Descripción de módulos

| Módulo | Descripción |
|--------|--------------|
| **main.py** | Punto de entrada del programa. Carga datos iniciales (carreras, materias, estudiantes y notas) y gestiona el flujo del menú principal. |
| **menu.py** | Contiene las funciones que implementan los menús interactivos de alta, edición, búsqueda, promedios y visualización. |
| **auxiliars.py** | Funciones de soporte: cálculo de promedios, filtros, generación de IDs, etc. |
| **validations.py** | Validaciones de datos: entradas del usuario, formatos, existencia de registros, etc. |



## Listas y estructuras en uso

El sistema utiliza **listas de listas** como estructuras de datos temporales (simulación de base de datos):

| Entidad | Estructura | Ejemplo |
|----------|-------------|---------|
| **Students** | `[id, legajo, nombre, codigo_carrera]` | `[1, "1111", "Sofía Fernandez", "1010"]` |
| **Subjects** | `[id, codigo_materia, nombre, codigo_carrera]` | `[1, "1532", "Programación I", "1010"]` |
| **Careers** | `[id, codigo_carrera, nombre, facultad]` | `[1, "1010", "Ingeniería en Sistemas", "Facultad de Ingeniería"]` |
| **Notes** | `[id, codigo_materia, legajo_estudiante, nota]` | `[1, "1532", "1111", 90]` |

---

## Lógica del programa

El flujo principal del sistema sigue el patrón:
Menú principal → Submenú → Acción → Validación → Resultado → Retorno al menú



##  Futuras mejoras

- Usar diccionarios para más claridad  
- Guardar datos en archivos CSV o JSON  
- Agregar eliminación de registros  
- Crear interfaz gráfica  



##  Repositorio original

Proyecto base: [jesuse99/proyecto_final_prog1](https://github.com/jesuse99/proyecto_final_prog1)
