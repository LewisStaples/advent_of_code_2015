# adventOfCode 2015 day 19
# https://adventofcode.com/2015/day/19

import itertools

class Replacements:
    def __init__(self):
        self._replacement_rules = dict()

    def add(self, in_string):
        input, output = in_string.split(' => ')
        self._replacement_rules[output] = input

    def get_substring(self, full_string, index_list):
        return full_string[index_list[0] : index_list[-1] + 1]

    def find_all(self, in_string):
        ret_val = set()
        for substring_indices in itertools.combinations_with_replacement(range(len(in_string)), 2):
            the_substring = self.get_substring(in_string, substring_indices)
            # if substring has an associated rule
            if the_substring in self._replacement_rules:
                for replacement_string in self._replacement_rules[the_substring]:
                    ret_val.add(
                        in_string[:substring_indices[0]] +
                        replacement_string + 
                        in_string[substring_indices[-1] + 1:]
                    )
        return ret_val

the_replacements = Replacements()

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
            the_replacements.add(in_string)
        else:
            medicine_molecule = in_string

step_number = 0
molecule_in_x_steps = {}
newest_molecules = [{medicine_molecule},set()]
while 'e' not in molecule_in_x_steps:
    for molecule in newest_molecules[step_number % 2]:
        if molecule not in molecule_in_x_steps:
            molecule_in_x_steps[molecule] = step_number
            newest_molecules[(step_number + 1) % 2].update(the_replacements.find_all(molecule))
    newest_molecules[step_number % 2] = set()
    step_number += 1

print('The number of steps to create the medicine_molecule (answer to part B) is: ', end ='')
print(molecule_in_x_steps['e'])
print()

