class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(numRows):
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
        return ans