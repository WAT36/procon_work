class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moveslist=list(moves)
        if((moveslist.count("U") == moveslist.count("D")) and
           (moveslist.count("L") == moveslist.count("R"))):
            return True
        else:
            return False
