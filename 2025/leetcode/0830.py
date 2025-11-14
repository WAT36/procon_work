class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans=[]
        same=0
        start=-1
        end=-1
        for i in range(len(s)):
            if i>0:
                if s[i] == s[i-1]:
                    same+=1
                else:
                    end=i-1
                    if same>=3:
                        ans.append([start,end])
                    same=1
                    start=i
                    end=-1
            else:
                same=1
                start=0
        else:
            end=i
            if same>=3:
                ans.append([start,end])
        return ans