# adventOfCode 2015 day ??
# https://adventofcode.com/2015/day/??


# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_text = in_string.rstrip().split(' ')
        in_text = [x.replace(':','') for x in in_text] # remove colons
        print(in_text)

        # Convert in_text elements 2 through end into a dict
        # See if any items in input dict conflict with given "ticker tape"
        # If there's no conflict the answer is the string of digits in element # 1
