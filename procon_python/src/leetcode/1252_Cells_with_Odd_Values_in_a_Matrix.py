class Solution:
    def oddCells(self, n: int, m: int, indices: list[list[int]]) -> int:
        n_point=[0 for _ in range(n)]
        m_point=[0 for _ in range(m)]
        for i in range(len(indices)):
            ind_i=indices[i]
            n_point[ind_i[0]]+=1
            m_point[ind_i[1]]+=1

        ans=0
        for i in range(n):
            for j in range(m):
                if( (n_point[i]+m_point[j])%2 != 0 ):
                    ans+=1
        return ans