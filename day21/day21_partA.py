# adventOfCode 2015 day 21
# https://adventofcode.com/2015/day/21

from dataclasses import dataclass

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
            print(f'Initially:          ', end='')
        for player in self._players:
            print(f'{player._hit_points} ', end=' ')
        print()

    def play_round(self):
        # play the round
        self._round_number += 1
        
    def run_game(self, show_all_rounds = True):
        if len(self._players) != 2:
            raise LogicError('You can only play with exactly two players')
        while self._round_number < 11:
            if show_all_rounds:
                # Displaying status before the round is played
                self.display_status()
            self.play_round()
        # Displaying final status
        self.display_status()

the_game = Game()
the_game.add_player( Player(8, 5, 5, 'The player') )
the_game.add_player( Player(12, 7, 2, 'The boss') )
the_game.run_game()
