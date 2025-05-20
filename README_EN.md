Extensibility
The code is designed to be easily extensible. Possible future improvements may include:

Support for multiple nesting levels
Multiple fields to explode simultaneously
Format options for the output file# JSON Exploder
Description
JSON Exploder is a Python tool designed to transform nested JSON structures into flat records. This utility allows you to "explode" elements within a list in a JSON file, generating multiple individual records that inherit common fields from the upper level.

System Requirements
Python 3.8 or higher
No external libraries required (uses only Python standard modules)
Installation
No specific installation is required. Simply clone or download this repository:

bash
git clone https://github.com/albertoleonrd/json_exploder.git
cd json_exploder
Usage Example
Given an input.json file with an individual object:

json
{
  "age": 18,
  "course": "10th Grade",
  "students": [
    {"name": "Jose", "grade": 8.5},
    {"name": "Luis", "grade": 7.2},
    {"name": "Ana", "grade": 9.0}
  ]
}
Or with a collection of objects:

json
[
  {
    "age": 18,
    "course": "10th Grade",
    "students": [
      {"name": "Jose", "grade": 8.5},
      {"name": "Luis", "grade": 7.2}
    ]
  },
  {
    "age": 19,
    "course": "11th Grade",
    "students": [
      {"name": "Ana", "grade": 9.0},
      {"name": "Carlos", "grade": 8.3}
    ]
  }
]
You can run:

bash
python main.py -i input.json -o output.json -e students -c age,course --overwrite
And you will get an output.json file with all exploded records:

json
[
  {"age": 18, "course": "10th Grade", "name": "Jose", "grade": 8.5},
  {"age": 18, "course": "10th Grade", "name": "Luis", "grade": 7.2},
  {"age": 19, "course": "11th Grade", "name": "Ana", "grade": 9.0},
  {"age": 19, "course": "11th Grade", "name": "Carlos", "grade": 8.3}
]
Parameter Configuration
The program accepts the following parameters:

Parameter	Description
-i, --input	Path to the input JSON file (required)
-o, --output	Path to the output JSON file (required)
-e, --explode	Field containing the list to explode (required)
-c, --common-fields	List of common fields to inherit, comma-separated (required)
--overwrite	Overwrite output file if it exists (optional)
Error Handling
The program includes validations for:

The existence of the input file
Valid JSON format
The existence of the field to explode
Verification that the field to explode is a list
Overwriting existing files (with the corresponding option)
Key Features
Flexible Processing: Handles both individual JSON objects and collections (arrays) of objects
Inherit Common Fields: Allows you to specify which fields from the upper level should be inherited
Command-line Configuration: Easy-to-use interface with multiple options
Robust Validation: Checks JSON structure and handles errors appropriately
License
This project is licensed under the MIT License.

Note: This project was created with the assistance of an AI tool, in collaboration with a human developer.

