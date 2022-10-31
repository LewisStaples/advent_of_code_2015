# adventOfCode 2015 day 24
# https://adventofcode.com/2015/day/24


import itertools


# Determine if what's left over after group1 is defined
# can be split into equal-summed groups 2, 3, and 4,
def g1valid(g1combo, pkg_wts, sum_four):
    g234combo = pkg_wts.difference(set(g1combo))
    
    # Consider all valid group two's
    for i in range(1, len(g234combo)//3 + 1):
        g2combo_iter = itertools.combinations(g234combo, i)
        for g2combo in g2combo_iter:
            if sum(g2combo) == sum_four:
                g34combo = g234combo.difference(g2combo)

                # Consider all valid group three's
                for j in range(1, len(g34combo)//2 + 1):
                    g3combo_iter = itertools.combinations(g34combo, j)
                    for g3combo in g3combo_iter:
                        if sum(g3combo) == sum_four:
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
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        pkg_wts.add(int(in_string))

len_pkg = len(pkg_wts)

if sum(pkg_wts) % 4 != 0:
    raise ValueError("The given list's sum divided by four isn't an integer!")

sum_four = int(sum(pkg_wts) / 4)

for len_g1 in range(1, len_pkg):
    # Consider all combinations of this length
    all_combos_of_this_length = itertools.combinations(pkg_wts, len_g1)
    for g1combo in all_combos_of_this_length:
        # Disregard any combination choices for group1 which don't sum up to sum_four
        if sum(g1combo) != sum_four:
            continue
        # Perform other checks to see if this group1 choice is valid
        # (Can the remainder be split into equal-summed groups 2 and 3?)
        if g1valid(g1combo, pkg_wts, sum_four):
            smallest_qu_ent = min(smallest_qu_ent, quantum_entanglement(g1combo))
    if smallest_qu_ent < float('inf'):
        break

print(f'The smallest quantum entanglement associated with the smallest possible packages \
in the passenger compartment (group1) are {smallest_qu_ent}\n')


