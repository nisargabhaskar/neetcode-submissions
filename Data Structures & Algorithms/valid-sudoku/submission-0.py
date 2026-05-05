import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            nos = [x for x in row if x != '.'] 
            if len(set(nos)) != len(nos):
                return False

        board_col = np.array(board).T.tolist()
        for col in board_col:
            nos = [x for x in col if x != '.'] 
            if len(set(nos)) != len(nos):
                return False

        board_cube = []
        for x in range(0,9,3):
            board_cube.append(board[x][:3] +board[x +1][:3] +board[x +2][:3])
            board_cube.append(board[x][3:6] +board[x +1][3:6] +board[x +2][3:6])
            board_cube.append(board[x][6:9] +board[x +1][6:9] +board[x +2][6:9])

        for cube in board_cube:
            nos = [x for x in cube if x != '.'] 
            if len(set(nos)) != len(nos):
                return False

        return True
