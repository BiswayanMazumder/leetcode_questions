class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cross3 = {}
        for i in range(3):
            for j in range(3):
                cross3 = {}
                for x in range(i*3, i*3+3):
                    for y in range(j*3, j*3+3):
                        if board[x][y] != '.':
                            if board[x][y] not in cross3:
                                cross3[board[x][y]] = ''
                            else:
                                return False
        Big_Location = {"1x":{}, "2x":{}, "3x":{}, "4x":{}, "5x":{}, "6x":{}, "7x":{}, "8x":{}, "9x":{}, "1y":{}, "2y":{}, "3y":{}, "4y":{}, "5y":{}, "6y":{}, "7y":{}, "8y":{}, "9y":{}}
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] != '.':
                    if x in Big_Location[board[x][y]+"x"] or y in Big_Location[board[x][y]+"y"]:
                        return False
                    else:
                        Big_Location[board[x][y]+"x"][x] = "f"
                        Big_Location[board[x][y]+"y"][y] = "f"
        return True