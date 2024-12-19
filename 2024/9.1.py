files = [int(n) for n in open("2024/9.txt", "r").readline()]

storagespace = ["."] * sum(files)

index = 0
ID = 0

for j in range(len(files)):
    if j % 2 == 0:
        filesize = files[j]
        for block in range(filesize):
            storagespace[index] = ID
            index += 1
        ID += 1 

    if j % 2 == 1: 
        space = files[j]
        for block in range(space):
            index += 1

# =========================================================
freespace_index = 0
for i in reversed(range(len(storagespace))):
    block = storagespace[i]
    if block == ".": continue

    # find freespace index
    while True:
        if storagespace[freespace_index] == ".": break
        freespace_index += 1
    
    if freespace_index > i: break

    storagespace[freespace_index] = block
    storagespace[i] = "."

# =========================================================

result = 0
for position in range(len(storagespace)):
    ID = storagespace[position]
    if ID == ".": continue
    result += position * ID

print(result)