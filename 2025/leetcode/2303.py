class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        money=min(income,brackets[0][0])
        income-=brackets[0][0]
        ans=money*brackets[0][1]*0.01
        if income<=0:
            return ans
        for i in range(1,len(brackets)):
            if income<=0:
                return ans
            money=min(income,brackets[i][0]-brackets[i-1][0])
            income-=brackets[i][0]-brackets[i-1][0]
            ans+=money*brackets[i][1]*0.01
        return ans