import os

file = open("input.txt", 'r')
lines = file.readlines()
file.close()

position = 50
count = 0

for line in lines:
    direction = line[0]
    distance = line[1:-1]

    if(direction == 'R'):
        position += int(distance)
    else:
        position -= int(distance)

    position = position % 100

    if(position == 0):
        count += 1

print(count)