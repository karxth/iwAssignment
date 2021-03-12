"""Find a package in the Python standard library for dealing with
JSON. Import the library module and inspect the attributes of the
module. Use the help function to learn more about how to use the
module. Serialize a dictionary mapping 'name' to your name and 'age'
to your age, to a JSON string. Deserialize the JSON back into
Python."""

import json

information = {'name': 'Mr.Robot', 'age':25}
print(f'Dictionary: {information}')

serialize_json_string = json.dumps(information)
print(f'After Serializing into JSON string {serialize_json_string}')

deserialize_json_string = json.loads(serialize_json_string)
print(f'After Deserializing into JSON string {deserialize_json_string}')
