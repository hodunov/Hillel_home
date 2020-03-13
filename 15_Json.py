import json

with open('questions.json', 'r') as file:
    json_data = json.load(file)
    for each in json_data['questions']:
        print(each["q"])
        each["answer"] = str(input("Your answer- "))
    with open('questions.json', 'w') as f:
        json.dump(json_data, f, indent=2)
