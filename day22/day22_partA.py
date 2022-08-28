# adventOfCode 2015 day 22
# https://adventofcode.com/2015/day/22

from dataclasses import dataclass  
from enum import Enum

class LogicError(Exception):
    pass

class SpellID(Enum):
    MAGIC_MISSILE = 0,
    DRAIN = 1,
    SHIELD = 2,
    POISON = 3,
    RECHARGE = 4

class Player:
    pass

    # _hit_points: int
    # _damage: int

class Wizard(Player):
    def __init__(self, hit_points, mana):
        # current state
        self._hit_points = hit_points
        self._damage = 0
        self._armor = 0
        self._mana = mana

        # timers
        self._shield_remaining = 0
        self._recharge_remaining = 0

# @dataclass
class Boss(Player):
    def __init__(self, hit_points, damage):
        self._hit_points = hit_points
        self._damage = damage

class Game:
    def __init__(self, wizard_hp, wizard_mana, boss_input_filename, games_list, rounds_to_show = []):
        self._wizard = Wizard(wizard_hp, wizard_mana)
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
                # print(in_string)
        self._boss = Boss(boss_hp, boss_damage)
        self._round_number = 0
        self._games_list = games_list
        self._rounds_to_show = rounds_to_show

    def show_status(self):
        if len(self._rounds_to_show) == 0:
            return # not displaying this one
        print(f'-- turn --')

    def run_game(self):
        while True:
            # self.wizard_round()
            # self.boss_round()
            break # TO BE REPLACED LATER (for now it's here to prevent infinite loops)

# First sample given:
games_s0 = []
games_s0.append(Game(10, 250, 'input_sample0.txt', games_s0, [SpellID.POISON, SpellID.MAGIC_MISSILE]))
games_s0[0].run_game()

