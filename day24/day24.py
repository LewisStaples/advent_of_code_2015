# adventOfCode 2015 day 24
# https://adventofcode.com/2015/day/24


import itertools
import copy
pkg_wts = set()
smallest_qu_ent = float('inf')

def quantum_entanglement(combination):
    ret_val = 1
    for el in combination:
        ret_val *= el
    return ret_val

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # print(in_string)
        pkg_wts.add(int(in_string))

len_pkg = len(pkg_wts)

if sum(pkg_wts) % 3 != 0:
    raise ValueError("The given list's sum divided by three isn't an integer!")

sum_third = int(sum(pkg_wts) / 3)

for len_pass_comp in range(1, len_pkg):
    all_combos_of_this_length = itertools.combinations(pkg_wts, len_pass_comp)
    # print(len_pass_comp)
    # Consider all combinations of this length
    for combo in all_combos_of_this_length:
        # Disregard any combinations which don't sum up to sum_third
        if sum(combo) != sum_third:
            continue
        remainder = pkg_wts.difference(set(combo))

        for i in range(1, len(remainder)):
            remainder1_iter = itertools.combinations(remainder, i)
            for remainder1 in remainder1_iter:
                if sum(remainder1) == sum_third:
                    # pass
                #     # calculate quantum_entanglement and keep the smallest,
                #     # because now it's known that combo == remainder1 == sum_third 
                #     # (incidentally this is also equal to combo.difference(remainder1))
                    smallest_qu_ent = min(smallest_qu_ent, quantum_entanglement(combo))

    if smallest_qu_ent < float('inf'):
        break

print(f'The smallest quantum entanglement associated with the smallest possible packages \
in the passenger compartment are {smallest_qu_ent}\n')


