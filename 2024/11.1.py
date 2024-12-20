from tqdm import tqdm

array = [int(n) for n in open("2024/11.txt", "r").read().split()]

def blink(array):
    newarray = []
    for stone in array:
        if stone == 0:
            newarray.append(1)
        elif len(str(stone))%2 == 0:
            index = len(str(stone))//2
            leftstone = int(str(stone)[:index])
            rightstone = int(str(stone)[index:])

            newarray.append(leftstone)
            newarray.append(rightstone)
        else:
            newarray.append(stone * 2024)
    
    return newarray

result = array
for i in tqdm(range(25)):
    result = blink(result)

print(len(result))