class Solution:
    def minDeletionSize(self, A: list[str]) -> int:
        ans=0
#        deletion=[]
        len_chr=len(A[0])
        for i in range(len_chr):
            chr_i=A[0][i]
            flag=False
            for j in range(len(A)-1):
                if(chr_i <= A[j+1][i]):
                    chr_i=A[j+1][i]
                else:
#                    deletion.append(i)
                    flag=True
                    break

            if(flag):
                ans+=1
#        print(deletion)
        return ans