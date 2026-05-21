class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        num="0123456789"
        ans=[]
        ansi=""
        for i in range(len(word)):
            if word[i] in num:
                ansi=ansi+word[i]
            else:
                if ansi!="":
                    while len(ansi)>0 and ansi[0]=="0":
                        ansi=ansi[1:]
                    ans.append(ansi)
                    ansi=""
        else:
            if ansi!="":
                while len(ansi)>0 and ansi[0]=="0":
                    ansi=ansi[1:]
                ans.append(ansi)
                ansi=""
        return len(list(set(ans)))