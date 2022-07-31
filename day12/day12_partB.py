# adventOfCode 2015 day 12 part B
# https://adventofcode.com/2015/day/12

import json
import sys

# "red" encountered in a dict (object),
# making that object 0
class RedException(Exception):
    pass

def process_element(ele):
    ret_val = 0
    if isinstance(ele, (dict, list)):
        ret_val += recursive_count(ele)
    elif isinstance(ele, int):
        ret_val += ele
    elif isinstance(ele, str):
        if ele == "red":
            raise RedException()
    else:
        print(f'Unexpected type encountered: {type(ele)}')
        sys.exit('Exiting now ....')
    return ret_val

def recursive_count(data_struc):
    ret_val = 0
    # traverse the data_structure
    for ele in data_struc:
        ret_val += process_element(ele)
    if isinstance(data_struc, dict):
        for ele in data_struc.values():
            try:
                ret_val += process_element(ele)
            except RedException:
                return 0
    return ret_val

# Reading input from the input file
input_filename='input_sample2.json'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    json_in = json.load(f)
dummy = 123

sum_partB = recursive_count(json_in)
print(f'The sum of all numbers not in an object where "red" appears (part B) is: {sum_partB}')


