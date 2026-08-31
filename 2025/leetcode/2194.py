class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans=[]
        alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        c=s.split(':')
        a=alphabet[alphabet.index(c[0][0]):alphabet.index(c[1][0])+1]
        n1=int(c[0][1])
        n2=int(c[1][1])
        for i in range(len(a)):
            for j in range(n1,n2+1):
                ans.append(a[i]+str(j))
        return ans
