class Solution:
    def minimumSum(self, num: int) -> int:
        ans=99999999
        sn=str(num)
        ij=[0,1,2,3]
        for i in range(4):
            for j in range(i+1,4):
                kl= [k for k in ij if k not in [i,j]]
                k=kl[0]
                l=kl[1]
                ans=min(ans,int(sn[i]+sn[j])+int(sn[k]+sn[l]))
                ans=min(ans,int(sn[i]+sn[j])+int(sn[l]+sn[k]))
                ans=min(ans,int(sn[j]+sn[i])+int(sn[k]+sn[l]))
                ans=min(ans,int(sn[j]+sn[i])+int(sn[l]+sn[k]))
                print(ans)
        return ans