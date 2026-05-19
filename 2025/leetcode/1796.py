class Solution:
    def secondHighest(self, s: str) -> int:
        nums="0123456789"
        numset=set([])
        for i in range(len(s)):
            if s[i] in nums:
                numset.add(int(s[i]))
        numlist=sorted(list(numset))
        if len(numlist) < 2:
            return -1
        else:
            return numlist[-2]
        