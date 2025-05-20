# JSON Exploder

## Description
JSON Exploder is a Python tool designed to transform nested JSON structures into flat records. This utility allows you to "explode" elements within a list in a JSON file, generating multiple individual records that inherit common fields from the upper level.

## System Requirements

- Python 3.8 or higher
- No external libraries required (uses only Python standard modules)

## Installation

No specific installation is required. Simply clone or download this repository:

```bash
git clone https://github.com/user/json_exploder.git
cd json_exploder
```

## Usage Example

Given an `input.json` file with the following content:

```json
{
  "age": 18,
  "course": "10th Grade",
  "students": [
    {"name": "Jose", "grade": 8.5},
    {"name": "Luis", "grade": 7.2},
    {"name": "Ana", "grade": 9.0}
  ]
}
```

You can run:

```bash
python main.py -i input.json -o output.json -e students -c age,course --overwrite
```

And you will get an `output.json` file with:

```json
[
  {"age": 18, "course": "10th Grade", "name": "Jose", "grade": 8.5},
  {"age": 18, "course": "10th Grade", "name": "Luis", "grade": 7.2},
  {"age": 18, "course": "10th Grade", "name": "Ana", "grade": 9.0}
]
```

## Parameter Configuration

The program accepts the following parameters:

| Parameter | Description |
|-----------|-------------|
| `-i`, `--input` | Path to the input JSON file (required) |
| `-o`, `--output` | Path to the output JSON file (required) |
| `-e`, `--explode` | Field containing the list to explode (required) |
| `-c`, `--common-fields` | List of common fields to inherit, comma-separated (required) |
| `--overwrite` | Overwrite output file if it exists (optional) |

## Error Handling

The program includes validations for:
- The existence of the input file
- Valid JSON format
- The existence of the field to explode
- Verification that the field to explode is a list
- Overwriting existing files (with the corresponding option)

## Extensibility

The code is designed to be easily extensible. Possible future improvements may include:
- Support for multiple nesting levels
- Multiple fields to explode simultaneously
- Format options for the output file

## License

This project is licensed under the [MIT License](LICENSE).

---

Note: This project was created with the assistance of an AI tool, in collaboration with a human developer.