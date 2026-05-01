class Solution:
    def checks(self, nums: List[int], ind: int) -> bool:
        endind=ind-1 if ind!=0 else len(nums)-1
        while ind!=endind:
            if ind < len(nums)-1 and nums[ind] <= nums[ind+1]:
                ind+=1
            elif ind >= len(nums)-1:
                if nums[-1] <= nums[0]:
                    ind=0
                else:
                    return False
            else:
                return False
        return True

    def check(self, nums: List[int]) -> bool:
        inds=[i for i, x in enumerate(nums) if x == min(nums)]
        for i in inds:
            if self.checks(nums,i):
                return True
        return False