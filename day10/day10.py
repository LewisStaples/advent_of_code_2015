# adventOfCode 2015 day ??
# https://adventofcode.com/2015/day/??

def update_string(curr_str):
    new_str = ''
    next_sequence = {
        'num_repeats': 1,
        'digit_ch': curr_str[0]
    }
    for i in range(1, len(curr_str)):
        if curr_str[i] == next_sequence['digit_ch']:
            # Add to the prior sequence
            next_sequence['num_repeats'] += 1
        else:
            new_str += str(next_sequence['num_repeats']) + next_sequence['digit_ch']
            next_sequence = {
                'num_repeats': 1,
                'digit_ch': curr_str[i]
            }
    new_str += str(next_sequence['num_repeats']) + next_sequence['digit_ch']
    return new_str

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}')
print('Note that this input file is number of repetitions, followed by the initial sequence\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        # print(in_string)
        rep_num, curr_str = in_string.split(',')
        print(f'string: {curr_str} will be processed {rep_num} time(s)')
        rep_num = int(rep_num)

        for i in range(rep_num):
            curr_str = update_string(curr_str)
        if len(curr_str) < 60:
            print(f'     result: {curr_str}')
        else:
            print(f'The resulting string has a length of {len(curr_str)}')
print()
