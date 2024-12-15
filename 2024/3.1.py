import re

with open("2024/3.txt", "r") as corrupted_instructions:
    instructions = re.findall(r"mul\(\d+,\d+\)", corrupted_instructions.read())

result = sum(int(a) * int(b) for a, b in (re.findall(r"\d+", instruction) for instruction in instructions))

print(result)