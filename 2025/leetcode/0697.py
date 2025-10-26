class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        nmap={}
        for ni in nums:
            if ni in nmap:
                v=nmap[ni]
                nmap[ni]=v+1
            else:
                nmap[ni]=1
        #print(nmap)
        maxk=[]
        maxv=-1
        for k,v in nmap.items():
            if v > maxv:
                maxk=[k]
                maxv=v
            elif v == maxv:
                maxk.append(k)
                maxv=v
        firsti=[]
        lasti=[]
        ans=99999999999
        for k in maxk:
            firsti=nums.index(k)
            nums.reverse()
            lasti=(len(nums)-1)-nums.index(k)
            nums.reverse()
            ans=min(ans,lasti-firsti+1)
            #print(firsti,lasti,ans)
        return ans
            