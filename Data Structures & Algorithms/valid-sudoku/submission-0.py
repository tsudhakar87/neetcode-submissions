from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = {}
        col_sets = {}
        square_sets = {}

        for i in range(9):
            row_sets[i] = set()
            col_sets[i] = set()
            square_sets[i] = set()

        for row in range(9):
            for col in range(9):
                curr_num = board[row][col]
                # if the current cell is empty, move along, we don't need to check it
                if curr_num == ".":
                    continue

                # otherwise, check if this number is in row set, col set, or square set
                if curr_num in row_sets[row]:
                    return False
                else:
                    row_sets[row].add(curr_num)

                if curr_num in col_sets[col]:
                    return False
                else:
                    col_sets[col].add(curr_num)
                
                square_idx = (row // 3) * 3 + (col // 3)

                if curr_num in square_sets[square_idx]:
                    return False
                else:
                    square_sets[square_idx].add(curr_num)

        return True