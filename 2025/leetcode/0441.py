class Solution:
    def arrangeCoins(self, n: int) -> int:
        k=1
        coins=1
        while True:
            #print(k,coins)
            if n<coins:
                return k-1
            elif n==coins:
                return k
            k+=1
            coins+=k