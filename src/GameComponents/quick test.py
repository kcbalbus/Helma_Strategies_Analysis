from src.GameComponents.Board import Board
from src.GameComponents.Game import Game
from src.GameComponents.Player import Player
from src.Tactics.Strategies import *

if __name__ == '__main__':
    buffer =""

    board = Board('../boards/board_basic.csv')
    player_1 = Player(1, winning_position_distance_and_density)
    player_2 = Player(2, winning_position_distance_and_density)

    game = Game(board, player_1, player_2)
    game.play_game(depth_player1=1, depth_player2=3, use_alfa_beta=True)

    buffer+= (f'Player1: {board.check_win(1)}\n')
    buffer+= (f'Player2: {board.check_win(2)}\n')
    buffer+=(f'Player1 playing time: {player_1.playing_time}\n')
    buffer+=(f'Player2 playing time: {player_2.playing_time}\n\n')

    print(buffer)


"""
    board = Board('../boards/board_basic.csv')
    player_1 = Player(1, winning_position_distance_and_random)
    player_2 = Player(2, winning_position_distance_and_random)

    game = Game(board, player_1, player_2)
    game.play_game(depth_player1=1, depth_player2=3, use_alfa_beta=True)

    buffer += (f'Player1: {board.check_win(1)}\n')
    buffer += (f'Player2: {board.check_win(2)}\n')
    buffer += (f'Player1 playing time: {player_1.playing_time}\n')
    buffer += (f'Player2 playing time: {player_2.playing_time}\n\n')



    board = Board('../boards/board_basic.csv')
    player_1 = Player(1, winning_position_distance_and_jumps)
    player_2 = Player(2, winning_position_distance_and_jumps)

    game = Game(board, player_1, player_2)
    game.play_game(depth_player1=1, depth_player2=3, use_alfa_beta=True)

    buffer += (f'Player1: {board.check_win(1)}\n')
    buffer += (f'Player2: {board.check_win(2)}\n')
    buffer += (f'Player1 playing time: {player_1.playing_time}\n')
    buffer += (f'Player2 playing time: {player_2.playing_time}\n\n')



    board = Board('../boards/board_basic.csv')
    player_1 = Player(1, winning_position_distance_and_moves)
    player_2 = Player(2, winning_position_distance_and_moves)

    game = Game(board, player_1, player_2)
    game.play_game(depth_player1=1, depth_player2=3, use_alfa_beta=True)

    buffer += (f'Player1: {board.check_win(1)}\n')
    buffer += (f'Player2: {board.check_win(2)}\n')
    buffer += (f'Player1 playing time: {player_1.playing_time}\n')
    buffer += (f'Player2 playing time: {player_2.playing_time}\n\n')



    board = Board('../boards/board_basic.csv')
    player_1 = Player(1, winning_position_distance_and_density_and_moves)
    player_2 = Player(2, winning_position_distance_and_density_and_moves)

    game = Game(board, player_1, player_2)
    game.play_game(depth_player1=1, depth_player2=3, use_alfa_beta=True)

    buffer += (f'Player1: {board.check_win(1)}\n')
    buffer += (f'Player2: {board.check_win(2)}\n')
    buffer += (f'Player1 playing time: {player_1.playing_time}\n')
    buffer += (f'Player2 playing time: {player_2.playing_time}\n\n')


    print(buffer)


    board = Board('../boards/board_basic.csv')
    player_1 = Player(1, winning_position_distance_and_density)
    player_2 = Player(2, winning_position_distance_and_density)

    game = Game(board, player_1, player_2)
    game.play_game(depth_player1=1, depth_player2=2, use_alfa_beta=False)

    buffer += (f'Player1: {board.check_win(1)}\n')
    buffer += (f'Player2: {board.check_win(2)}\n')
    buffer += (f'Player1 playing time: {player_1.playing_time}\n')
    buffer += (f'Player2 playing time: {player_2.playing_time}\n\n')
"""