# adventOfCode 2015 day 22
# https://adventofcode.com/2015/day/22

from dataclasses import dataclass  
from enum import Enum

class LogicError(Exception):
    pass

class PlayerID(Enum):
    THE_PLAYER = 0,
    THE_BOSS = 1

class SpellID(Enum):
    MAGIC_MISSILE = 0,
    DRAIN = 1,
    SHIELD = 2,
    POISON = 3,
    RECHARGE = 4

@dataclass
class Player:
    # current state
    _hit_points: int
    _damage: int
    _armor: int
    _mana: int
    _id: PlayerID
    _shield_remaining: int
    _poision_remaining: int
    _recharge_remaining: int

class Game:
    def __init__(self):
        self._players = []
        self._round_number = 0

        # self._player_spells = None

    def add_player(self, player_to_add):
        if self._round_number > 0:
            raise LogicError("You can't add players while a game is playing")
        self._players.append(player_to_add)
    
    def display_status(self):
        print(f'Round # {self._round_number} -- {self._players[self._round_number%2]._id} turn')
        for player in self._players:
            # print(f'- {player._id} has {player._hit_points} hit points, {player._armor} armor, {player._mana} mana')
            print(player)

    # This returns None if there is no winner.  If someone has won, their name will be returned.
    def play_round(self, spell=None):
        index_attacker = self._round_number % 2
        index_defender = (index_attacker + 1) % 2

        damage = self._players[index_attacker]._damage
        armor = self._players[index_defender]._armor

        if self._players[index_attacker] == PlayerID.THE_PLAYER:
            # Cast a spell
            if spell is None:
                # Determine all available spells (spells that are not yet active, have enough mana)
                # Then (perhaps) create new thread with its own unique object
                dummy = 123
                raise LogicError('Functionality not yet implemented !!!') # reminder to come back to this
            if spell is SpellID.MAGIC_MISSILE:
                self._players[index_attacker]._mana -= 53
                damage += 4
            if spell is SpellID.DRAIN:
                self._players[index_attacker]._mana -= 73
                damage += 2
                self._players[index_attacker]._hit_points += 2
            if spell is SpellID.SHIELD:
                self._players[index_attacker]._mana -= 113
                self._players[index_attacker]._shield_remaining = 6
            if spell is SpellID.POISON:
                self._players[index_attacker]._mana -= 173
                self._players[index_attacker]._poison_remaining = 6
            if spell is SpellID.RECHARGE:
                self._players[index_attacker]._mana -= 229
                self._players[index_attacker]._recharge_remaining = 5

            if self._players[index_attacker]._shield_remaining > 0:
                armor += 7
                self._players[index_attacker]._shield_remaining -= 1
            if self._players[index_attacker]._poison_remaining > 0:
                damage += 3
                self._players[index_attacker]._poison_remaining -= 1
            if self._players[index_attacker]._recharge_remaining > 0:
                self.player[index_attacker]._mana += 101
                self._players[index_attacker]._recharge_remaining -= 1

        self._players[index_defender]._hit_points -= max(1, damage - armor)

        self._round_number += 1
        # If the attacker has won, return the attacker's name (who is the winner)
        if self._players[index_defender]._hit_points <= 0:
            return self._players[index_attacker]._id
        
        # Update remaining variables

        # If there isn't a winner yet, return None
        return None

    def run_game(self, show_rounds = True, player_spells = {}):
        if len(self._players) != 2:
            raise LogicError('You can only play with exactly two players')

        while True:
            # Displaying final status
            if show_rounds:
                self.display_status()
                print()
            if self._round_number in player_spells:
                the_winner = self.play_round(player_spells[self._round_number])
            else:
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
print()
the_game = Game()
the_game.add_player( Player(10, 0, 0, 250, PlayerID.THE_PLAYER, 0, 0, 0) )
the_game.add_player( Player(13, 8, 0, 0, PlayerID.THE_BOSS, 0, 0, 0) )
the_game.run_game(True, {0 : SpellID.POISON, 2 : SpellID.MAGIC_MISSILE})

the_game = Game()
the_game.add_player( Player(10, 0, 0, 250, PlayerID.THE_PLAYER, 0, 0, 0) )
the_game.add_player( Player(14, 8, 0, 0, PlayerID.THE_BOSS, 0, 0, 0) )
the_game.run_game(True, {0 : SpellID.RECHARGE, 2: SpellID.SHIELD, 4: SpellID.DRAIN, 6: SpellID.POISON, 8: SpellID.MAGIC_MISSILE})

