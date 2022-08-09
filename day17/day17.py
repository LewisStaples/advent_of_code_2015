# adventOfCode 2015 day 17
# https://adventofcode.com/2015/day/17

import itertools

container_list = list()
total_combinations = 0 # part A answer
container_dict = dict() # part B answer

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        container_list.append(int(in_string))

for r in range(1, len(container_list)):
    for combo in itertools.combinations(container_list, r):
        if sum(combo) == 25:
            total_combinations += 1 
            if len(combo) in container_dict:
                container_dict[len(combo)] += 1
            else:
                container_dict[len(combo)] = 1

print(f'The total combinations (part A answer) is: {total_combinations}')
print(f'The count of choices for the minimum number of containers (part B answer) is: {container_dict[min(container_dict.keys())]}\n')

