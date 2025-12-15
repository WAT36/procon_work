class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans=[]
        strnum=""
        for n in nums:
            strnum=strnum+str(n)
            ans.append(int(strnum,2)%5 == 0)
        return ans