# adventOfCode 2019 day 01
# https://adventofcode.com/2019/day/01


input_filename='input_sample8.txt'
print(f'\nUsing input file: {input_filename}')
with open(input_filename) as f:
    in_string = f.readline().rstrip()

# Display input contents (unless they are very large)
if len(in_string) < 70:
    print(f'containing:  {in_string}')
print(f"\nThe solution to part A is {(in_string.count('(') - in_string.count(')'))} floors")
