import copy
from typing import List
from typing import Set
from typing import Tuple
from typing import Optional

# part 1

def _black_white_max_seen_helper(picture: List[List[int]], color: str) -> List[List[int]]:
    """
    convetring all the cell of -1 to 1
    :param picture: the board
    :param color: black or white depend what we want to get in the end
    :return: picture - 2D list
    """
    new_pic = copy.deepcopy(picture)
    for row_j, row in enumerate(new_pic):
        for pix_i, pix in enumerate(row):
            if pix == -1 and color == 'white':
                new_pic[row_j][pix_i] = 1
            elif pix == -1 and color == 'black':
                new_pic[row_j][pix_i] = 0
    return new_pic


def _rightovers_raw_max_seen(leftover_items_of_pix_row: List[int], count: int = 0) -> int:
    """
    function that calculate the number of white cell that from given row on a picture
    :param leftover_items_of_pix_row: the given row from the given point until the end or
                                        Riverse given row from the start to the point
    :return: int that gives the number of white cell that we can see and the row and column
    """
    if leftover_items_of_pix_row == []:
        return count
    elif leftover_items_of_pix_row[0] == 0:
        return count
    return _rightovers_raw_max_seen(leftover_items_of_pix_row[1:], count + 1)


def _leftovers_raw_max_seen(leftover_items_of_pix_row: List[int], count: int = -1) -> int:
    """
    function that calculate the number of white cell that from given row on a picture
    :param leftover_items_of_pix_row: the given row from the given point until the end or
                                        Riverse given row from the start to the point
    :return: int that gives the number of white cell that we can see and the row and column
    """
    if leftover_items_of_pix_row == []:
        return count
    elif leftover_items_of_pix_row[0] == 0:
        return count
    return _rightovers_raw_max_seen(leftover_items_of_pix_row[1:], count + 1)


# def _leftovers_up_max_seen(picture: List[List[int]], col: int, count: int = 0) -> int:
#     """
#     function that calculate the number of white cell that from given place on a picture
#     :param picture: the board game
#     :param row: the row number place
#     :param col: the column number place
#     :param count: the counter
#     :return: int that gives the number of white cell that we can see and the row and column
#     """
#     print(picture)
#     if len(picture) == 0:
#         return count
#     elif picture[0][col] == 0:
#         return count
#     return _leftovers_up_max_seen(picture[1:], col, count + 1)


def _count_up(picture: List[List[int]], row: int, col: int) -> int:
    """
    :param picture: Two-dimensional picture picture representing a partial picture.
    :param row: the index of the raws
    :param col: the index of the column
    :return: int wich represent the up seen cell
    """
    sumi = 0
    i = row - 1
    while i >= 0:
        if picture[i][col] == 0:
            return sumi
        sumi += 1
        i -= 1
    return sumi


def _count_down(picture: List[List[int]], row: int, col: int) -> int:
    """
    :param picture: Two-dimensional picture picture representing a partial picture.
    :param row: the index of the raws
    :param col: the index of the column
    :return: int wich represent the down seen cell
    """
    sumi = 0
    i = row + 1
    while i < len(picture):
        if picture[i][col] == 0:
            return sumi
        sumi += 1
        i += 1
    return sumi


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
    pic = _black_white_max_seen_helper(picture, 'white')
    if pic[row][col] == 0:
        return 0
    else:
        count_to_right = _rightovers_raw_max_seen(pic[row][col:])
        count_to_left = _leftovers_raw_max_seen(pic[row][col::-1])
        count_down = _count_down(pic, row, col)
        count_up = _count_up(pic, row, col)
        tot_count = count_to_right + count_to_left + count_up + count_down
        return tot_count


def min_seen_cells(picture: List[List[int]], row: int, col: int) -> int:
    """
    function that receives a partial image and a location on it, and returns the number of "visible" matches  from the
    cell at this location if all the unknown matches account for canines.
    :param picture: Two-dimensional picture picture representing a partial picture.
    :param row: the index of the raws
    :param col: the index of the column
    :return: An integer equal to the number of "visible" cells from the cell in the row row and the col column,
    when unknown cells are considered black cells.
    """
    black_pic = _black_white_max_seen_helper(picture, 'black')
    if black_pic[row][col] == 0:
        return 0
    else:
        count_to_right = _rightovers_raw_max_seen(black_pic[row][col:])
        count_to_left = _leftovers_raw_max_seen(black_pic[row][col::-1])
        count_down = _count_down(black_pic, row, col)
        count_up = _count_up(black_pic, row, col)
        tot_count = count_to_right + count_to_left + count_up + count_down
        return tot_count


