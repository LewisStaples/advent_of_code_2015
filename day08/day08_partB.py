# adventOfCode 2015 day 08
# https://adventofcode.com/2015/day/08


def encode(in_string):
    out_string = in_string.replace('\\','\\\\')
    out_string = out_string.replace('\"', '\\\"')
    out_string = '"' + out_string + '"'
    return out_string

sum_part_B = 0
# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        encoded_string = encode(in_string)
        sum_part_B += len(encoded_string) - len(in_string)
print(f'The answer to part B is {sum_part_B}\n')
