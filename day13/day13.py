# adventOfCode 2015 day 13
# https://adventofcode.com/2015/day/13

attendee_happiness_impact = dict()
attendees = set()

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

