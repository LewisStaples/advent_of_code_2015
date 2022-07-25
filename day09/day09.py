# adventOfCode 2015 day 09
# https://adventofcode.com/2015/day/09

import itertools

class LocationInfo:
    def __init__(self):
        self._locations = set()
        self._journey_legs = dict()
    
    def input_a_line(self, line_of_input):
        left_of_equals, right_of_equals = line_of_input.split(' = ')
        locn1, locn2 = left_of_equals.split(' to ')
        self._locations.add(locn1)
        self._locations.add(locn2)

        # Avoid duplicate pairs in self._journey_legs
        index = (locn1,locn2) if locn1 < locn2 else (locn2,locn1)
        self._journey_legs[index] = int(right_of_equals)

    def get_distance(self, path):
        distance = 0
        while len(path) > 1:
            distance += self._journey_legs[tuple(sorted(path[-2:]))]
            path.pop()
        return distance

    def get_shortest_distance(self):
        shortest_distance = float('inf')
        for path in itertools.permutations(self._locations):
            # Avoid duplicate paths that are same forward vs. backward
            if path[0] > path[-1]:
                continue
            shortest_distance = min(shortest_distance, self.get_distance(list(path)))
        return shortest_distance


location_info = LocationInfo()
# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        location_info.input_a_line(in_string)

location_info.get_shortest_distance()

print(f'\nThe final result is {location_info.get_shortest_distance()}\n')

