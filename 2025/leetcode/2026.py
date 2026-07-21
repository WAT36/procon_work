class Solution:
    def minimumMoves(self, s: str) -> int:
        ans=0
        lists=list(s)
        for i in range(len(lists)):
            if lists[i]=='X':
                lists[i]='0'
                if i+1<len(lists):
                    lists[i+1]='0'
                if i+2<len(lists):
                    lists[i+2]='0'
                ans+=1
        return ans