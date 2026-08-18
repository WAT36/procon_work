class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s=title.split(' ')
        ans=[]
        for si in s:
            if len(si)<=2:
                ans.append(si.lower())
            else:
                ans.append(si[0].upper() + si[1:].lower())
        return ' '.join(ans)
