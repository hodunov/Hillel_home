# Task 3-1 List Operations
first_list = [1, 2, 'Hillel', True, 3.14, [4, 3, 2, 1]]
print('first list =', first_list)

first_list.append('End')
print('first_list.append =', first_list)

first_list.insert(2, 'IT')
print('first_list.insert =', first_list)

first_list.remove('End')
print('first_list.remove = ', first_list)

first_list.clear()
print('first_list.clear =', first_list)

print('')

second_list = [3, 4, False, 'AI', [12, 11, 10, 9], 3.14, 3]
print('second_list =', second_list)

print('second_list.index =', second_list.index(4))

second_list.pop(4)
print('second_list.pop(4) = ', second_list)

print('second_list.count(3) = ', second_list.count(3))

print('')

third_list = [10, 3.14, 111, 2212, 20]
print('third_list = ', third_list)

third_list.sort()
print('third_list.sort = ', third_list)

third_list.reverse()
print('third_list.reverse = ', third_list)

print("len(second_list) = ", len(second_list))

print('sorted(third_list = ', sorted(third_list))

print('min(third_list) = ', min(third_list))

print('max(third_list) = ', max(third_list))
