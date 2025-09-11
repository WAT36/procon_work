class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        ans=""
        minus=""
        if num<0:
            minus="-"
            num*=-1
        while num>0:
            ans+=str(num%7)
            num//=7
        return minus + ans[::-1]