class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        sum=0
        str_n=str(n)
        for i in range(len(str_n)):
            product*=int(str_n[i])
            sum+=int(str_n[i])
        return product-sum