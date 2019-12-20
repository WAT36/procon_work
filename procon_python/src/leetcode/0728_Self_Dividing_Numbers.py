class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans=[]
        for i in range(left,right+1):
            flag=True
            str_i=str(i)
            if('0' in str_i):
                continue

            for j in range(len(str_i)):
                if(i%int(str_i[j]) != 0):
                    flag=False
                    break
            if(flag):
                ans.append(i)

        return(ans)
