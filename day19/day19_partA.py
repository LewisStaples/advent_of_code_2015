# adventOfCode 2015 day 19
# https://adventofcode.com/2015/day/19

class All_replacements:
    def __init__(self):
        self._replacement_rules = dict()
        self._all_possible_replacements = set()

    def add(self, in_string):
        input, output = in_string.split(' => ')
        if input in self._replacement_rules:
            self._replacement_rules[input].append(output)
        else:
            self._replacement_rules[input] = [output]

    def find_all(self, in_string):
        substring_indices = []
        for i in range(len(in_string)):
            substring_indices.append(i)
            substring = in_string[substring_indices[0]:substring_indices[-1]+1]
            if substring not in self._replacement_rules:
                sub_substring_indices = substring_indices
                while len(sub_substring_indices) > 1:
                    sub_substring_indices.pop(0)
                    sub_substring = in_string[sub_substring_indices[0]:sub_substring_indices[-1]+1]
                    if sub_substring in self._replacement_rules:
                        substring = sub_substring
                        break
                if substring not in self._replacement_rules:
                    continue
            for replacement_string in self._replacement_rules[substring]:
                self._all_possible_replacements.add(in_string[:substring_indices[0]] + replacement_string + in_string[substring_indices[-1]+1:])
                dummy = 123
            substring_indices = []

all_replacements = All_replacements()
medicine_molecule = None

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
            all_replacements.add(in_string)
        else:
            all_replacements.find_all(in_string)

print('The number of distinct molecules (answer to part A) is: ', end ='')
print(len(all_replacements._all_possible_replacements))
