class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans=[first]
        for i in range(len(encoded)):
            ai=bin(ans[-1])
            ei=bin(encoded[i])
            ans_i=''
            a_j=-1
            e_j=-1
            while(True):
                ans_j=''
                if(ai[a_j]=='b' and ei[e_j]=='b'):
                    break
                elif(ai[a_j]=='b'):
                    ans_j=ei[e_j]
                    e_j-=1
                elif(ei[e_j]=='b'):
                    ans_j=ai[a_j]
                    a_j-=1
                else:
                    ans_j='0' if ai[a_j]==ei[e_j] else '1'
                    a_j-=1
                    e_j-=1
                ans_i=ans_j+ans_i
            ans.append(int(ans_i,2))
        return ans