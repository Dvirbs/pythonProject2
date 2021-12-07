import typing

def max_seen_cells(picture: List[List[int]], row: int, col: int) -> int:
    """
    function that receives a partial image and a location on it, and returns the number of "visible" matches  from the
    cell at this location if all the unknown matches account for canines.
    :param picture: Two-dimensional picture picture representing a partial picture.
    :param row: the index of the raws
    :param col: the index of the column
    :return: An integer equal to the number of "visible" cells from the cell in the row row and the col column,
    when unknown cells are considered white cells.
    """
    pass

def board_start(n,m):
	# The function make a board game with -1 in all places
	# n: number of raws
	# m: number of columns
	#return: 2D matrix
	board = []
	for i in range(n):
		board.append(list())
		for j in range(m):
			board[i].append(list())
	return board


def next_step(board):
	# function that find the mext place on the board where we get -1
	for raw_i, raw in enumarate(board):
		for column_j, column in enumrate(raw):
			if column == -1:
				return [raw_i, column_j]
	return False


def solve_pazzer_helper(board):
	#backtracking function that fill the board in the correct place
	if check_constrains(board, constrains_set) == 0:
		return
	else:
		if not next_step:
			return board
		else:
			raw_i, column_j = next_step(board)
			board[raw_i][column_j] = 0
			next_step(board)
			board[raw_i][column_j] = 1
			next_step(board)
			return

