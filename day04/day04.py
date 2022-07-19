# adventOfCode 2015 day 04
# https://adventofcode.com/2015/day/04

import hashlib

# Reading input from the input file
input_filename='input_sample1.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    secret_key = f.readline().rstrip()

i=0
while True:
    i += 1    
    result = hashlib.md5((secret_key + str(i)).encode('utf-8')).hexdigest()
    if result[:5] == '00000':
        print(f'The answer to part A is: {i}')
        break
print()

i=0
while True:
    i += 1    
    result = hashlib.md5((secret_key + str(i)).encode('utf-8')).hexdigest()
    if result[:6] == '000000':
        print(f'The answer to part B is: {i}')
        break
print()
