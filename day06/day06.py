# adventOfCode 2015 day 15
# https://adventofcode.com/2015/day/15


class Lights:
    def __init__(self):
        self.light_grid = [[False for y in range(1000)] for x in range(1000)]

    def get_turn_on_value(self, i, j):
        return True

    def get_turn_off_value(self, i, j):
        return False

    # Return toggled boolean state of the light
    def get_toggle_value(self, i, j):
        return self.light_grid[i][j] != True

    def update_light(self, operation, i, j):
        self.light_grid[i][j] = getattr(self, operation)(i,j)

    def update_grid(self, parms):
        dummy = 123
        for i in range(parms[1][0], parms[2][0]+1):
            for j in range(parms[1][1], parms[2][1]+1):
                self.update_light(parms[0], i, j)

    def count_lights_on(self):
        ret_val = 0
        for i in range(len(self.light_grid)):
            for j in range(len(self.light_grid[0])):
                if self.light_grid[i][j]:
                    ret_val += 1
        return ret_val


lights = Lights()

# This parses a line of input from the instructions
# and it returns a 3-tuple of type (str, 2-tuple, 2-tuple), which are
# (turn_on/turn_off/toggle, coords. of lower bound x,y, coords of upper bound x,y)
def parse(in_string):
    operation_mid_str, right_str = in_string.split(' through ')
    split_index = operation_mid_str.rfind(' ')
    operation_str = 'get_' + operation_mid_str[:split_index].replace(' ', '_') + '_value'
    mid_str = operation_mid_str[split_index+1:]
    lower_bounds = tuple(int(x) for x in mid_str.split(','))
    upper_bounds = tuple(int(x) for x in right_str.split(','))
    return (operation_str, lower_bounds, upper_bounds)


input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        lights.update_grid(parse(in_string))

print(f'There are {lights.count_lights_on()} light(s) on.')
print()


