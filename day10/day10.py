# adventOfCode 2015 day ??
# https://adventofcode.com/2015/day/??

import time

def update_list(curr_str_list):
    new_str_list = []
    next_sequence = {
        'num_repeats': 1,
        'digit_ch': curr_str[0]
    }
    for i in range(1, len(curr_str_list)):
        if curr_str_list[i] == next_sequence['digit_ch']:
            # Add to the prior sequence
            next_sequence['num_repeats'] += 1
        else:
            new_str_list.append(next_sequence['num_repeats'])
            new_str_list.append(next_sequence['digit_ch'])
            next_sequence = {
                'num_repeats': 1,
                'digit_ch': curr_str_list[i]
            }
    new_str_list.append(next_sequence['num_repeats'])
    new_str_list.append(next_sequence['digit_ch'])
    return new_str_list

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}')
print('Note that this input file is number of repetitions, followed by the initial sequence\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        rep_num, curr_str = in_string.split(',')
        print(f'string: {curr_str} will be processed {rep_num} time(s)')
        rep_num = int(rep_num)

        start_time = time.time()
        curr_str_list = list(curr_str)
        for i in range(rep_num):
            curr_str_list = update_list(curr_str_list)
        end_time = time.time()
        if len(curr_str_list) < 60:
            print('     result: ', end='')
            for ch in curr_str_list:
                print(ch, end='')
            print()
        else:
            print(f'The resulting string has a length of {len(curr_str_list)}')
        print(f'This took {end_time - start_time} seconds to run')
print()
