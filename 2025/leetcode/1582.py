class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans=0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]==0:
                    continue
                for ii in range(len(mat)):
                    if ii==i:
                        continue
                    if mat[ii][j]==1:
                        # notm.append(ii)
                        break
                else:
                    for jj in range(len(mat[i])):
                        if jj==j:
                            continue
                        if mat[i][jj]==1:
                            # notn.append(jj)
                            break
                    else:
                        print(i,j)
                        ans+=1
        return ans

