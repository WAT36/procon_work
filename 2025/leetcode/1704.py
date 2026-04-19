class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels=['a','e','i','o','u']
        a=s[:len(s)//2]
        b=s[len(s)//2:]
        av=[]
        bv=[]
        for ai in a:
            if ai.lower() in vowels:
                av.append(ai.lower)
        for bi in b:
            if bi.lower() in vowels:
                bv.append(bi.lower)
        return len(av) == len(bv)