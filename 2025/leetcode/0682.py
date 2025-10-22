class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        for oi in operations:
            if oi == "+":
                ans.append(ans[-1]+ans[-2])
            elif oi == "D":
                ans.append(2*ans[-1])
            elif oi == "C":
                ans.pop()
            else:
                ans.append(int(oi))
        return sum(ans)