# adventOfCode 2015 day 11
# https://adventofcode.com/2015/day/11

def increment_password(santas_password):
    str_len = len(santas_password)
    for i in range(str_len - 1, -1, -1):
        # print(f'index: {i}, char: {santas_password[i]}')
        if santas_password[i] == 'z':
            santas_password[i] = 'a'
            continue
        santas_password[i] = chr(ord(santas_password[i]) + 1)
        break
    return santas_password

def requirement_one_fails(santas_password):
    for i in range(0, len(santas_password)-2):
        if ord(santas_password[i]) + 1 == ord(santas_password[i + 1]):
            if ord(santas_password[i + 1]) + 1 == ord(santas_password[i + 2]):
                # Requirement 1 has been met
                return False
    return True

def requirement_two_fails(santas_password):
    for ch in 'iol':
        if ch in santas_password:
            return True
    return False


def requirement_three_fails(santas_password):
    i_match = None
    for i in range(0, len(santas_password)-1):
        if ord(santas_password[i]) + 1 == ord(santas_password[i + 1]):
            if i_match is None:
                i_match = i
            else:
                if i_match > i+1:
                    return False
    return True

def is_valid(santas_password):
    if requirement_one_fails(santas_password):
        return False
    if requirement_two_fails(santas_password):
        return False
    # if requirement_three_fails(santas_password):
        # return False
    return True

# Reading input from the input file
input_filename='input_sample3.txt'
print(f'\nUsing input file: {input_filename}')
with open(input_filename) as f:
    santas_password = list(f.readline().rstrip())
print(f"This file's contents are:  {''.join(santas_password)}\n")

while True:
    santas_password = increment_password(santas_password)
    if is_valid(santas_password):
        break

print(f'The resulting password is: {"".join(santas_password)}')

