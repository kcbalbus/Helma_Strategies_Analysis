from src.GameComponents.Board import Board
from src.GameComponents.Game import Game
from src.GameComponents.Player import Player
from src.Tactics.Strategies import *

if __name__ == '__main__':
    board = Board('../boards/board_basic.csv')
    player_1 = Player(1, winning_position_distance)
    player_2 = Player(2, winning_position_distance)

    game = Game(board, player_1, player_2)
    game.play_game_2(depth_player1=1, depth_player2=2, use_alfa_beta=False)

    print(f'Player1 playing time: {player_1.playing_time}')
    print(f'Player2 playing time: {player_2.playing_time}')


    board.display_board()