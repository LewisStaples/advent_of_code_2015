# adventOfCode 2015 day 07
# https://adventofcode.com/2015/day/07


import re
import sys
import operator

# Some dictionaries are used in this program:

# This dictionary shows the known value for each wire whose value is now known
wires_known = dict()

# This dictionary has all wires with not yet determined values
# and it lists their value in terms of other wires
wires_unknown = dict()

binary_bitwise_operator_dict = {
    'AND': operator.__and__,
    'OR': operator.__or__,
    'LSHIFT': operator.__lshift__,
    'RSHIFT': operator.__rshift__
    }

def resolve_wire(string_value):
    string_list = string_value.split(' ')
    string_list = [int(x) if x.isdigit() else x for x in string_list ]
    if len(string_list) == 2:
        # The operator must be NOT
        if string_list[-2] != 'NOT':
            print(f'ERROR: "{string_list}" is wrong ... it could have two items only if the operator is NOT')
            sys.exit()
        string_list = [~string_list[-1]]
    elif len(string_list) == 3:
        string_list = [binary_bitwise_operator_dict[string_list[1]](string_list[0],string_list[2])]
    string_list[0] = string_list[0] % 65536
    return string_list[0]

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(f'INPUT:  {in_string}')

        # Fill in information in the three dictionaries
        lhs_str, rhs_str = in_string.split(' -> ')
        if re.search('[a-z]', lhs_str) is None:
            wires_known[rhs_str] = resolve_wire(lhs_str)
        else:
            wires_unknown[rhs_str] = lhs_str
            
wires_known['b'] = 3176
            
del input_filename, lhs_str, rhs_str, f

while len(wires_unknown) > 0:
    # Replace any known variables with their (known) values
    for k,v in wires_unknown.items():
        factor_list =  re.findall('[a-z]+', v)
        for factor in factor_list:
            if factor in wires_known:
                # substitute the value 
                # (doing this in a for loop is OK as long as keys() remains unchanged)
                wires_unknown[k] = wires_unknown[k].replace(factor, str(wires_known[factor]))

    # For any items without any variables, mark them as resolved
    for k,v in wires_unknown.items():
        if re.search('[a-z]', v) is None:
            wires_known[k] = resolve_wire(v)
            wires_unknown[k] = None
    
    filtered = {k: v for k, v in wires_unknown.items() if v is not None}
    wires_unknown.clear()
    wires_unknown.update(filtered)

print(f'The answer to part A is {wires_known["a"]}')

