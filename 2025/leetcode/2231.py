class Solution:
    def largestInteger(self, num: int) -> int:
        strnum=str(num)
        e=[]
        o=[]
        for s in strnum:
            if int(s)%2==0:
                e.append(s)
            else:
                o.append(s)
        e.sort()
        o.sort()
        ans=[]
        for s in strnum:
            if int(s)%2==0:
                ans.append(e.pop())
            else:
                ans.append(o.pop())
        return int(''.join(ans))