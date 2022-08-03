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
            'distance_travelled': 0,
            'points_accumulated': 0,
            }

    # This gets the current reindeer speed,
    # which is either 0 (if resting), or the flight_speed (if not resting)
    def get_reindeer_speed(self, reindeer_name, time):
        # If at rest, return 0. Else return flight_speed
        remainder = (time) % (self._reindeer[reindeer_name]['flight_duration'] + self._reindeer[reindeer_name]['rest_duration'])
        if remainder > self._reindeer[reindeer_name]['flight_duration']:
            return 0
        return self._reindeer[reindeer_name]['flight_speed']


    def winning_reindeers_points(self, duration):
        for timestamp in range(1, duration+1):
            print(timestamp, end=': ')
            longest_travelled = {
                'distance': float('-inf'),
                'reindeer': []
            }
            # Update all reindeer's positions:
            for this_reindeer in self._reindeer:
                self._reindeer[this_reindeer]['distance_travelled'] += self.get_reindeer_speed(this_reindeer, timestamp)
        
                # If there's a tie
                if longest_travelled['distance'] == self._reindeer[this_reindeer]['distance_travelled']:
                    longest_travelled['reindeer'].append(this_reindeer)
                # Alternatively, if this is the longest yet seen
                if longest_travelled['distance'] < self._reindeer[this_reindeer]['distance_travelled']:
                    longest_travelled['distance'] = self._reindeer[this_reindeer]['distance_travelled']
                    longest_travelled['reindeer'] = [this_reindeer]

            # for the leading reindeer, add a point
            for this_reindeer in longest_travelled['reindeer']:
                # print(this_reindeer)
                self._reindeer[this_reindeer]['points_accumulated'] += 1
            
            # Printing only
            for this_reindeer in self._reindeer:
                dummy = 123
                # print(f'{this_reindeer}: Dist: {self._reindeer[this_reindeer]['distance_travelled']}', end=', ')
                print(f'{this_reindeer}: Dist=', end='')
                print(self._reindeer[this_reindeer]['distance_travelled'], end=', ')
                print('Points=', end='')
                print(self._reindeer[this_reindeer]['points_accumulated'], end=', ')
            print()
        # Return that point amount
        largest_point_amount = float('-inf')
        for this_reindeer in self._reindeer:
            largest_point_amount = max(largest_point_amount, self._reindeer[this_reindeer]['points_accumulated'])
        return largest_point_amount


# Reading input from the input file
input_filename='input_sample0.txt'
reindeerProperties = ReindeerProperties()

print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        reindeerProperties.add(in_string)

answer = reindeerProperties.winning_reindeers_points(150)
print(f'The answer to part B is {answer}')

