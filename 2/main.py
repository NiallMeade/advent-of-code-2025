import os

def is_recurring(id):
    if ((len(str(id)) % 2) != 0):
        return False
    
    id_str = str(id)
    if (id_str[0: int(len(id_str)/2)] == id_str[int(len(id_str)/2): int(len(id_str))]):
        return True

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