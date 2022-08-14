class Replacements:
    def __init__(self):
        self._replacement_rules = dict()

    def add(self, in_string):
        input, output = in_string.split(' => ')
        self._replacement_rules[output] = input

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
                ret_val.add(in_string[:substring_indices[0]] + replacement_string + in_string[substring_indices[-1]+1:])
            substring_indices = []

        # self._known_replacements[in_string] = ret_val
        return ret_val

the_replacements = Replacements()

# Reading input from the input file
input_filename='input_sample2.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        if len(in_string) == 0:
            continue
        elif ' => ' in in_string:
            the_replacements.add(in_string)
            print(in_string)

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
        dummy = 123
    newest_molecules[step_number % 2] = set()
    step_number += 1

    dummy = 123
