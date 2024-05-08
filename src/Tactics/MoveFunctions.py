def minmax(board, depth, current_player, player_1, player_2):

    if (depth == 0 or board.is_no_more_possible_moves()):
        return (board.get_score(player_1, player_2), None)

    if (board.check_win(player_1.player_number)):
        return (float('inf'), None)

    if (board.check_win(player_2.player_number)):
        return (float('-inf'), None)

    if (current_player == player_1):
        max_score = float('-inf')
        best_move = None
        possible_moves = board.get_possible_moves(current_player.player_number)
        for move in possible_moves:
            board.make_move(move)
            score, previuos_best_move = minmax(
                board,
                depth - 1,
                player_2,
                player_1,
                player_2
            )

            board.undo_move(move)
            if (score > max_score):
                max_score = score
                best_move = move

        return (max_score, best_move)

    else:
        min_score = float('inf')
        min_move = None
        possible_moves = board.get_possible_moves(current_player.player_number)
        for move in possible_moves:
            board.make_move(move)
            score, previous_best_move = minmax(
                board,
                depth - 1,
                player_1,
                player_1,
                player_2
            )

            board.undo_move(move)
            if (score < min_score):
                min_score = score
                min_move = move

        return (min_score, min_move)


def minmax_alfabeta(board, depth, current_player, player_1, player_2, alfa, beta):

    if (depth == 0 or board.is_no_more_possible_moves()):
        return (board.get_score(player_1, player_2), None)

    if (board.check_win(player_1.player_number)):
        return (float('inf'), None)

    if (board.check_win(player_2.player_number)):
        return (float('-inf'), None)

    if (current_player == player_1):
        max_score = float('-inf')
        best_move = None
        possible_moves = board.get_possible_moves(current_player.player_number)
        for move in possible_moves:
            board.make_move(move)
            score, previuos_best_move = minmax_alfabeta(
                board,
                depth - 1,
                player_2,
                player_1,
                player_2,
                alfa,
                beta
            )

            board.undo_move(move)
            if (score > max_score):
                max_score = score
                best_move = move

            alfa = max(alfa, score)
            if (beta <= alfa):
                break

        return (max_score, best_move)

    else:
        min_score = float('inf')
        min_move = None
        possible_moves = board.get_possible_moves(current_player.player_number)
        for move in possible_moves:
            board.make_move(move)
            score, previous_best_move = minmax_alfabeta(
                board,
                depth - 1,
                player_1,
                player_1,
                player_2,
                alfa,
                beta
            )

            board.undo_move(move)
            if (score < min_score):
                min_score = score
                min_move = move

            beta = min(beta, score)
            if (beta <= alfa):
                break

        return (min_score, min_move)