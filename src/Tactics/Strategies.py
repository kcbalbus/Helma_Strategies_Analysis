from math import sqrt
import random


def random_moves():
    return random.randint(-10, 10)



def density(board: list[list], player):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    score = 0

    for x in range(len(board)):
        for y in range(len(board)):
            if(board[x][y] == player.player_number):
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if(0 <= nx < len(board) and 0 <= ny < len(board)):
                        if(board[nx][ny] == player.player_number):
                            score += 1
    return score



def winning_position_distance(board, player):
    score = 0
    start_position = 0 if player.player_number == 1 else 15

    for x in range(len(board)):
        for y in range(len(board)):
            if (board[x][y] == player.player_number):
                rows_distance = (x - start_position)
                columns_distance = (y - start_position)
                distance = sqrt(abs(rows_distance) + abs(columns_distance))
                score += distance

    return score



def winning_position_distance_and_density(board, player):
    winning_position_distance_score = winning_position_distance(board, player) * 5
    density_score = density(board, player)

    combined_score = winning_position_distance_score + density_score

    return combined_score

def winning_position_distance_and_random(board, player):
    winning_position_distance_score = winning_position_distance(board, player) * 5
    random_score = random_moves()

    combined_score = winning_position_distance_score + random_score

    return combined_score

"""
def possible_jumps(board, player):
    possible_jumps_score = board.count_possible_jumps(player.player_number)
    
    return possible_jumps_score


def winning_position_distance_and_jumps(board, player):
    winning_position_distance_score = winning_position_distance(board, player) * 5
    jumps_score = possible_jumps(board, player)

    combined_score = winning_position_distance_score + jumps_score

    return combined_score
"""