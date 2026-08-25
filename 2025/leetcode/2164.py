class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        e=[nums[i] for i in range(len(nums)) if i%2==0]
        o=[nums[i] for i in range(len(nums)) if i%2!=0]
        e=sorted(e)
        o=sorted(o)[::-1]
        ans=[]
        i=0
        while i<len(e) or i<len(o):
            if i<len(e):
                ans.append(e[i])
            if i<len(o):
                ans.append(o[i])
            i+=1
        return ans