import sys

with open(sys.argv[1], "r") as f:
    lines = [list(map(int, line.split())) for line in f.readlines()]

"""_summary_

int is the function map() is passing in so map over the array and convert each element to an int then convert the array into a list because map returns a generator

Here's what AI says about the map function:

The map() function in Python returns a map object, which is an iterator that yields transformed items on demand.
This iterator is created by applying a specified function to each element of one or more iterables.
Since the map object is lazy, it does not compute or store all results in memory at once; instead, it computes each result only when iterated over.
To access the results directly, the map object must be converted to a list, tuple, or another sequence type using their respective factory functions.

"""

# One way of doing it
# list1 = []
# list2 = []
# for line in lines:
#     list1.append(line[0])
#     list2.append(line[1])

list1, list2 = list(map(list, zip(*lines)))

a1 = sum(abs(x1 - x2) for x1, x2 in zip(sorted(list1), sorted(list2)))

a2 = sum(x * len([y for y in list2 if y == x]) for x in list1)


part1 = a1
print(f"Part 1: {part1}")
part2 = a2
print(f"Part 2: {part2}")
