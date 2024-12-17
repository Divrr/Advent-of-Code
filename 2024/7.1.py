file = open("2024/7.txt", "r")

testvals = []
numberlists = []

for line in file.readlines():
    testvalraw, numberlistraw = line.split(": ")

    testvals.append(int(testvalraw))
    numberlists.append([int(n) for n in numberlistraw.split(" ")])

file.close()

# =========================================================
from itertools import product

result = 0

for index, testval in enumerate(testvals):
    numberlist = numberlists[index]
    combos = list(product(*[("*", "+")]*len(numberlist)))

    for combo in combos:
        answer = numberlist[0]
        for position in range(len(numberlist)-1):
            if combo[position] == "*":
                answer *= numberlist[position+1]
            elif combo[position] == "+":
                answer += numberlist[position+1]
        
        if answer == testval:
            result += testval
            break

print(result)
