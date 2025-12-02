import os

def get_factors(num) -> list:
    factors = []
    for i in range(1, num):
        if (num % i == 0):
            factors.append(i)
    return factors

def is_recurring(id):
    id_str = str(id)

    factors = get_factors(len(id_str))

    for factor in factors:
        comparisons = 0
        repeating = False
        shift = int(len(id_str))/factor

        if(factor > 1):
            repeating = True

        while(comparisons < factor-1 and repeating):
            if (id_str[int(comparisons*shift): int((comparisons + 1)*shift)] != id_str[int((comparisons + 1)*shift): int((comparisons + 2)*shift)]):
                repeating = False
            comparisons += 1
        if(repeating):
            return True
    return False


file = open("input.txt", 'r')
data = file.readline()
file.close()

# parse data
id = ""
start_ids = []
end_ids = []

for i in range(len(data)):
    if (data[i] == "-"):
        start_ids.append(int(id))
        id = ""
    elif (data[i] == ","):
        end_ids.append(int(id))
        id = ""
    else:
        id = id + data[i]
end_ids.append(int(id))

cnt = 0

for i in range(len(start_ids)):
    current_id = start_ids[i]

    while (current_id <= end_ids[i]):
        if (is_recurring(current_id)):
            cnt += current_id
        current_id += 1

print(cnt)