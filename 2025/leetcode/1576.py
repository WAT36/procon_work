class Solution:
    def modifyString(self, s: str) -> str:
        alphabet="abcdefghijklmnopqrstuvwxyz"
        i=0
        while "?" in s:
            ind=s.index('?')
            if (ind>0 and s[ind-1] == alphabet[i]) or (ind<len(s)-1 and s[ind+1] == alphabet[i]):
                i+=1
                continue
            s=s.replace("?",alphabet[i],1)
            i+=1
            i%=len(alphabet)
        return s