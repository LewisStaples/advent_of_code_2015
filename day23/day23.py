# adventOfCode 2015 day 23
# https://adventofcode.com/2015/day/23

instructions = []
line_number = None
a=None
b=None


def hlf(register):
    globals()[register] = globals()[register] // 2

def inc(register):
    globals()[register] = globals()[register] + 1

def jie(params):
    register, offset = params.split(', ')
    if globals()[register] % 2 == 0:
        jmp(offset)

def jio(params):
    register, offset = params.split(', ')
    if globals()[register] == 1:
        jmp(offset)

def jmp(offset):
    globals()['line_number'] += int(offset) - 1

def tpl(register):
    globals()[register] = globals()[register] * 3

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        instructions.append(in_string)

line_number = 0
a = 0
b = 0
while line_number < len(instructions):
        command, params = instructions[line_number].split(' ',1)
        locals()[command](params)
        line_number += 1
print(f'The result to part A/1 is that b equals {b}\n')

line_number = 0
a = 1
b = 0
while line_number < len(instructions):
        command, params = instructions[line_number].split(' ',1)
        locals()[command](params)
        line_number += 1
print(f'The result to part B/2 is that b equals {b}\n')
