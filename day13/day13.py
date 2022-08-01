# adventOfCode 2015 day 13
# https://adventofcode.com/2015/day/13

from itertools import permutations

attendee_happiness_impact = dict()
attendees = set()

def calc_happiness_change(permutation, attendee_happiness_impact):
    ret_val = 0
    for index_attendee1 in range(len(permutation)):
        index_attendee2 = (index_attendee1 + 1) % len(permutation)
        ret_val += attendee_happiness_impact[(permutation[index_attendee1], permutation[index_attendee2])]
        ret_val += attendee_happiness_impact[(permutation[index_attendee2], permutation[index_attendee1])]
    return ret_val

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        words = in_string.rstrip().split()
        attendee_happiness_impact[(words[0], words[-1][:-1])] = int(words[3])
        if words[2] == 'lose':
            attendee_happiness_impact[(words[0], words[-1][:-1])] *= -1
        attendees.add(words[0])

happiness_change_ans_A = float('-inf')
for permutation in permutations(attendees):
    this_happiness_change = calc_happiness_change(permutation, attendee_happiness_impact)
    happiness_change_ans_A = max(happiness_change_ans_A, this_happiness_change)
print(f'The total change in happiness excluding myself (part A) is {happiness_change_ans_A}\n')

# Define a string for myself
self_string = 'myself'
# Ensure that self_string doesn't clash with any strings in attendees
while self_string in attendees:
    self_string += '_'

attendees.add(self_string)
for attendee in attendees:
    attendee_happiness_impact[(self_string, attendee)] = 0
    attendee_happiness_impact[(attendee, self_string)] = 0

happiness_change_ans_B = float('-inf')
for permutation in permutations(attendees):
    this_happiness_change = calc_happiness_change(permutation, attendee_happiness_impact)
    happiness_change_ans_B = max(happiness_change_ans_B, this_happiness_change)
print(f'The total change in happiness including myself (part B) is {happiness_change_ans_B}\n')
