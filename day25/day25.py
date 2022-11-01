# adventOfCode 2015 day 25
# https://adventofcode.com/2015/day/25


# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        row_number, column_number = [int(x) for x in in_string[80:-1].split(', column ')]

        # From row, col#, determine number of times the code needs to be processed
        sum_coords = row_number + column_number
        # Using this https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
        times_to_run = column_number + (sum_coords - 2) * (sum_coords - 1) // 2 - 1

        the_code = 20151125
        # Then use number of times in a for loop to calculate the value
        for i in range(times_to_run):
            the_code *= 252533
            the_code %= 33554393

        print(f'The answer when using row number {row_number} and column number {column_number} is {the_code}')
print()

