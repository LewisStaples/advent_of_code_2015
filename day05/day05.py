# adventOfCode 2015 day ??
# https://adventofcode.com/2015/day/??


def failed_three_vowels_test(in_string):
    all_vowels = 'aeiouAEIOU'
    number_vowels_found = 0
    for ch in in_string:
        if ch in all_vowels:
            if number_vowels_found > 1:
                # Stop counting vowels once the third vowel is found
                # (Any letters after the third vowel will be skipped to save time)
                return False # it passed
            number_vowels_found += 1
    return True # it failed

def failed_repeat_letter_test(in_string):
    for i in range(1,len(in_string)):
        # Stop looking for matches once a single match is found
        if in_string[i-1] == in_string[i]:
            return False # it passed the test
    return True # it failed

def failed_forbidden_substring_test(in_string):
    for for_ss in ['ab', 'cd', 'pq', 'xy']:
        if for_ss in in_string:
            return True # it failed
    return False # it passed the test

nice_string_count = 0
# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(f'\n{in_string}')
        if failed_three_vowels_test(in_string):
            print('Failed three vowel test')
            continue
        if failed_repeat_letter_test(in_string):
            print('Failed repeat letter test')
            continue
        if failed_forbidden_substring_test(in_string):
            print('Failed forbidden substring test')
            continue
        print('Passed all tests')
        nice_string_count += 1

print(f'The solution to part A is {nice_string_count}')
