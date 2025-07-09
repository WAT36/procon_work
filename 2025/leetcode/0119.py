class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[]
        for i in range(rowIndex+1):
            if(i==0):
                ans.append([1])
            elif(i==1):
                ans.append([1,1])
            else:
                ans_i=[]
                lastArr=ans[-1]
                ans_i.append(lastArr[0])
                for j in range(i-1):
                    ans_i.append(lastArr[j]+lastArr[j+1])
                ans_i.append(lastArr[-1])
                ans.append(ans_i)
        return ans[-1]