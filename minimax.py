from copy import deepcopy
def minimax(board, player):
	if player == 1:
		best = [None, -float("inf")]
	else:
		best = [None, float("inf")]
	result = board.check()
	if result in (1, 0, -1):
		return [None, result]
	for move in board.available_moves():
		new_board = deepcopy(board)
		new_board.move(move, player)
		_, score = minimax(new_board, -player)
		if player == 1:
			if score > best[1]:
				best = [move, score]
		else:
			if score < best[1]:
				best = [move, score]
	return best
