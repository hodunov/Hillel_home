import json

with open('questions.json', 'r') as file:
    json_data = json.load(file)
    for item in json_data:
        if item["answer"]:
            item[""] = "ARTEM"
with open('questions.json', 'w') as file:
    json.dump(json_data, file, indent=2)


# Test

import json

with open('/path/to/josn_file.json', 'r') as file:
    json_data = json.load(file)
    for item in json_data:
        if item['ParameterKey'] in ["Shell", "Type"]:
            item['ParameterKey'] = "new value"
with open('/path/to/josn_file.json', 'w') as file:
    json.dump(json_data, file, indent=2)
