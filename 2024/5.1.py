file = open("2024/5.txt", "r")
rulesraw, updatesraw = file.read().split("\n\n")
file.close()

# SETUP
# isbefore[i] = [a, b, c] i.e. i is before a, b, and c
# isafter[i] = [d, e, f] i.e. i is after d, e, and f
isbefore = {}
isafter = {}

for line in rulesraw.split("\n"):
    before, after = [int(n) for n in line.split("|")]
    isbefore[before] = isbefore.get(before, []) + [after]
    isafter[after] = isafter.get(after, []) + [before]

updates = []
for line in updatesraw.split("\n"):
    updates.append([int(n.strip()) for n in line.split(",")])

# =========================================================
result = 0

# CHECKING
for update in updates:
    valid = True
    for index, pageno in enumerate(update):
        # there is a rule for every element before
        for before in update[:index]:
            if pageno not in isbefore[before]:
                valid = False
        
        # there is a rule for every element after
        for after in update[index+1:]:
            if pageno not in isafter[after]:
                valid = False

    if valid:
        median = update[len(update)//2]
        result += median
    
print(result)