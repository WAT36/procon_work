class Solution:
    def countLargestGroup(self, n: int) -> int:
        sums=[]
        for i in range(1,n+1):
            sumi=0
            stri=str(i)
            for j in range(len(stri)):
                sumi+=int(stri[j])
            while sumi >= len(sums):
                sums.append([])
            sums[sumi].append(i)
        
        sizemap={}
        for j in sums:
            if len(j) not in sizemap.keys():
                sizemap[len(j)]=1
            else:
                sizemap[len(j)]=sizemap[len(j)]+1
        # print(sums)
        # print(sizemap)
        return sizemap[max(sizemap.keys())]

