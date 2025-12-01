import os
from math import ceil

file = open("input.txt", 'r')
lines = file.readlines()
file.close()

position = 50
count = 0

for line in lines:
    direction = line[0]
    distance = int(line[1:-1])
    print(distance)

    elements = ceil(distance/100)

    for i in range(elements - 1):
        count += 1
    
    if(distance % 100 == 0):
        cnt += 1
    elif(direction == 'R'):
        position += distance % 100
    else:
        position -= distance % 100

    # Checks if a zero pass has occured and that the previous postion was not 0
    if((position > 99 or position < 1) and (abs(position) != distance % 100)):
        print("Incrementing... ", position)
        count += 1
    
    position = position % 100
    print(position)
    print("-----")

print(count)