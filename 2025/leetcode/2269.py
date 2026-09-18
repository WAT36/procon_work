class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans=0
        for i in range(len(str(num))):
            if i+k<=len(str(num)):
                div=int(str(num)[i:i+k])
                if div!=0 and num%div==0:
                    ans+=1
        return ans