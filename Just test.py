def countDivisibles(A, B, M):
    # Variable to store the counter
    counter = 0;

    # Running a loop from A to B 
    # and check if a number is  
    # divisible by M. 
    for i in range(A, B):
        if (i % M == 0):
            counter = counter + 1

    return counter


# Driver code
# A and B define the range, 
# M is the dividend 
A = int(input('Enter start number  '))
B = int(input('Enter stop number  '))
M = int(input('Enter step number  '))

# Printing the result 
print(countDivisibles(A, B, M)) 