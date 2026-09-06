class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        diff=(int(correct[:2])-int(current[:2]))*60 + (int(correct[3:])-int(current[3:]))
        ans=0
        while diff>0:
            if diff>=60:
                diff-=60
                ans+=1
            elif diff>=15:
                diff-=15
                ans+=1
            elif diff>=5:
                diff-=5
                ans+=1
            else:
                diff-=1
                ans+=1
            #print(ans,diff)
        return ans