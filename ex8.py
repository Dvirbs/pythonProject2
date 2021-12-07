import copy
from typing import List
from typing import Set
from typing import Tuple


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


def _leftovers_up_max_seen(picture: List[List[int]], col: int, count: int = 0) -> int:
    """
    function that calculate the number of white cell that from given place on a picture
    :param picture: the board game
    :param row: the row number place
    :param col: the column number place
    :param count: the counter
    :return: int that gives the number of white cell that we can see and the row and column
    """
    if len(picture) == 0:
        return count
    elif picture[0][col] == 0:
        return count
    return _leftovers_up_max_seen(picture[1:], col, count + 1)


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
        count_down = _leftovers_up_max_seen(pic[row + 1:], col)
        count_up = _leftovers_up_max_seen(pic[row - 1::-1], col)
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
        count_down = _leftovers_up_max_seen(black_pic[row + 1:], col)
        count_up = _leftovers_up_max_seen(black_pic[row - 1::-1], col)
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
#assert check_constraints(picture1, {(0, 3, 5), (1, 2, 5), (2, 0, 1)}) == 0
# picture1 = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
# assert check_constraints(picture1, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 2
