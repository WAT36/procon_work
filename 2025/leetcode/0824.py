class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ss=sentence.split()
        ans=[]
        for i in range(len(ss)):
            ansi=ss[i]
            if ansi[0] in ['a','e','i','o','u','A','E','I','O','U']:
                ansi=ansi+"ma"
            else:
                ansi=ansi[1:]+ansi[0]+"ma"
            ansi=ansi+("a"*(i+1))
            ans.append(ansi)
            #print(ansi)
        return ' '.join(ans)
