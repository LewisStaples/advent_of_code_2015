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

    def get_substring(self, full_string, index_list):
        return full_string[index_list[0] : index_list[-1] + 1]

    def find_all(self, in_string):
        substring_indices = []
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
                self._all_possible_replacements.add(in_string[:substring_indices[0]] + replacement_string + in_string[substring_indices[-1]+1:])
            substring_indices = []

all_replacements = All_replacements()

# Reading input from the input file
input_filename='input_sample1.txt'
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
