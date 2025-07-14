class Solution:
    def makeLetters(self,letterList: List[str]) -> List[str]:
        if(letterList is None or len(letterList)==0):
            return []
        elif(len(letterList) == 1):
            return [letter for letter in list(letterList[0])]
        ans=[]
        for i in range(len(letterList[0])):
            latterList = self.makeLetters(letterList[1:])
            ans.extend([letterList[0][i] + letters for letters in latterList])
        return ans

    def letterCombinations(self, digits: str) -> List[str]:
        LETTERS={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        letters=[]
        for i in range(len(digits)):
            letters.append(LETTERS[digits[i]])
        return self.makeLetters(letters)