# adventOfCode 2015 day 19
# https://adventofcode.com/2015/day/19

class All_replacements:
    def __init__(self):
        self._replacement_rules = dict()
        # self._all_found_replacements = set()

    def add(self, in_string):
        input, output = in_string.split(' => ')
        if input in self._replacement_rules:
            self._replacement_rules[input].append(output)
        else:
            self._replacement_rules[input] = [output]

    def get_substring(self, full_string, index_list):
        return full_string[index_list[0] : index_list[-1] + 1]

    def find_all(self, in_string):
        substring_indices = []
        ret_val = set()
        for i in range(len(in_string)):
            # Append an/other index to substring_indices
            substring_indices.append(i)
            # See if the whole substring (using all indices) has an associated rule
            if self.get_substring(in_string, substring_indices) not in self._replacement_rules:
                # Remove one character, at a time, from the start of it ... see if that substring has an associated rule
                sub_substring_indices = substring_indices
                while len(sub_substring_indices) > 1:
                    sub_substring_indices.pop(0)
                    if self.get_substring(in_string, sub_substring_indices) in self._replacement_rules:
                        substring_indices = sub_substring_indices
                        break
                else:
                    # break was never triggered from within while (hence, no match has been found)
                    continue
            # for replacement_string in self._replacement_rules[substring]:
            for replacement_string in self._replacement_rules[self.get_substring(in_string, substring_indices)]:
                # self._all_found_replacements.add(in_string[:substring_indices[0]] + replacement_string + in_string[substring_indices[-1]+1:])
                ret_val.add(in_string[:substring_indices[0]] + replacement_string + in_string[substring_indices[-1]+1:])
            substring_indices = []

        return ret_val

all_replacements = All_replacements()
medicine_molecule = None

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
            all_replacements.add(in_string)
        else:
            medicine_molecule = in_string

# Index: molecule, Value: number of steps to synthesize that molecule
molecules_and_step_counts = dict()
newest_molecules = [{'e'},set()]
step_number = 0
while medicine_molecule not in molecules_and_step_counts:
    for molecule in newest_molecules[step_number % 2]:
        if len(molecule) <= len(medicine_molecule):
            if molecule not in molecules_and_step_counts:
                molecules_and_step_counts[molecule] = step_number
                newest_molecules[(step_number + 1) % 2].update(all_replacements.find_all(molecule))
    newest_molecules[step_number % 2] = set()
    step_number += 1

    print(f'dict size: {len(molecules_and_step_counts)}')

print(f'The answer to part B is {molecules_and_step_counts[molecule]}\n')

