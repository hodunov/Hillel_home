# Sets
set_a = set('Hello World')
print(set_a)

print('')

set_b = {5, 3, 4, 1, '2', 'Boring', 'Company'}
print(set_b)

print(set_b.isdisjoint('2'))  # False if two sets are not disjoint sets
print(set_b.isdisjoint('1'))  # True if two sets are disjoint sets

print('')

set_c = set.copy(set_b)  # Set copy
print(set_c)
print(set_b == set_c)  # True if all set elements belong to other

print(set_b.issubset(set_b))
print(set_a <= set_b)

print("")

print(set_b.issuperset(set_c))
print(set_b >= set_c)

print(set_a.union(set_c))

set_d = {5, 3, 4, 11, 5000}
print(set_d)

print(set_d.intersection(set_b))  # The intersection of two sets is the set of elements which are common to all sets

print(set_b.difference(set_d))  # difference between the number of elements in two sets.

print(set_b.symmetric_difference(set_d))  # the set of elements that are in either A or B, but not in their intersection

print('Operations that directly change a set')

set_a.update(set_c)  # update() function in set adds elements from a set (passed as an argument) to the set.
print(set_a)

print('')

# The intersection_update() updates the set calling intersection_update() method with the intersection of sets.
print(set_a)
print(set_d)
set_a.intersection_update(set_d)
print(set_a)

print('')

# The difference_update() updates the set calling difference_update() method with the difference of sets.
set_d.difference_update(set_a)
print(set_d)

print('')

# The symmetric_difference_update() method finds the symmetric difference of two sets and updates the set calling it.
print(set_a)
print(set_c)
set_c.symmetric_difference_update(set_a)
print(set_c)

print('')
# adds/remove/delete an element on the set
set_c.add(33)
set_c.add('Big')
print(set_c)
set_c.remove('Big')   # If element x does not exist, it raises a KeyError.
print(set_c)
set_c.discard(33)  # If element x does not exist, it does not raise a KeyError.
print(set_c)

print('')

print(set_c)
set_c.pop()
print(set_c)

set_d.clear()  # The clear() method removes all elements from the set.
print(set_d)
