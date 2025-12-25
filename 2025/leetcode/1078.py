class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ts=text.split(' ')
        ans=[]
        for i in range(2,len(ts)):
            if i>=len(ts):
                break
            if ts[i-1]==second and ts[i-2]==first:
                ans.append(ts[i])
        return ans
