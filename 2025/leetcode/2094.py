class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ds=set([])
        for i in range(len(digits)):
            if digits[i]==0:
                continue
            for j in range(len(digits)):
                if i==j:
                    continue
                for k in range(len(digits)):
                    if i==k or j==k:
                        continue
                    elif digits[k]%2 != 0:
                        continue
                    ds.add(str(digits[i])+str(digits[j])+str(digits[k]))
        ans=list(ds)
        return sorted([int(ans[i]) for i in range(len(ans))])