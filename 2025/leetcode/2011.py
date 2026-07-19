class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans=0
        for o in operations:
            if '+' in o:
                ans+=1
            elif '-' in o:
                ans-=1
        return ans