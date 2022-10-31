# adventOfCode 2015 day 24
# https://adventofcode.com/2015/day/24


import itertools


# Determine if group1 can be split into groups two and three,
# where group three's sum is the targetted sum_third
#
# Since it is assumed that it was previously shown that group one sums to sum_third,
# This means that groups 1, 2, and 3 are all equal, thus the group 1 choice is valid.
def g1valid(g1combo, pkg_wts, sum_third):
    g2and3combo = pkg_wts.difference(set(g1combo))

    for i in range(1, len(g2and3combo)//2 + 1):
        g3combo_iter = itertools.combinations(g2and3combo, i)
        for g3combo in g3combo_iter:
            if sum(g3combo) == sum_third:
                return True
    return False

# Calculate quantum entanglement for this combination
def quantum_entanglement(combination):
    ret_val = 1
    for el in combination:
        ret_val *= el
    return ret_val

pkg_wts = set()
smallest_qu_ent = float('inf')

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        pkg_wts.add(int(in_string))

len_pkg = len(pkg_wts)

if sum(pkg_wts) % 3 != 0:
    raise ValueError("The given list's sum divided by three isn't an integer!")

sum_third = int(sum(pkg_wts) / 3)

for len_g1 in range(1, len_pkg):
    # Consider all combinations of this length
    all_combos_of_this_length = itertools.combinations(pkg_wts, len_g1)
    for g1combo in all_combos_of_this_length:
        # Disregard any combination choices for group1 which don't sum up to sum_third
        if sum(g1combo) != sum_third:
            continue
        # Perform other checks to see if this group1 choice is valid
        # (Can the remainder be split into equal-sized groups 2 and 3?)
        if g1valid(g1combo, pkg_wts, sum_third):
            smallest_qu_ent = min(smallest_qu_ent, quantum_entanglement(g1combo))
    if smallest_qu_ent < float('inf'):
        break

print(f'The smallest quantum entanglement associated with the smallest possible packages \
in the passenger compartment (group1) are {smallest_qu_ent}\n')


