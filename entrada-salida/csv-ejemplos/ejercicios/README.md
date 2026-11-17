# Curso práctico: manejo de ficheros CSV con Python

Este paquete contiene 12 ejemplos progresivos para trabajar con archivos CSV usando
el módulo `csv` de la biblioteca estándar de Python. No es necesario instalar paquetes.

## Contenido

- `alumnos.csv`: fichero de entrada con 20 alumnos y las columnas `nombre`, `edad` y `nota`.
- `01_leer_csv.py`: lectura básica con `csv.reader`.
- `02_leer_sin_cabecera.py`: omitir la cabecera y convertir tipos de datos.
- `03_crear_csv.py`: crear un CSV con `csv.writer`.
- `04_anadir_registro.py`: añadir una fila con el modo `a`.
- `05_dictreader.py`: leer filas como diccionarios.
- `06_dictwriter.py`: escribir diccionarios con `csv.DictWriter`.
- `07_calcular_media.py`: calcular la media de las notas.
- `08_aprobados.py`: clasificar alumnos según su nota.
- `09_buscar_alumno.py`: buscar un alumno por nombre.
- `10_generar_aprobados.py`: crear un CSV nuevo con los aprobados.
- `11_mejor_nota.py`: localizar la nota más alta.
- `12_separador_punto_y_coma.py`: trabajar con el delimitador `;`.

## Cómo ejecutar los ejemplos

1. Descomprime el ZIP.
2. Abre una terminal en la carpeta `curso_csv_python`.
3. Ejecuta, por ejemplo:

   ```bash
   python 01_leer_csv.py
   ```

4. Repite con los demás archivos.

Los ejemplos que leen `alumnos.csv` deben ejecutarse desde esta carpeta, donde se encuentra
el CSV de entrada. Los ejemplos 03 y 04 están relacionados: ejecuta primero el 03 para crear
`productos.csv` y después el 04 para añadir un producto.

## Conceptos importantes

### Abrir y cerrar ficheros

Se recomienda `with open(...) as fichero` porque cierra el fichero automáticamente,
incluso si se produce un error.

### Modos de apertura

- `r`: lectura.
- `w`: escritura; crea el fichero o sobrescribe el contenido existente.
- `a`: añade contenido al final.

### Funciones del módulo csv

- `csv.reader(fichero)`: devuelve cada fila como una lista.
- `csv.writer(fichero)`: permite escribir filas con `writerow` o `writerows`.
- `csv.DictReader(fichero)`: devuelve cada fila como un diccionario.
- `csv.DictWriter(fichero, fieldnames=...)`: escribe diccionarios.
- `writeheader()`: escribe los nombres de las columnas.

### Parámetros habituales

- `encoding="utf-8"`: permite manejar correctamente caracteres como á, é y ñ.
- `newline=""`: es la forma recomendada al abrir CSV para que el módulo `csv` gestione
  correctamente los saltos de línea.
- `delimiter=";"`: permite indicar que el separador es punto y coma.

### Tipos de datos

El módulo `csv` devuelve los valores como cadenas de texto. Convierte explícitamente
los valores cuando necesites operar con ellos:

```python
edad = int(alumno["edad"])
nota = float(alumno["nota"])
```

## Actividades de ampliación

1. Cuenta cuántos alumnos hay en `alumnos.csv`.
2. Calcula la nota media solo de los aprobados.
3. Muestra los alumnos cuya nota sea superior a la media de la clase.
4. Busca al alumno con la nota más baja.
5. Ordena los alumnos por nota y guarda el resultado en `alumnos_ordenados.csv`.
6. Añade una columna llamada `resultado` con los valores `APROBADO` o `SUSPENSO`.
7. Controla el caso en que el fichero no exista usando `try/except FileNotFoundError`.
8. Crea un menú que permita listar, buscar y añadir alumnos.

## Requisitos

Python 3.8 o superior. Solo se utiliza la biblioteca estándar.
