# adventOfCode 2019 day 02
# https://adventofcode.com/2019/day/02

from itertools import combinations
import math

area_needed_partA = 0

# Reading input from the input file into memory
# presents_dimensions = []
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        dimensions = [int(x) for x in in_string.split('x')]
        areas = []
        for side_dimensions in combinations(dimensions, 2):
            areas.append(math.prod(side_dimensions))
        areas.sort()
        area_needed_partA += areas[0] + sum(areas) * 2

print(f'The answer to part A is {area_needed_partA}\n')


