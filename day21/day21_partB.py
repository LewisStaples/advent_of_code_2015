# adventOfCode 2015 day 21
# https://adventofcode.com/2015/day/21


# Plan for how to solve part B:
# Brute force: consider all possible combinations of purchases of weapons, armor, rings
#   calculate the cost, damage, and armor for each combination
#   keep the lowest price option in dict brute_forced_options
#
# Run every combination of purchases through Game.run_game()
#   eliminate all items in dict brute_forced_options where player loses
#   
# Then sort the values in brute_forced_options ... the largest cost is the answer to part B.


from dataclasses import dataclass  
from itertools import product, combinations
import copy
import numpy as np

class LogicError(Exception):
    pass

@dataclass
class Player:
    _hit_points: int
    _damage: int
    _armor: int
    _name: str

class Game:
    def __init__(self):
        self._players = []
        self._round_number = 0

    def add_player(self, player_to_add):
        if self._round_number > 0:
            raise LogicError("You can't add players while a game is playing")
        self._players.append(player_to_add)

    def display_status(self):
        if self._round_number > 0:
            print(f'After round # {self._round_number:3}:  ', end='')
        else:
            print()
            print(f"Player's Damage: {self._players[0]._damage}, Player's Armor {self._players[0]._armor}", end=", ")
            print(f"Boss' Damage {self._players[1]._damage}, Boss' Armor {self._players[1]._armor}")
            print('--------------------------------------------------')
            print("Player/Boss' Hit Pts |P. Hit Pts|B. Hit Pts")
            print(f'Initially:          ', end='')
        for player in self._players:
            print(f' |{player._hit_points:9}', end='')
        print()

    # This returns the hit points of the defending player
    # This returns None if there is no winner, or the winning player's name
    def play_round(self):
        # play the round
        index_attacker = self._round_number % 2
        index_defender = (index_attacker + 1) % 2
        self._players[index_defender]._hit_points -= max(1, self._players[index_attacker]._damage - self._players[index_defender]._armor)
        self._round_number += 1
        # return self._players[index_defender]._hit_points
        if self._players[index_defender]._hit_points <= 0:
            return self._players[index_attacker]._name
        # implicit else
        return None

    def run_game(self, show_all_rounds = True):
        if len(self._players) != 2:
            raise LogicError('You can only play with exactly two players')
        # while self._round_number < 8:
        while True:
            # if show_all_rounds:
            #     # Displaying status before the round is played
            #     self.display_status()
            # if self.play_round() is not None:
            #     # Stop playing
            #     break
            the_winner = self.play_round()
            if the_winner is not None:
                break
        # Displaying final status
        # self.display_status()
        # print()
        return the_winner

# Code created to test the above code ...    
the_game = Game()
the_game.add_player( Player(8, 5, 5, 'The player') )
the_game.add_player( Player(12, 7, 2, 'The boss') )
print(f'The winner is ... {the_game.run_game()}')

# Use brute force, considering all possible purchases, to determine all possible total combinations of price, damage, and armor.  If there are any repeats of damage and armor, then only consider the lowest priced version for that combination



@dataclass
class PurchaseCharacteristics:
    cost: int
    damage: int
    armor: int

# key = (damage, armor) combination
# value = lowest seen price
brute_forced_options = dict()

price_list = dict()
# Reading input from the input file
input_filename='shop_price_list.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    item_category = None
    for in_string in f:
        in_string = in_string.rstrip()
        if len(in_string) == 0:
            continue
            item_category = None
        if in_string[0].islower():
            item_category = in_string
            price_list[item_category] = set()
        else:
            [item_name, cost, damage, armor] = in_string.split()
            price_list[item_category].add( (int(cost), int(damage), int(armor)) )
print(price_list)

# You must buy exactly one weapon
# You can buy either 0 or 1 pieces of armor
# You can buy 0, 1, or 2 rings
purchase_amount_options_dict = {
    'weapons': [1],
    'armor': [0,1],
    'rings': [0,1,2]
}
purchase_type = ['weapons', 'armor', 'rings']

purchase_amount_options_iter = product(
    purchase_amount_options_dict['weapons'],
    purchase_amount_options_dict['armor'],
    purchase_amount_options_dict['rings']
)

print()

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        var_name, value_str = in_string.split(': ')
        value_int = int(value_str)
        if var_name == 'Hit Points':
            boss_hit_points = value_int
        elif var_name == 'Damage':
            boss_damage = value_int
        elif var_name == 'Armor':
            boss_armor = value_int

dummy = 123

for option in purchase_amount_options_iter:
    # print(f'Option: {option}')
    options = []
    for i, item_type_quantity in enumerate(option):
        # print(f'{item_type_quantity} of {purchase_type[i]}')
        if i == 0:
            for items in combinations(price_list[purchase_type[i]], item_type_quantity):
                for item in items:
                    options.append([np.asarray(item)])
        else:
        #   go through each item in options and copy it so there are enough to cover all possibilities for the next item type, and append that to the list
            new_options = []
            for option_i in range(len(options)):
                for items in combinations(price_list[purchase_type[i]], item_type_quantity):
                    new_options.append(copy.deepcopy(options[option_i]))
                    for item in items:
                        new_options[-1].append(np.asarray(item))
            if len(new_options) > 0:
                options = new_options

    # print()
    for option in options:
        # print(f'Option {option}')
        option_combined = np.array([0,0,0])
        for nparray in option:
            option_combined += nparray
        
        # print(f'Combined: {option_combined}')

        the_game = Game()
        the_game.add_player( Player(100, option_combined[1], option_combined[2], 'The player') )
        the_game.add_player( Player(boss_hit_points, boss_damage, boss_armor, 'The boss') )
        # print(f'The winner is ... {the_game.run_game()}')
        if the_game.run_game() == 'The boss':
            dummy = 123
            # brute_forced_options[(option_combined[1], option_combined[2])] = option_combined[0]
            player_variables = (option_combined[1], option_combined[2])
            if player_variables in brute_forced_options:
                brute_forced_options[player_variables] = max(brute_forced_options[player_variables] , option_combined[0])
            else:
                brute_forced_options[player_variables] = option_combined[0]

print(f'The answer is {max(brute_forced_options.values())}')

