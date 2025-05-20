## Extensibilidad

El código está diseñado para ser fácilmente extensible. Posibles mejoras futuras pueden incluir:
- Soporte para múltiples niveles de anidamiento
- Múltiples campos a explotar simultáneamente
- Opciones de formato para el archivo de salida# JSON Exploder

## Descripción
JSON Exploder es una herramienta en Python diseñada para transformar estructuras JSON anidadas en registros planares. Esta utilidad permite "explotar" elementos dentro de una lista en un JSON, generando múltiples registros individuales que heredan los campos comunes del nivel superior.

## Requisitos del sistema

- Python 3.8 o superior
- No se requieren bibliotecas externas (usa únicamente módulos estándar de Python)

## Instalación

No se requiere instalación específica. Simplemente clone o descargue este repositorio:

```bash
git clone https://github.com/usuario/json_exploder.git
cd json_exploder
```

## Ejemplo de uso

Teniendo un archivo `input.json` con un objeto individual:

```json
{
  "edad": 18,
  "curso": "4º ESO",
  "alumnos": [
    {"nombre": "Jose", "nota": 8.5},
    {"nombre": "Luis", "nota": 7.2},
    {"nombre": "Ana", "nota": 9.0}
  ]
}
```

O con una colección de objetos:

```json
[
  {
    "edad": 18,
    "curso": "4º ESO",
    "alumnos": [
      {"nombre": "Jose", "nota": 8.5},
      {"nombre": "Luis", "nota": 7.2}
    ]
  },
  {
    "edad": 19,
    "curso": "1º Bachillerato",
    "alumnos": [
      {"nombre": "Ana", "nota": 9.0},
      {"nombre": "Carlos", "nota": 8.3}
    ]
  }
]
```

Puedes ejecutar:

```bash
python main.py -i input.json -o output.json -e alumnos -c edad,curso --overwrite
```

Y obtendrás un archivo `output.json` con todos los registros explotados:

```json
[
  {"edad": 18, "curso": "4º ESO", "nombre": "Jose", "nota": 8.5},
  {"edad": 18, "curso": "4º ESO", "nombre": "Luis", "nota": 7.2},
  {"edad": 19, "curso": "1º Bachillerato", "nombre": "Ana", "nota": 9.0},
  {"edad": 19, "curso": "1º Bachillerato", "nombre": "Carlos", "nota": 8.3}
]
```

## Configuración de parámetros

El programa acepta los siguientes parámetros:

| Parámetro | Descripción |
|-----------|-------------|
| `-i`, `--input` | Ruta del archivo JSON de entrada (requerido) |
| `-o`, `--output` | Ruta del archivo JSON de salida (requerido) |
| `-e`, `--explode` | Campo que contiene la lista a explotar (requerido) |
| `-c`, `--common-fields` | Lista de campos comunes a heredar, separados por comas (requerido) |
| `--overwrite` | Sobrescribir el archivo de salida si ya existe (opcional) |

## Manejo de errores

El programa incluye validaciones para:
- La existencia del archivo de entrada
- El formato válido del JSON
- La existencia del campo a explotar
- Verificar que el campo a explotar sea una lista
- Sobrescritura de archivos existentes (con la opción correspondiente)

## Características principales

- **Procesamiento flexible**: Maneja tanto objetos JSON individuales como colecciones (arrays) de objetos
- **Heredar campos comunes**: Permite especificar qué campos del nivel superior se deben heredar
- **Configuración por línea de comandos**: Interfaz fácil de usar con múltiples opciones
- **Validación robusta**: Comprueba la estructura del JSON y maneja errores adecuadamente


## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).