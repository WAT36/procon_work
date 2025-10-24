class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans=0
        concount=[]
        now_num=s[0]
        now_count=0
        for si in s:
            if si != now_num:
                concount.append(now_count)
                now_num=si
                now_count=1
            else:
                now_count+=1
        else:
            concount.append(now_count)
        #print(concount)
        for i in range(len(concount)-1):
            ans+=min(concount[i],concount[i+1])
        return ans