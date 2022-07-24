# adventOfCode 2015 day 08
# https://adventofcode.com/2015/day/08


def count_memory_chars(the_string):
    ret_val = 0
    index = 0
    while True:
        try:
            index += 1
            if the_string[index] == '"':
                break
            ret_val += 1
            if the_string[index] == '\\':
                index += 1
                if the_string[index] == 'x':
                    index += 2
        except IndexError:
            break
    return ret_val

sum_part_A = 0
# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        sum_part_A += len(in_string) - count_memory_chars(in_string)
print(f'The answer to part A is {sum_part_A}\n')
