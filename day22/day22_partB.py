# adventOfCode 2015 day 22
# https://adventofcode.com/2015/day/22


import copy

class Wizard():
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
        self.armor = 0
        self.mana = mana
        self.mana_spent = 0

        # timers
        self.shield_remaining = 0
        self.poison_remaining = 0
        self.recharge_remaining = 0

    def cast_magic_missile(self):
        return {'hit_points':-4, 'message':'Because player has cast Magic Missile, damage of 4 is dealt.'}

    
    def cast_drain(self):
        self.hit_points += 2
        return {'hit_points':-2, 'message':'Because player has cast Drain, damage of 2 is dealt.'}

    def cast_shield(self):
        self.shield_remaining = 6
        self.armor += 7
        return {}

    def cast_poison(self):
        self.poison_remaining = 6
        return {}

    def cast_recharge(self):
        self.recharge_remaining = 5
        return {}

    def get_status(self):
        return f'{self.hit_points} hit points, {self.armor} armor, {self.mana} mana'

class Boss():
    def __init__(self, hit_points, damage):
        self.hit_points = hit_points
        self.damage = damage

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
        ret_val = '\n'
        if self.round_number % 2 == 0:
            ret_val += f'-- Player turn --\n'
        else:
            ret_val += f'-- Boss turn --\n'
        ret_val += f'-Player has ' + self.wizard.get_status() + '\n'
        ret_val += f'-Boss has ' + self.boss.get_status()
        return ret_val


    def round_start(self):  
        # part B (part 2) code
        if self.round_number % 2 == 0:
            self.wizard.hit_points -= 1
            if self.wizard.hit_points <= 0:
                return 'END'

        ret_val = self.print_status()
        if self.wizard.shield_remaining > 0:
            self.wizard.shield_remaining -= 1
            if self.wizard.shield_remaining == 0:
                self.wizard.armor -= 7
            ret_val += f"\nSpell shield's timer is now {self.wizard.shield_remaining}."
        if self.wizard.poison_remaining > 0:
            self.wizard.poison_remaining -= 1
            self.boss.hit_points -= 3
            ret_val += f"\nPoison deals 3 damage; Spell poison's timer is now {self.wizard.poison_remaining}."
        if self.wizard.recharge_remaining> 0:
            self.wizard.mana += 101
            self.wizard.recharge_remaining -= 1
            ret_val += f"\nRecharge provides 101 mana; Spell recharge's timer is now {self.wizard.recharge_remaining}."
            
    
        if self.boss.hit_points <= 0:
            Game.min_mana_win = min(Game.min_mana_win, self.wizard.mana_spent)
            ret_val += f'\nThe boss is dead (down to {self.boss.hit_points} hit points)\nEND'
            return ret_val

        if self.round_number % 2 == 1:
            # Boss attacking ... calculated using Day 21's logic
            damage_inf_by_boss = max(1, self.boss.damage - self.wizard.armor)
            self.wizard.hit_points -= damage_inf_by_boss
            ret_val += f'\nBoss attacks for {damage_inf_by_boss} damage'
            if self.wizard.hit_points <= 0:
                ret_val += '\nEND'

        return ret_val
# End of class Game


def play_game(game_list):
    Game.min_mana_win = float('inf')
    while len(game_list) > 0:
        this_game = game_list.pop()
        ret_val = this_game.round_start()
        if ret_val[-3:] == 'END':
            if this_game.rounds_to_show != []:
                print(ret_val)
            continue
        if this_game.round_number % 2 == 0:
            # Command for wizard's/player's turn
            for i in range(5):
                spell_mana_cost = Wizard.spell_list[i]['mana_cost']
                if spell_mana_cost > this_game.wizard.mana:
                    # Not enough mana to cast this particular spell
                    continue
                
                if Wizard.spell_list[i]['spell_name']+"'s timer is now" in ret_val:
                    if Wizard.spell_list[i]['spell_name']+"'s timer is now 0" not in ret_val:
                        continue
                if i < 4:
                    # make a new deep copy
                    new_game = copy.deepcopy(this_game)
                else:
                    new_game = this_game
                # cast a spell
                new_game.wizard.mana -= spell_mana_cost
                new_game.wizard.mana_spent += spell_mana_cost
                if new_game.wizard.mana_spent >= Game.min_mana_win:
                    # Discard new_game if its mana won't be less than the already known global minimum
                    continue
                if new_game.rounds_to_show != []:
                    popped_spell = new_game.rounds_to_show.pop(0)
                    if Wizard.spell_list[i]['spell_name'] != popped_spell:
                        new_game.rounds_to_show = []
                    else:
                        print(ret_val)
                        print('Player casts ' + Wizard.spell_list[i]['spell_name'])
                        if new_game.rounds_to_show == []:
                            # This is to show the boss found following the last displayed wizard round
                            # (if there is one)
                            new_game.rounds_to_show = ['display_boss_round']
                # Return object has message or changes to instance variables of boss object
                ret_obj = getattr(new_game.wizard, 'cast_' + Wizard.spell_list[i]['spell_name'])()
                for key, val in ret_obj.items():
                    if key == 'message':
                        if new_game.rounds_to_show != []:
                            print(val)
                    else:
                        # Changes to instance variables of boss object
                        # (Note that any changes to wizard object aren't returned:
                        # they're made in the cast* method directly)
                        new_value = getattr(new_game.boss, key) + val
                        setattr(new_game.boss, key, new_value)

                if new_game.wizard.hit_points < 0:
                    # The wizard ran out of h.p. ... doesn't count to objective
                    continue
                # update round number
                new_game.round_number += 1
                # put back on the list
                game_list.insert(0, new_game)
        
        else:
            # Commands for boss' turn
            if this_game.rounds_to_show != []:
                print(ret_val)
            this_game.round_number += 1
            game_list.insert(0, this_game)

    print(f'\nThe minimum mana that can be spent on a win is {Game.min_mana_win}\n')


def test_partA_graded():
    print('Testing graded problem ... ')
    game_list = [Game(50, 500, 'input.txt', 0, [])]
    play_game(game_list)

# test_sample_zero()
# test_sample_one()

test_partA_graded()

