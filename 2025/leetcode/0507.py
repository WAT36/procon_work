import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        div=[1]
        for i in  range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                div.append(i)
                div.append(num//i)
        return num == sum(list(set(div)))