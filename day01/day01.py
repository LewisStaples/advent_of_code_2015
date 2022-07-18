# adventOfCode 2019 day 01
# https://adventofcode.com/2019/day/01


input_filename='input.txt'
print(f'\nUsing input file: {input_filename}')
with open(input_filename) as f:
    in_string = f.readline().rstrip()

# Display input contents (unless they are very large)
if len(in_string) < 70:
    print(f'containing:  {in_string}')

print(f"\nThe solution to part A is {(in_string.count('(') - in_string.count(')'))} floors")

# Part B
current_floor = 0
for i, ch in enumerate(in_string):
    current_floor += 1 if ch == '(' else -1
    if current_floor == -1:
        print(f'\nThe solution to part B is {(i+1)}  (the position where Santa first enters the basement)')
        break
