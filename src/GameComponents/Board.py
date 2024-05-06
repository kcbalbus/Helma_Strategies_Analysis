import csv
import random

from src.GameComponents.Player import Player


class Board:
    def __init__(self, filename):
        self.size = 16
        self.board: list[list] = self.initialize_board_from_csv(filename)
        """self.player1_starting_positions = [
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
            (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
            (2, 0), (2, 1), (2, 2), (2, 3),
            (3, 0), (3, 1), (3, 2),
            (4, 0), (4, 1)
        ]
        self.player2_starting_positions = [
            (15, 15), (15, 14), (15, 13), (15, 12), (15,11),
            (14, 15), (14, 14), (14, 13), (14, 12), (14,11),
            (13, 15), (13, 14), (13, 13), (13, 12),
            (12, 15), (12, 14), (12, 13),
            (11, 15), (11, 14)
        ]"""

        self.player1_starting_positions = [(0, 0), (0, 1), (0, 2),(1, 0), (1, 1),(2, 0)]
        self.player2_starting_positions = [(15, 15), (15, 14), (15, 13),(14, 15), (14, 14),(13, 15)]

        #self.player1_starting_positions = [(0, 0)]
        #self.player2_starting_positions = [(15, 15)]

    def initialize_board_from_csv(self, filename):
        board = []
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file, delimiter=' ')
            for row in reader:
                board.append([int(value) for value in row])

        return board

    def check_win(self, player_number):
        if player_number == 1:
            winning_positions = self.player2_starting_positions
        elif player_number == 2:
            winning_positions = self.player1_starting_positions

        for position in winning_positions:
            if self.board[position[0]][position[1]] != player_number:
                return False

        return True

    def display_board(self):
        size = len(self.board)

        for i in range(size):
            for j in range(size):
                if self.board[i][j] == 0:
                    print(".  ", end="")
                else:
                    print(f"{self.board[i][j]:<3d}", end="")
            print(f"{i:3d}")

        print()
        print(0, end=" ")
        print(" ".join(f"{x:2d}" for x in (range(1, size))))


    def find_jumps(self, x, y, visited: set, initial_x, initial_y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        jumps = []
        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if(0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] != 0):
                jump_x, jump_y = nx + dx, ny + dy
                if(0 <= jump_x < self.size and 0 <= jump_y < self.size and self.board[jump_x][jump_y] == 0):
                    if((jump_x, jump_y) not in visited):
                        visited.add((jump_x, jump_y))
                        jumps.append((initial_x, initial_y, jump_x, jump_y))
                        jumps.extend(self.find_jumps(jump_x, jump_y, visited, x, y))
        return jumps

    def get_possible_moves(self, player_number):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for x in range(self.size):
            for y in range(self.size):
                if(self.board[x][y] == player_number):
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if(0 <= nx < self.size and 0 <= ny < self.size and self.board[nx][ny] == 0):
                            moves.append((x, y, nx, ny))
                    moves.extend(self.find_jumps(x, y, set(), x, y))

        random.shuffle(moves)
        return moves

    def is_no_more_possible_moves(self):
        return not self.get_possible_moves(1) or not self.get_possible_moves(2)

    def make_move(self, move):
        start_x, start_y, end_x, end_y = move
        self.board[end_x][end_y] = self.board[start_x][start_y]
        self.board[start_x][start_y] = 0

    def undo_move(self, move):
        start_x, start_y, end_x, end_y = move
        self.board[start_x][start_y] = self.board[end_x][end_y]
        self.board[end_x][end_y] = 0

    def get_score(self, player1, player2):
        return self.get_player_score(player1)-self.get_opponent_score(player1, player2)

    def get_player_score(self, player1):
        return player1.use_strategy(self.board, player1)

    def get_opponent_score(self, player1, player2):
        return player1.use_strategy(self.board, player2)


    def count_possible_jumps(self, player_number):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for x in range(self.size):
            for y in range(self.size):
                if (self.board[x][y] == player_number):
                    moves.extend(self.find_jumps(x, y, set(), x, y))

        print(len(moves))
        return len(moves)
