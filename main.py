#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JSON Exploder

Este script permite realizar un "explode" sobre estructuras tipo JSON,
transformando elementos anidados en listas en múltiples registros planares
que heredan los campos comunes.
"""

import json
import argparse
import os
import sys
from typing import Dict, List, Any, Union


def load_json_file(file_path: str) -> Dict:
    """
    Carga un archivo JSON y devuelve su contenido como un diccionario.

    Args:
        file_path: Ruta al archivo JSON de entrada.

    Returns:
        Diccionario con el contenido del archivo JSON.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        json.JSONDecodeError: Si el archivo no tiene un formato JSON válido.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: El archivo de entrada '{file_path}' no existe.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: El archivo '{file_path}' no contiene un JSON válido.")
        sys.exit(1)
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
        sys.exit(1)


def save_json_file(file_path: str, data: List[Dict], overwrite: bool = False) -> None:
    """
    Guarda datos en un archivo JSON.

    Args:
        file_path: Ruta donde se guardará el archivo JSON.
        data: Datos a guardar en formato de lista de diccionarios.
        overwrite: Si es True, sobrescribe el archivo si ya existe.

    Raises:
        FileExistsError: Si el archivo ya existe y overwrite es False.
    """
    if os.path.exists(file_path) and not overwrite:
        print(f"Error: El archivo de salida '{file_path}' ya existe. Use la opción '--overwrite' para sobrescribirlo.")
        sys.exit(1)
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print(f"Archivo de salida guardado exitosamente en: {file_path}")
    except Exception as e:
        print(f"Error al guardar el archivo de salida: {str(e)}")
        sys.exit(1)


def explode_json(data: Dict, explode_field: str, common_fields: List[str]) -> List[Dict]:
    """
    Explota un campo de tipo lista en un JSON, generando registros planares.

    Args:
        data: Diccionario que contiene los datos JSON.
        explode_field: Nombre del campo que contiene la lista a explotar.
        common_fields: Lista de campos comunes que deben heredarse.

    Returns:
        Lista de diccionarios con los registros explotados.

    Raises:
        KeyError: Si el campo a explotar no existe en el JSON.
        TypeError: Si el campo a explotar no es una lista.
    """
    # Verificar que el campo a explotar exista
    if explode_field not in data:
        print(f"Error: El campo '{explode_field}' no existe en el JSON de entrada.")
        sys.exit(1)
    
    # Verificar que el campo a explotar sea una lista
    if not isinstance(data[explode_field], list):
        print(f"Error: El campo '{explode_field}' no es una lista.")
        sys.exit(1)
    
    # Crear diccionario con los campos comunes
    common_data = {}
    for field in common_fields:
        if field in data:
            common_data[field] = data[field]
        else:
            print(f"Advertencia: El campo común '{field}' no existe en el JSON de entrada.")
    
    # Realizar el explode
    result = []
    for item in data[explode_field]:
        if not isinstance(item, dict):
            print(f"Advertencia: Se encontró un elemento no diccionario en '{explode_field}'. Se omitirá.")
            continue
        
        # Combinar campos comunes con el elemento de la lista
        exploded_item = common_data.copy()
        exploded_item.update(item)
        result.append(exploded_item)
    
    return result


def parse_arguments() -> argparse.Namespace:
    """
    Parsea los argumentos de línea de comandos.

    Returns:
        Namespace con los argumentos parseados.
    """
    parser = argparse.ArgumentParser(
        description='JSON Exploder - Transforma elementos anidados en JSON a múltiples registros planares.'
    )
    
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Ruta del archivo JSON de entrada.'
    )
    
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Ruta del archivo JSON de salida.'
    )
    
    parser.add_argument(
        '-e', '--explode',
        required=True,
        help='Campo que contiene la lista a explotar.'
    )
    
    parser.add_argument(
        '-c', '--common-fields',
        required=True,
        help='Lista de campos comunes a heredar, separados por comas.'
    )
    
    parser.add_argument(
        '--overwrite',
        action='store_true',
        help='Sobrescribir el archivo de salida si ya existe.'
    )
    
    return parser.parse_args()


def main() -> None:
    """Función principal del programa."""
    # Parsear argumentos
    args = parse_arguments()
    
    # Convertir la lista de campos comunes a una lista
    common_fields = [field.strip() for field in args.common_fields.split(',')]
    
    # Cargar datos del archivo JSON
    data = load_json_file(args.input)
    
    # Realizar el explode
    try:
        result = explode_json(data, args.explode, common_fields)
    except Exception as e:
        print(f"Error al procesar el JSON: {str(e)}")
        sys.exit(1)
    
    # Guardar el resultado
    save_json_file(args.output, result, args.overwrite)


if __name__ == "__main__":
    main()