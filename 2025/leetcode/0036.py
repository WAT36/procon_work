class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #横
        for i in range(len(board)):
            digits=[]
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] in digits:
                        return False
                    digits.append(board[i][j])

        #縦
        for i in range(len(board)):
            digits=[]
            for j in range(len(board[i])):
                if board[j][i] != '.':
                    if board[j][i] in digits:
                        return False
                    digits.append(board[j][i])

        #ます
        for i in range(3):
            digits=[]
            for j in range(3):
                for k in range(i*3,(i+1)*3):
                    for l in range(j*3,(j+1)*3):
                        if board[k][l] != '.':
                            if board[k][l] in digits:
                                return False
                            digits.append(board[k][l])
                digits=[]
        return True