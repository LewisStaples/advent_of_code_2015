# adventOfCode 2015 day 22
# https://adventofcode.com/2015/day/22

from dataclasses import dataclass  
from enum import Enum
from abc import ABC, abstractmethod
import copy
from webbrowser import get

class LogicError(Exception):
    pass

# class SpellID(Enum):
#     MAGIC_MISSILE = 0,
#     DRAIN = 1,
#     SHIELD = 2,
#     POISON = 3,
#     RECHARGE = 4

class Player:
    def __init__(self, hit_points, damage):
        self.hit_points = hit_points
        self.damage = damage



class Wizard(Player):
    # static variable
    spell_list = [
        {'spell_name': 'magic_missile', 'mana_cost': 53},
        {'spell_name': 'drain', 'mana_cost': 73},
        {'spell_name': 'shield', 'mana_cost': 113},
        {'spell_name': 'poison', 'mana_cost': 173},
        {'spell_name': 'recharge', 'mana_cost': 229}
    ]

    def __init__(self, hit_points, mana):
        # current state
        self.hit_points = hit_points
        self.damage = 0
        self.armor = 0
        self.mana = mana

        # timers
        self.magic_missile_remaining = 0
        self.drain_remaining = 0
        self.shield_remaining = 0
        self.poison_remaining = 0
        self.recharge_remaining = 0

    def cast_magic_missile(self):
        # self.mana -= 53
        self.magic_missile_remaining = 1
        self.damage += 4
    
    def cast_drain(self):
        # self.mana -= 73
        self.damage += 2
        self.hit_points += 2

    def cast_shield(self):
        # self.mana -= 113
        self.shield_remaining = 7
        self.armor += 7

    def cast_poison(self):
        # self.mana -= 173
        self.poison_remaining = 7

    def cast_recharge(self):
        # self.mana -= 229
        self.recharge_remaining = 5



    def get_status(self):
        return f'{self.hit_points} hit points, {self.armor} armor, {self.mana} mana'

class Boss(Player):
    def __init__(self, hit_points, damage):
        super().__init__(hit_points, damage)

    def get_status(self):
        return f'{self.hit_points} hit points'


class Game:
    # static variable
    min_mana_win: int

    def __init__(self, wizard_hp, wizard_mana, boss_input_filename, round_number, rounds_to_show = []):
        self.wizard = Wizard(wizard_hp, wizard_mana)
        print(f'\nUsing boss paramater input file: {boss_input_filename}\n')
        with open(boss_input_filename) as f:
            # Pull in each line from the input file
            for in_string in f:
                in_string = in_string.rstrip()
                varname, value = in_string.split(': ')
                if varname == 'Hit Points':
                    boss_hp = int(value)
                elif varname == 'Damage':
                    boss_damage = int(value)
        self.boss = Boss(boss_hp, boss_damage)

        # Odd round numbers are played by the wizard/player, 
        # and even round numbers are played by the boss
        self.round_number = round_number
        
        # The purpose of this variable is to display to user information about the sample spells
        # (All other permutations of spells won't be shown)
        self.rounds_to_show = rounds_to_show

    def print_status(self):
        print(f'-Player has ', end='')
        print(self.wizard.get_status())
        print(f'-Boss has ', end='')
        print(self.boss.get_status())

    def round_start(self):
        # Process Wizard's timers
        if self.wizard.magic_missile_remaining > 0:
            self.wizard.magic_missile_remaining -= 1
            if self.wizard.magic_missile_remaining == 0:
                self.wizard.damage -= 4
        if self.wizard.drain_remaining > 0:
            self.wizard.drain_remaining -= 1
            if self.wizard.drain_remaining == 0:
                self.wizard.damage -= 2
        if self.wizard.shield_remaining > 0:
            self.wizard.shield_remaining -= 1
            if self.wizard.shield_remaining == 0:
                self.wizard.armor -= 7
        if self.wizard.poison_remaining > 0:
            self.wizard.poison_remaining -= 1
            self.boss.hit_points -= 3
            print(f'Poison deals 3 damage; its timer is now {self.wizard.poison_remaining}.')
        if self.wizard.recharge_remaining> 0:
            self.wizard.mana += 101
            print(f'Recharge provides 101 mana; its timer is now {self.wizard.recharge_remaining}.')
            self.wizard.recharge_remaining -= 1
        

        # Calculate hit point loss of the party under attack
        # Note for the wizard, this implies each of the scenarios
        if self.round_number % 2 == 0:
            self.boss.hit_points -= max(1, self.wizard.damage)
        else:
            self.wizard.hit_points -= max(1, self.boss.damage - self.wizard.armor)



# End of class Game


def play_game(game_list):
    Game.min_mana_win = float('inf')
    while len(game_list) > 0:
        this_game = game_list.pop()
        this_game.round_start()
        if this_game.round_number % 2 == 0:
            for i in range(5):
                spell_mana_cost = Wizard.spell_list[i]['mana_cost']
                if spell_mana_cost > this_game.wizard.mana:
                    # Not enough mana to cast this particular spell
                    continue
                if i < 4:
                    # make a new deep copy
                    new_game = copy.deepcopy(this_game)
                else:
                    new_game = this_game
                # cast a spell
                getattr(new_game.wizard, 'cast_' + Wizard.spell_list[i]['spell_name'])
                if new_game.wizard.hit_points < 0:
                    # The wizard ran out of h.p. ... doesn't count to objective
                    continue
                # update round number
                new_game.round_number += 1

                # put back on the list
                game_list.insert(0, new_game)
                pass
           
            dummy = 123
        else:
            pass
        # Update round number
        this_game.round_number += 1

    print(f'The minimum mana that can be spent on a win is {Game.min_mana_win}')


def test_sample_zero():
    print('Testing sample zero ...')
    game_list = [Game(10, 250, 'input_sample0.txt', 0, [Wizard.spell_list[3]['spell_name'], Wizard.spell_list[0]['spell_name']])]
    play_game(game_list)

test_sample_zero()



