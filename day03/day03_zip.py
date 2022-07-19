# adventOfCode 2015 day 03
# https://adventofcode.com/2015/day/03


# Reading input from the input file
input_filename='input_sample2.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
   

chr_coor_delta_dict = {'^':[0,1], 'v':[0,-1], '>':[1,0], '<':[-1,0]}

# Part A
curr_coords = [0,0]
visited_house_coords_A = set()
visited_house_coords_A.add((0,0))
for ch in in_string:
    curr_coords = [a+b for a,b in zip(curr_coords, chr_coor_delta_dict[ch])]
    visited_house_coords_A.add(tuple(curr_coords))
print(f'The answer to A is {len(visited_house_coords_A)}')

# Part B
REGULAR_SANTA_ID = 0
ROBO_SANTA_ID = 1
curr_coords_B = {
    REGULAR_SANTA_ID: [0,0],
    ROBO_SANTA_ID: [0,0]
}
visited_house_coords_B = set()
visited_house_coords_B.add((0,0))

for i, ch in enumerate(in_string):
    curr_coords_B[i%2] = [a+b for a,b in zip(curr_coords_B[i%2], chr_coor_delta_dict[ch])]
    visited_house_coords_B.add(tuple(curr_coords_B[i%2]))

print(f'The answer to B is {len(visited_house_coords_B)}')
