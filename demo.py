#  Dictionary Operations
my_dict = {'Date:': '11-02-20', 'Login': 'admin', 'Password': 123456789}
print(my_dict)  # My dictionary

my_dict2 = my_dict.copy()
print('my_dict2 =', my_dict2)  # Dictionary 1 copy

my_dict2.clear()
print('my_dict2 =', my_dict2)  # Clear Dictionary 2

my_dict2 = dict.fromkeys(['A', 'B'], 333)
print('my_dict2 fromkeys =', my_dict2)  # Method returns a dictionary with the specified keys and the specified value

print("my_dict2 get('B')=", my_dict2.get('B'))  # Method returns the value of the item with the specified key

print('my_dict.keys = ', my_dict.keys())  # The keys() method returns a view object.
# The view object contains the keys of the dictionary, as a list.

print('Login:', my_dict.pop('Login'))  # Method removes the specified item from the dictionary

print('my_dict.popitem = ', my_dict.popitem())  # Method removes the item that was last inserted into the dictionary
print(my_dict)

add1 = {"Login": 'ADMIN'}
my_dict.update(add1)  # Method inserts the specified items to the dictionary
print('my_dict.update = ', my_dict)

my_dict.setdefault('Password', 22222)  # Method returns the value of the item with the specified key
print('my_dict.setdefault = ', my_dict)

dict_values = my_dict.values()
print(dict_values)  # Method returns a view object. The view object contains the values of the dictionary, as a list.

my_dict['Password'] = 3333
print(my_dict) # also gets updated

del [my_dict['Password']]
print(my_dict.items())  # The items() method returns a view object.
# The view object contains the key-value pairs of the dictionary, as tuples in a list.
