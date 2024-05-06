
class Player:
    def __init__(self, player_number, strategy):
        self.playing_time = 0.0
        self.player_number = player_number
        self.strategy = strategy

    def use_strategy(self, board, player):
        return self.strategy(board, player)