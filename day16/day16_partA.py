# adventOfCode 2015 day 16
# https://adventofcode.com/2015/day/16


import sys



# Perform string manipulations
def manipulate_string(in_string):
    ret_list = in_string.rstrip().split(' ') # 
    ret_list = [x.replace(':','') for x in ret_list] # remove colons
    ret_list = [x.replace(',','') for x in ret_list] # remove commas
    return ret_list

# Convert in_text elements 2 through end into a dict
# (and convert the counts from a string of digits to integers)
def convert_to_dict(in_text):
        keys = [v for k,v in enumerate(in_text) if k > 1 and k % 2 == 0]
        vals = [int(v) for k,v in enumerate(in_text) if k > 1 and k % 2 == 1]
        in_text_dict = dict(zip(keys, vals))
        return in_text_dict

# Is this input line for the correct Aunt Sue?
def correct_aunt_sue_found(in_text_dict, known_characteristics):
        # See if any items in input dict conflict with given "ticker tape"
        # If there's no conflict the answer is the string of digits in element # 1
        for k,v in known_characteristics.items():
            if k in in_text_dict:
                if v != in_text_dict[k]:
                    return False
        return True

# Known characteristics of the Aunt Sue that we're looking for
known_characteristics = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_text_list = manipulate_string(in_string)
        in_text_dict = convert_to_dict(in_text_list)
        
        if correct_aunt_sue_found(in_text_dict, known_characteristics):
            print(f"The aunt Sue that you're looking for is {in_text_list[1]}\n")
            break

