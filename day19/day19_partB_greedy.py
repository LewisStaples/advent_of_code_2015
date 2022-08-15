# adventOfCode 2015 day 19
# https://adventofcode.com/2015/day/19

import random

class Replacements:
    def __init__(self):
        self._replacement_rules = dict()

    def add(self, in_string):
        input, output = in_string.split(' => ')
        self._replacement_rules[output] = input

    def find_longest_substitution(self, in_string):
        available_substitutes = ['']
        for rule_output in self._replacement_rules:
            if rule_output in in_string:
                # Only retain the substitutes that are the longest (greedy alg.)
                if len(rule_output) > len(available_substitutes[0]):
                    available_substitutes = [rule_output]
                # If two or more are tied for the longest, keep all longest
                elif len(rule_output) == len(available_substitutes[0]):
                    available_substitutes.append(rule_output)

        # This seems to never happen in this problem (but it could happen)
        if available_substitutes == ['']:
            return None
        
        # Randomly any one of the longest (kept list of) substitutes
        string_to_swap_out = available_substitutes[random.randrange(len(available_substitutes))]
        string_to_substitute = self._replacement_rules[string_to_swap_out]
        # Do only one substitution at a time, so each one gets counted with step_number
        return in_string.replace(string_to_swap_out, string_to_substitute, 1)

the_replacements = Replacements()

# Reading input from the input file
input_filename='input_sample3.txt'
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


best_result = float('inf')
answer_count = 0
# Trying the greedy algorithm multiple times, because the given problem
# asks to find the fewest number of steps (which implies that there's one than
# one correct solution)
while answer_count < 100:  # outer loop
    step_number = 0
    newest_molecule = medicine_molecule
    while True:  # inner loop
        step_number += 1
        newest_molecule = the_replacements.find_longest_substitution(newest_molecule)
        if newest_molecule == 'e':
            best_result = min(best_result, step_number) # retain the lowest step_number
            answer_count += 1
            break # exit inner loop, thus restarting outer loop

        # dead end
        if newest_molecule is None:
            break # exit inner loop, thus restarting outer loop

print(f'The number of steps to create the medicine_molecule (answer to part B) is: {best_result}\n')
