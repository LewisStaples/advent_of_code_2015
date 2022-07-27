# adventOfCode 2015 day 11
# https://adventofcode.com/2015/day/11

def increment_password(santas_password):
    str_len = len(santas_password)
    for i in range(str_len - 1, -1, -1):
        print(f'index: {i}, char: {santas_password[i]}')
        if santas_password[i] == 'z':
            santas_password[i] = 'a'
            continue
        santas_password[i] = chr(ord(santas_password[i]) + 1)
        break
    return santas_password

# Reading input from the input file
input_filename='input_scenario0.txt'
print(f'\nUsing input file: {input_filename}')
with open(input_filename) as f:
    santas_password = list(f.readline().rstrip())
print(f"This file's contents are:  {''.join(santas_password)}\n")

while True:
    # increment password
    santas_password = increment_password(santas_password)
    # check if valid
    if True:
        break

print(f'The resulting password is: {"".join(santas_password)}')

