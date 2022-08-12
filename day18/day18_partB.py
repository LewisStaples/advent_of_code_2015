# adventOfCode 2015 day 18
# https://adventofcode.com/2015/day/18

debug = False

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
            i_neighbor = i + delta[0]
            j_neighbor = j + delta[1]
            if i_neighbor not in range(self._array_height) or j_neighbor not in range(self._array_width):
                # This neighbor is over an edge, so proceed to the next neighbor
                continue
            if self._light_arrays[prior_index][i_neighbor][j_neighbor] == '#':
                neighbor_lights_on_count += 1

        # "A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise."
        if debug:
            print(f'i,j ({i},{j}) has {neighbor_lights_on_count} lit neighbor(s)')
        if self._light_arrays[prior_index][i][j] == '#':
            if neighbor_lights_on_count in [2,3]:
                return '#'

        # "A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise."
        else:
            if neighbor_lights_on_count == 3:
                return '#'
        return '.'

    def update_array(self, step_number):
        prior_index = (step_number + 1) % 2
        current_index = step_number % 2
        for i in range(self._array_height):
            for j in range(self._array_width):
                self._light_arrays[current_index][i][j] = self.get_new_char(prior_index, i, j)
    
    def force_corners_on(self, step_number):
        current_index = step_number % 2
        self._light_arrays[current_index][0][0] = '#'
        self._light_arrays[current_index][self._array_height - 1][0] = '#'
        self._light_arrays[current_index][0][self._array_width - 1] = '#'
        self._light_arrays[current_index][self._array_height - 1][self._array_width - 1] = '#'

    def count_lights_on(self, step_number):
        ret_val = 0
        current_index = step_number % 2
        for i in range(self._array_height):
            for j in range(self._array_width):
                if self._light_arrays[current_index][i][j] == '#':
                    ret_val += 1

        return ret_val

MAX_STEP = 5
light_arrays = Light_arrays('input_sample0.txt')
light_arrays.force_corners_on(0)
for step_number in range(1, MAX_STEP + 1):
    light_arrays.update_array(step_number)
    light_arrays.force_corners_on(step_number)

print(f'Part B answer ... At the end {light_arrays.count_lights_on(step_number)} light(s) are on.')
print()




