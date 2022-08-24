# adventOfCode 2015 day 21
# https://adventofcode.com/2015/day/21


# Plan for how to solve the problem:
# Brute force: consider all possible combinations of purchases of weapons, armor, rings
#   calculate the cost, damage, and armor for each combination
#   keep the lowest price option in dict brute_forced_options
#
# Run every combination of purchases through Game.run_game()
#   eliminate all items in dict brute_forced_options where player loses
#   
# Then sort the values in brute_forced_options ... the smallest cost is the answer to part A.


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

    # This returns None if there is no winner, or the winning player's name
    def play_round(self):
        index_attacker = self._round_number % 2
        index_defender = (index_attacker + 1) % 2
        self._players[index_defender]._hit_points -= max(1, self._players[index_attacker]._damage - self._players[index_defender]._armor)
        self._round_number += 1
        # If the attacker has won, return the attacker's name (who is the winner)
        if self._players[index_defender]._hit_points <= 0:
            return self._players[index_attacker]._name
        # If there isn't a winner yet, return None
        return None

    def run_game(self, show_rounds = True):
        if len(self._players) != 2:
            raise LogicError('You can only play with exactly two players')
        while True:
            if show_rounds:
                # Displaying status before the round is played
                self.display_status()
            the_winner = self.play_round()
            if the_winner is not None:
                break
        # Displaying final status
        if show_rounds:
            self.display_status()
            print()
        return the_winner

# Code created to test the above code
# by reproducing the given sample data 
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
# Reading input from the price list file
input_filename='shop_price_list.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    item_category = None
    for in_string in f:
        in_string = in_string.rstrip()
        if len(in_string) == 0:
            item_category = None
            continue
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

# Reading input from the puzzle input file
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

# purchase_quantities_per_category is .. quantities of items to purchase per category
for purchase_quantities_per_category in purchase_amount_options_iter:
    list_of_purchase_options = []
    for i, item_type_quantity in enumerate(purchase_quantities_per_category):
        if i == 0:
            # solo__cost_dmg_armr .. cost, damage, armor values for a single item
            # grp__cost_dmg_armr .. cost, damage, armor values for a single type of item (it could be a pair of rings)
            for grp__cost_dmg_armr in combinations(price_list[purchase_type[i]], item_type_quantity):
                for solo__cost_dmg_armr in grp__cost_dmg_armr:
                    list_of_purchase_options.append([np.asarray(solo__cost_dmg_armr)])
        else:
        #   go through each item in options and copy it so there are enough to cover all possibilities for the next item type, and append that to the list
            new_list_of_purchase_options = []
            for option_i in range(len(list_of_purchase_options)):
                for grp__cost_dmg_armr in combinations(price_list[purchase_type[i]], item_type_quantity):
                    new_list_of_purchase_options.append(copy.deepcopy(list_of_purchase_options[option_i]))
                    for solo__cost_dmg_armr in grp__cost_dmg_armr:
                        new_list_of_purchase_options[-1].append(np.asarray(solo__cost_dmg_armr))
            if len(new_list_of_purchase_options) > 0:
                list_of_purchase_options = new_list_of_purchase_options

    for single_purchase_option in list_of_purchase_options:
        single_purchase_option__totaled_cost_dmg_armr = np.array([0,0,0])
        # Total up the values of cost, damage, and armor for a given group of purchased items
        for nparray in single_purchase_option:
            single_purchase_option__totaled_cost_dmg_armr += nparray
        
        the_game = Game()
        the_game.add_player( Player(100, single_purchase_option__totaled_cost_dmg_armr[1], single_purchase_option__totaled_cost_dmg_armr[2], 'The player') )
        the_game.add_player( Player(boss_hit_points, boss_damage, boss_armor, 'The boss') )
        if the_game.run_game(False) == 'The player':
            dummy = 123
            player_variables = (single_purchase_option__totaled_cost_dmg_armr[1], single_purchase_option__totaled_cost_dmg_armr[2])
            if player_variables in brute_forced_options:
                brute_forced_options[player_variables] = min(brute_forced_options[player_variables] , single_purchase_option__totaled_cost_dmg_armr[0])
            else:
                brute_forced_options[player_variables] = single_purchase_option__totaled_cost_dmg_armr[0]

print(f'The answer is {min(brute_forced_options.values())}\n')

