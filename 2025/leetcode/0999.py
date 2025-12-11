class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        r=[]
        for i in range(len(board)):
            if "R" in board[i]:
                r=[board[i].index("R"),i]
                break
        ans=0
        x=r[0]
        y=r[1]
        while x>=0:
            if board[y][x] == 'B':
                break
            elif board[y][x] == 'p':
                ans+=1
                break
            x-=1        

        x=r[0]
        y=r[1]
        while x<len(board[0]):
            if board[y][x] == 'B':
                break
            elif board[y][x] == 'p':
                ans+=1
                break
            x+=1        

        x=r[0]
        y=r[1]
        while y>=0:
            if board[y][x] == 'B':
                break
            elif board[y][x] == 'p':
                ans+=1
                break
            y-=1        

        x=r[0]
        y=r[1]
        while y<len(board):
            if board[y][x] == 'B':
                break
            elif board[y][x] == 'p':
                ans+=1
                break
            y+=1        

        return ans