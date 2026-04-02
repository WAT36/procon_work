class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        alphabet="abcdefghijklmnopqrstuvwxyz"
        ans=-1
        for w in alphabet:
            if w in s:
                inds=[]
                for i in range(len(s)):
                    if s[i]==w:
                        inds.append(i)
                if len(inds)>=2:
                    ans=max(ans,abs(inds[-1]-inds[0]-1))
                print(w,ans,inds,s)
        return ans
