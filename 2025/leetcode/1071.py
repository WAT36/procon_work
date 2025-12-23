class Solution:
    def divisor(self,n: int) -> [int]:
        ans=[]
        for i in range(1,n+1):
            if n%i==0:
                ans.append(i)
        return ans

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1ans=[]
        str1divs=self.divisor(len(str1))
        for i in str1divs:
            str1_i=str1[:i]
            #print(i,str1_i)
            j=0
            while j+i<=len(str1):
                if str1_i != str1[j:j+i]:
                    break
                j+=i
            else:
                str1ans.append(str1_i)
        #print(str1ans)
        if len(str1ans)==0:
            return ""
        
        str2ans=[]
        str2divs=self.divisor(len(str2))
        for i in str2divs:
            str2_i=str2[:i]
            j=0
            while j+i<=len(str2):
                if str2_i != str2[j:j+i]:
                    break
                j+=i
            else:
                str2ans.append(str2_i)
        #print(str2ans)
        if len(str2ans)==0:
            return ""
        anslist=list(set(str1ans) & set(str2ans))
        if len(anslist)==0:
            return ""
        ans=anslist[0]
        for ansi in anslist:
            if len(ansi) > len(ans):
                ans=ansi
        return ans
