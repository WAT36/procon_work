class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        nowarr=[]
        for n in arr:
            if nowarr==[]:
                for p in pieces:
                    #print(n,p)
                    if p[0]==n:
                        nowarr=p
                        pieces.remove(p)
                        break
                else:
                    return  False
                nowarr.pop(0)
            else:
                if nowarr[0] == n:
                    nowarr.pop(0)
                else:
                    return  False
        return True