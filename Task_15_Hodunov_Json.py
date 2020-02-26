import json


def write_json(data, filename='questions.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


with open('questions.json') as json_file:
    data = json.load(json_file)

temp = data['questions']

a = {
        "q": "What is your name?",
        "answer": "Artem"
    }, {
        "q": "How old are you?",
        "answer": "25"
    }, {
        "q": "Do you like python?",
        "answer": "Yes"
    }, {
        "q": "What is the most difficult topic for you?",
        "answer": "Json"
    },{
    "q": "Please write suggestions and wishes",
    "answer": "I'm to lazy for that"
}

temp.append(a)


write_json(data)
