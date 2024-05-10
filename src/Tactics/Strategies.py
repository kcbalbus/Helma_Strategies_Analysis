from math import sqrt
import random

from src.GameComponents.Board import Board


def random_moves():
    return random.randint(-10, 10)

def density(board: Board, player):
    score = board.count_density(player.player_number)
    return score

def possible_moves_forward(board, player):
    possible_moves_score = board.count_possible_moves_forward(player.player_number)
    return possible_moves_score

def possible_jumps_forward(board, player):
    possible_jumps_score = board.count_possible_jumps_forward(player.player_number)
    return possible_jumps_score

def winning_position_distance(board, player):
    win_score = board.check_on_winning(player.player_number)*50
    score = board.count_distance(player.player_number)
    return score+win_score

def winning_position_distance_and_density(board, player):
    winning_position_distance_score = winning_position_distance(board, player) * 10
    density_score = density(board, player)

    combined_score = winning_position_distance_score + density_score

    return combined_score

def winning_position_distance_and_random(board, player):
    winning_position_distance_score = winning_position_distance(board, player) * 15
    random_score = random_moves()

    combined_score = winning_position_distance_score + random_score

    return combined_score


def winning_position_distance_and_jumps(board, player):
    winning_position_distance_score = winning_position_distance(board, player) * 35
    jumps_score = possible_jumps_forward(board, player)

    combined_score = winning_position_distance_score + jumps_score

    return combined_score

def winning_position_distance_and_moves(board, player):
    winning_position_distance_score = winning_position_distance(board, player) * 40
    moves_score = possible_moves_forward(board, player)

    combined_score = winning_position_distance_score + moves_score

    return combined_score

def winning_position_distance_and_density_and_moves(board, player):
    winning_position_distance_score = winning_position_distance(board, player) * 55
    density_score = density(board, player)
    moves_score = possible_moves_forward(board, player)

    combined_score = winning_position_distance_score + moves_score + density_score

    return combined_score

