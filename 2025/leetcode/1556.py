class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n<1000:
            return  str(n)
        else:
            strn=str(n)
            ans=strn[-3:]
            strn=strn[:-3]
            while len(strn)>=3:
                ans=strn[-3:]+"."+ans
                strn=strn[:-3]
            ans=strn+"."+ans if len(strn)>0 else ans 
            return  ans