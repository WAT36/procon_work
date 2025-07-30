class Solution:
    def makeAllParenthesis(self, parenthesisList: List[str]) -> List[str]:
        ans = []
        if len(parenthesisList) == 0:
            return ["()"]

        for i in range(len(parenthesisList)):
            for j in range(len(parenthesisList[i])):
                ans.append(parenthesisList[i][:j] + "()" + parenthesisList[i][j:])
        return list(set(ans))

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        for i in range(n):
            ans = self.makeAllParenthesis(ans)
        return ans
