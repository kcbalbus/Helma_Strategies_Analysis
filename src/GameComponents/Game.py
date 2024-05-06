from copy import deepcopy
import time
from ..Tactics import *
from ..Tactics.MoveFunctions import minmax


class Game:
    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2

    def play_game(self, depth, algorithm_name="minmax"):
        current_player = self.player_1
        opposite_player =self.player_2
        while (not self.board.is_no_more_possible_moves()):
            start_time = time.time()
            if (self.board.check_win(current_player.player_number)):
                print(f'Player_{current_player.player_number} win')
                return
            if (self.board.check_win(opposite_player.player_number)):
                print(f'Player_{opposite_player.player_number} win')
                return

            move = self.find_best_move_for_player(current_player, opposite_player, depth, algorithm_name)
            if (move):
                self.board.make_move(move)
                self.board.display_board()
                print(f'player_{current_player.player_number} {move}')
            else:
                print(f'No more moves for player_{current_player.player_number}')
                break
            current_player.playing_time += (time.time() - start_time)
            current_player = self.player_2 if current_player == self.player_1 else self.player_1
            opposite_player = self.player_1 if current_player == self.player_2 else self.player_2

        print("Game over")

    def find_best_move_for_player(self, current_player, opposite_player, depth, algorithm_name):

        if (algorithm_name == 'alfabeta'):
            pass
            #(score, best_move) = minmax_alfabeta(
            #    self.board,
             #   depth,
              #  current_player,
               # current_player,
               # enemy,
                #float('-inf'),
                #float('inf')
            #)
        else:
            (score, best_move) = minmax(
                self.board,
                depth,
                current_player,
                current_player,
                opposite_player
            )
        return (best_move)


