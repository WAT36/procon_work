class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',
               11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',
               21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
        i=0
        n=len(s)
        ans=[]
        while(i<n):
            if(i<n-2 and s[i+2]=='#'):
                num=int(s[i:i+2])
                ans.append(alpha[num])
                i+=3
            else:
                num=int(s[i])
                ans.append(alpha[num])
                i+=1
        return ''.join(ans)