import sys
from collections import defaultdict
from functools import cmp_to_key

with open(sys.argv[1], "r") as f:
    data = f.read()

# Part 1 plan
# if line is in correct order
# calc middle number
# sum all middle numbers


rules, jobs = data.split("\n\n")
rules = [tuple(map(int, l.split("|"))) for l in rules.splitlines()]
jobs = [tuple(map(int, l.split(","))) for l in jobs.splitlines()]

invalid_map = defaultdict(bool)
for x, y in rules:
    invalid_map[(y, x)] = True


# Part 1 version
# def check_job(job):
#     """
#     Returns zero if job is invalid
#     Returns the value of the element at the center index of the list
#     """
#     for i in range(len(job)):
#         for j in range(i + 1, len(job)):
#             if invalid_map[(job[i], job[j])]:
#                 return 0
#     return job[len(job) // 2]


def check_job(job: list[int]) -> bool:
    """
    Returns zero if job is invalid
    Returns the value of the element at the center index of the list
    """
    for i in range(len(job)):
        for j in range(i + 1, len(job)):
            if invalid_map[(job[i], job[j])]:
                return False
    return True


def sort_job(a: int, b: int) -> int:
    if invalid_map[(a, b)]:
        return 1
    return -1


part1 = 0
part2 = 0
for job in jobs:
    if check_job(job):
        part1 += job[len(job) // 2]
    else:
        fixed_job = sorted(job, key=cmp_to_key(sort_job))
        part2 += fixed_job[len(fixed_job) // 2]

print(f"Part1: {part1}")
print(f"Part2: {part2}")


""" 
Part 2 Plan
Modify the check job function to handle invalid jobs.  Instead of returning a zero, reorder the jobs.  But, what is the most efficient way to figure out what the correct order needs to be?  Brute force?  Try all posibilities until it works?  
"""
