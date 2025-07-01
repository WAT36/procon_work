class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strnum=''
        for i in range(len(digits)):
            strnum += str(digits[i])
        ansnum = str(int(strnum)+1)
        ans=[]
        for i in range(len(ansnum)):
            ans.append(int(ansnum[i]))
        return ans