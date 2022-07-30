# adventOfCode 2015 day 12 part A
# https://adventofcode.com/2015/day/12

import json
import sys

def process_element(ele):
    ret_val = 0
    if isinstance(ele, (dict, list)):
        ret_val += recursive_count(ele)
    elif isinstance(ele, int):
        ret_val += ele
    elif isinstance(ele, str):
        pass  # do nothing
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
            ret_val += process_element(ele)
    return ret_val

# Reading input from the input file
input_filename='input_sample0.json'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    json_in = json.load(f)
dummy = 123

sum_partA = recursive_count(json_in)
print(f'The sum of all numbers (part A) is: {sum_partA}')


