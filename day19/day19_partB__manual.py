# adventOfCode 2015 day 19
# https://adventofcode.com/2015/day/19

# This is a manual solution that only works on the full input file.
#
# The below code handles treating two letter atoms 
# as a single atom using capitalization, which is done by traversing 
# the full string in reverse and if a letter is lowercase then pairing
# it with the next letter.  (This is done since all elements are either
# a single capital letter, or a capital followed by a lowercase letter)

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        if len(in_string) == 0:
            continue
        elif ' => ' in in_string:
            continue
        else:
            medicine_molecule = in_string


this_atom = []
i = len(medicine_molecule) - 1
num_Y = 0
num_Rn_Ar = 0
num_all = 0
while i >= 0:
    this_atom.append(medicine_molecule[i])
    # See if this atom has two letters
    if this_atom[0].islower():
        i -= 1
        this_atom.insert(0,medicine_molecule[i])
    num_all += 1
    if this_atom[0] == 'Y':
        num_Y += 1
    elif this_atom[0] == 'R':
        num_Rn_Ar += 1
    elif this_atom[0] == 'A' and this_atom[1] == 'r':   # Checking second char is needed to distinguish Ar vs. Al
        num_Rn_Ar += 1
    i -= 1
    this_atom = []
print(f'The solution to part B is {num_all - num_Rn_Ar - 2 * num_Y - 1}')

