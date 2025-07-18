class Solution:
    def isHappy(self, n: int) -> bool:
        numset=set()
        while str(n) not in numset:
            str_n=str(n)
            numset.add(str_n)
            next_n=0
            for i in range(len(str_n)):
                next_n+=(int(str_n[i]))**2
            if next_n==1:
                return True
            n=next_n
        return False
