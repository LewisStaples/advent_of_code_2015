# adventOfCode 2015 day 14
# https://adventofcode.com/2015/day/14

class ReindeerProperties:
    def __init__(self):
        self._reindeer = dict()

    # Use a line of input to add another reindeer to ReindeerProperties
    def add(self, in_string):
        input_words = in_string.split(' ')

        self._reindeer[input_words[0]] = {
            'flight_speed': int(input_words[3]),
            'flight_duration': int(input_words[6]),
            'rest_duration': int(input_words[13]),
            }

    # Calculate total duration given cycle numbers if all flight and rest cycles were complete
    def calc_duration(self, flight_cycles, rest_cycles, value_dict):
        return flight_cycles * value_dict['flight_duration'] + rest_cycles * value_dict['rest_duration']

    # Calculate the distance travelled given the time elapsed (duration)
    def calc_timed_distance(self, value_dict, time):
        flight_cycles = 1
        rest_cycles = 0
        excess_flight_time = 0

        while self.calc_duration(flight_cycles, rest_cycles, value_dict) < time:
            if flight_cycles > rest_cycles:
                rest_cycles += 1
            else:
                flight_cycles += 1
        if flight_cycles > rest_cycles:
            excess_flight_time = self.calc_duration(flight_cycles, rest_cycles, value_dict) - time
        
        return flight_cycles * value_dict['flight_speed'] * value_dict['flight_duration'] - excess_flight_time * value_dict['flight_speed']

    # Calculate the maximum distance travelled
    def get_max_distance(self, time):
        ret_val = float('-inf')
        for value_dict in self._reindeer.values():
            ret_val = max(ret_val, self.calc_timed_distance(value_dict, time))
        return ret_val

# Reading input from the input file
input_filename='input.txt'
reindeerProperties = ReindeerProperties()

print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        reindeerProperties.add(in_string)

answer = reindeerProperties.get_max_distance(2503)
print(f'The answer to part A is {answer}')
