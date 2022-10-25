# adventOfCode 2015 day 22
# https://adventofcode.com/2015/day/22

from dataclasses import dataclass  
from enum import Enum
from abc import ABC, abstractmethod
from copy import deepcopy

class LogicError(Exception):
    pass

class SpellID(Enum):
    MAGIC_MISSILE = 0,
    DRAIN = 1,
    SHIELD = 2,
    POISON = 3,
    RECHARGE = 4

class Player:
    def __init__(self, hit_points, damage):
        self.hit_points = hit_points
        self.damage = damage

    @abstractmethod
    def play_round(self):
        pass

class Wizard(Player):
    def __init__(self, hit_points, mana):
        # current state
        self.hit_points = hit_points
        self.damage = 0
        self.armor = 0
        self.mana = mana

        # timers
        self.drain_remaining = 0
        self.shield_remaining = 0
        self.poison_remaining = 0
        self.recharge_remaining = 0

    def cast_magic_missile(self):
        pass
    
    def cast_drain(self):
        pass

    def cast_shield(self):
        pass

    def cast_poison(self):
        pass

    def cast_recharge(self):
        pass

    def play_round(self):
        pass

    def get_status(self):
        return f'{self.hit_points} hit points, {self.armor} armor, {self.mana} mana'

class Boss(Player):
    def __init__(self, hit_points, damage):
        super().__init__(hit_points, damage)

    def play_round(self):
        return 'dummy value'


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
        self.round_number = round_number
        
        # The purpose of this variable is to display to user information about the sample spells
        # (All other permutations of spells won't be shown)
        self.rounds_to_show = rounds_to_show

    def print_status(self):
        print(f'-Player has ', end='')
        print(self.wizard.get_status())
        print(f'-Boss has ', end='')
        print(self.boss.get_status())

    def next_round(self):
        pass


def test_sample_zero():
    print('Testing sample zero ...')
    game_list = [Game(10, 250, 'input_sample0.txt', 0, [SpellID.POISON, SpellID.MAGIC_MISSILE])]
    Game.min_mana_win = float('inf')
    while len(game_list) > 0:
        this_game = game_list.pop()
        this_game.next_round()

    print(f'The minimum mana that can be spent on a win is {Game.min_mana_win}')




