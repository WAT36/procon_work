import copy
class Solution:
    def search(self, board: List[List[str]], checked: List[List[str]], i:int, j:int, word: str) -> bool:
        print(i,j,word)
        checked[i][j]=True
        result = False
        if i>0 and board[i-1][j]==word[0] and not checked[i-1][j]:
            if len(word) == 1:
                return True
            result = result or self.search(board,copy.deepcopy(checked),i-1,j,word[1:])
        if i<len(board)-1 and board[i+1][j]==word[0] and not checked[i+1][j]:
            if len(word) == 1:
                return True
            result = result or self.search(board,copy.deepcopy(checked),i+1,j,word[1:])
        if j>0 and board[i][j-1]==word[0] and not checked[i][j-1]:
            if len(word) == 1:
                return True
            result = result or self.search(board,copy.deepcopy(checked),i,j-1,word[1:])
        if j<len(board[0])-1 and board[i][j+1]==word[0] and not checked[i][j+1]:
            if len(word) == 1:
                return True
            result = result or self.search(board,copy.deepcopy(checked),i,j+1,word[1:])
        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        isstartsequence=1
        for i in range(1,len(word)):
            if word[i] == word[0]:
                isstartsequence+=1
            else:
                break

        isendsequence=1
        for i in range(len(word)-1,-1,-1):
            if word[i] == word[-1]:
                isendsequence+=1
            else:
                break

        if isstartsequence > isendsequence:
            word = word[::-1]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    checkedlist=[[False for _ in range(len(board[0]))] for _ in range(len(board))]
                    result=self.search(board,checkedlist,i,j,word[1:])
                    if result:
                        return True
        return False