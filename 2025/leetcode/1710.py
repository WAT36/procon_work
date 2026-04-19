class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes=sorted(boxTypes, key=lambda x:(x[1]), reverse=True)
        ans=0
        j=0
        for i in range(truckSize):
            while boxTypes[j][0]==0:
                j+=1
                if j>=len(boxTypes):
                    return ans
            ans+=boxTypes[j][1]
            boxTypes[j]=[boxTypes[j][0]-1,boxTypes[j][1]]
        return ans
            