# part 2

def check_constraints(picture: List[List[int]], constraints_set: Set[Tuple[int, int, int]]) -> int:
    """
    function that get Partial image and set of constraints, returns an integer between 0 and 2 indicating success
    Satisfying the constraints in the partial picture.
    :param picture: the board
    :param constraints_set: Group constraints
    :return: Number from {2, 1, 0 }
    """
    counter = 0
    for tup in constraints_set:
        row = tup[0]
        col = tup[1]
        seen_cells = tup[2]
        max_seen = max_seen_cells(picture, row, col)
        min_seen = min_seen_cells(picture, row, col)
        if max_seen == min_seen == seen_cells:
            counter += 0
        elif min_seen <= seen_cells <= max_seen:
            counter += 1
        else:
            return 0
    if counter == 0:
        return 1
    else:
        return 2


# part 3

def board_start(n: int, m: int) -> List[List[int]]:
    """
    The function make a board game with -1 in all places
    :param n: number of rows
    :param m: number of columns
    :return: 2D matrix
    """
    board = []
    for i in range(n):
        board.append(list())
        for j in range(m):
            board[i].append(-1)
    return board


def next_step(board: List[List[int]]) -> List[int]:
    """
    function that find the mext place on the board where we get -1
    """
    for row_i, row in enumerate(board):
        for column_j, column in enumerate(row):
            if column == -1:
                return [row_i, column_j]
    return False


def solve_puzzle_helper(board: List[List[int]], constraints_set: Set[Tuple[int, int, int]]) -> Optional[
    List[List[int]]]:
    """
    backtracking function that fill the board in the correct place
    """
    if check_constraints(board, constraints_set) == 0:
        return None
    else:
        next_step_ = next_step(board)
        if not next_step_: #count
            return board
        else:
            row_i, column_j = next_step_
            board[row_i][column_j] = 0
            if solve_puzzle_helper(board, constraints_set) is not None:
                return board
            board[row_i][column_j] = 1
            if solve_puzzle_helper(board, constraints_set) is not None:
                return board
            board[row_i][column_j] = -1
            return


def solve_puzzle(constraints_set: Set[Tuple[int, int, int]], n: int, m: int) -> Optional[List[List[int]]]:
    """
    A function that accepts a set of constraints and a board plays, and returns an image depicting one solution
     of the board, if any.
    :param constraints_set: group constraints
    :param n: number of rows
    :param m: number of columns
    :return: image List 2D
    """
    reset_board = board_start(n, m)
    return solve_puzzle_helper(reset_board, constraints_set)

def solve_puzzle_helper2(board: List[List[int]], constraints_set: Set[Tuple[int, int, int]]) -> Optional[
    List[List[int]]]:
    """
    backtracking function that fill the board in the correct place
    """
    counter = 0
    if check_constraints(board, constraints_set) == 0:
        return 0
    else:
        next_step_ = next_step(board)
        if not next_step_: #count
            return 1
        else:
            row_i, column_j = next_step_
            board[row_i][column_j] = 0
            counter += solve_puzzle_helper2(board, constraints_set)

            board[row_i][column_j] = 1
            counter += solve_puzzle_helper2(board, constraints_set)
            board[row_i][column_j] = -1
            return counter


def how_many_solutions(constraints_set: Set[Tuple[int, int, int]], n: int, m: int) -> int:
    """
    A function that accepts a set of constraints and a board plays, and returns the number of solution
     of the board, if any.
    :param constraints_set: group constraints
    :param n: number of rows
    :param m: number of columns
    :return: int
    """
    reset_board = board_start(n, m)
    return solve_puzzle_helper2(reset_board, constraints_set)






# tests
## part 1
# picture1 = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
# row = 2
# col = 0
# assert max_seen_cells(picture1, row, col) == 1
# picture1 = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
# row = 1
# col = 2
# assert min_seen_cells(picture1, row, col) == 0

## part 2
# picture1 = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
# assert check_constraints(picture1, {(0, 3, 5), (1, 2, 5), (2, 0, 1)}) == 0
# picture1 = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
# assert check_constraints(picture1, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 2
# pic = [[0, 0, 0, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
##assert check_constraints(pic, {(0, 3, 3)}) == 0

##part 3
assert solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 0)}, 3, 4) == [[0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
assert solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)}, 3, 4)  == None
assert solve_puzzle({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) == [[0, 0, 1], [1, 1, 1], [1, 1, 1]]


## part 4
assert how_many_solutions({(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)}, 3, 4) == 0
assert how_many_solutions({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 1)}, 3, 4) == 1
assert how_many_solutions({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) == 2