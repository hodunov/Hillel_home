data = [
    {'name': 'Bill', 'lastname': 'Boll'},
    {'name': 'Bob', 'lastname': 'Zip'},
    {'lastname': 'Fuf'},
    {'lastname': 'Albertus'},
    {'name': 'Dimon', 'lastname': 'Nomid'}
]


def get_name(dictionary):
    """ Return the value of a key in a dictionary. """
    if 'name' in dictionary.values():
        return dictionary['name']
    else:
        return dictionary['lastname']


data.sort(key=get_name)
print(data)
