# adventOfCode 2015 day 05
# https://adventofcode.com/2015/day/05

test_output = False

# This probably has O(NlogN), since it performs a sort
def failed_pair_repeated_twice_test(in_string):
    # Create a list of tuples with two-char substrings and indices
    # This loop traverses the input string once, so the loop should be O(N)
    list_of_2char_and_indices = []
    for i in range(1, len(in_string)):
        list_of_2char_and_indices.append((in_string[i-1:i+1], i))
    
    # The sort will probably be O(NlogN)
    list_of_2char_and_indices.sort()

    # Go through sorted list to look for duplicates with index diff > 1
    # This logic traverses the input string once, so it should be O(N)
    for i in range(1, len(list_of_2char_and_indices)):
        if list_of_2char_and_indices[i-1][0] == list_of_2char_and_indices[i][0]:
            if abs(list_of_2char_and_indices[i-1][1] - list_of_2char_and_indices[i][1]) > 1:
                # Example that matches the rule, so failed status is False
                return False
            if i < len(list_of_2char_and_indices) - 1:
                if list_of_2char_and_indices[i-1][0] == list_of_2char_and_indices[i+1][0]:
                    # Example that matches the rule, so failed status is False
                    return False
    # No examples found that match the rule, therefore it failed, so failed status is True
    return True

# This function returns False if there is at least one instance
# of a character being repeated at indices i and i+2, otherwise True is returned.
# The function traverses the input string once, so it should be O(N)
def failed_letter_repeated_two_indices_later_test(in_string):
    for i in range(2, len(in_string)):
        if in_string[i-2] == in_string[i]:
            return False
    return True

nice_string_count = 0
# Reading input from the input file
input_filename='input_sample1.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        if test_output:
            print(f'\n{in_string}')
        if failed_pair_repeated_twice_test(in_string):
            if test_output:
                print('Failed repeated twice test')
            continue
        if failed_letter_repeated_two_indices_later_test(in_string):
            if test_output:
                print('Failed letter repeated two indices later test')
            continue

        if test_output:
            print('Passed all tests')
        nice_string_count += 1

if test_output:
    print()
print(f'The solution to part B is {nice_string_count}\n')

