# Part 1
# use regex to look for mul(x,x) pattern and pull those out into a list
# for each element, check if both args are valid numbers
# if they are, multiply them and accumulate the result

# Part 2
# Scan text for do() and don't()
# xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
# if do(): enable() or start accumulating
# if dont(): disable() or stop accumulating


import re
import sys
from math import prod

with open(sys.argv[1], "r") as f:
    data = f.read()

# pairs = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
# part1 = sum([prod(map(int, val)) for val in pairs])

part1 = 0
part2 = 0
enabled = True
for inst in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data):
    match inst:
        case "do()":
            enabled = True
        case "don't()":
            enabled = False
        case _:
            x, y = map(int, inst[4:-1].split(","))
            part1 += x * y
            if enabled:
                part2 += x * y

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
