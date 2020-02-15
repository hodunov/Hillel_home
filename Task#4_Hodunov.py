print("Printing inclusive range")
start = 20
stop  = 30
step  = 2
# to get inclusive range change stop as stop+step
stop +=step #now stop is 

for i in range(start, stop, step):
    print(i, end=', ')