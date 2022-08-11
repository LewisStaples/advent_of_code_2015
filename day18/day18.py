# adventOfCode 2015 day 18
# https://adventofcode.com/2015/day/18

from operator import ne


class Light_arrays:
    def __init__(self, input_filename):
        # light_arrays will have two indices, and each will point to a 2-d list showing all characters in the array
        # index 0 will be the array for an even step number (0, 2, 4, etc.)
        # index 1 will be the array for an odd  step number (1, 3, 5, etc.)
        self._light_arrays = [[], []]

        print(f'\nReading from input file: {input_filename}\n')
        with open(input_filename) as f:
            # Pull in each line from the input file
            for line_number, in_string in enumerate(f):
                in_string = in_string.rstrip()
                # Initialize with initial state
                self._light_arrays[0].append([ch for ch in in_string]) 
                # Initialize with dummy characters (so it can be easily modifiable later)
                self._light_arrays[1].append([None for ch in in_string])
        self._array_height = line_number + 1
        self._array_width = len(in_string)

    def get_new_char(self, prior_index, i, j):
        # Count the number of neighbor lights that are on
        neighbor_lights_on_count = 0
        for delta in [(-1,-1),(-1,0),(-1,1),(0,-1,),(0,1),(1,-1),(1,0),(1,1)]:
            try:
                if self._light_arrays[prior_index][i + delta[0]][j+delta[1]] == '#':
                    neighbor_lights_on_count += 1
            except IndexError:
                # This neighbor is over an edge, so proceed to the next one
                continue
        # A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
        if self._light_arrays[prior_index][i][j] == '#':
            if neighbor_lights_on_count in [2,3]:
                return '#'

        # A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
        else:
            if neighbor_lights_on_count == 3:
                return '#'
        return '.'

    def update_array(self, step_number):
        prior_index = (step_number + 1) % 2
        current_index = step_number % 2
        print(f'step_no.: {step_number}, prior_i: {prior_index}, current_i: {current_index}')
        for i in range(self._array_height):
            for j in range(self._array_width):
                self._light_arrays[current_index][i][j] = self.get_new_char(prior_index, i, j)
        
        dummy = 123

# # Reading input from the input file
# input_filename='input_sample0.txt'
# print(f'\nUsing input file: {input_filename}\n')
# with open(input_filename) as f:
#     # Pull in each line from the input file
#     for line_number, in_string in enumerate(f):
#         in_string = in_string.rstrip()
#         # Initialize with initial state
#         light_arrays[0].append([ch for ch in in_string]) 
#         # Initialize with dummy characters (so it can be easily modifiable later)
#         light_arrays[1].append([None for ch in in_string])


MAX_STEP = 4
light_arrays = Light_arrays('input_sample0.txt')
for step_number in range(1, MAX_STEP + 1):
    light_arrays.update_array(step_number)

dummy = 123


    # prior_index = (step_number + 1) % 2
    # current_index = step_number % 2
    # print(f'step_no.: {step_number}, prior_i: {prior_index}, current_i: {current_index}')
    # for i in range(array_height):
    #     for j in range(array_width):
    #         pass

