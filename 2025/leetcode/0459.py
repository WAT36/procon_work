class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1,len(s)):
            if len(s)%i!=0:
                continue
            substr=s[:i]
            j=i
            flag=True
            while j<=len(s):
                if s[j-i:j] != substr:
                    flag=False
                    break
                j+=i
            if flag:
                return True
        return False
