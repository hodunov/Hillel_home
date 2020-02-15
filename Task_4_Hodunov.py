print("Printing inclusive range")
start = int(input('Enter start number  '))
stop = int(input('Enter stop number  '))
step = int(input('Enter step number  '))

for i in range(start, stop + 1):
    if i % step == 0 and i > 0:
        print(i, end=', ')

print('')
# Or if we include zero

for i in range(start, stop + 1):
    if i % step == 0:
        print(i, end=', ')