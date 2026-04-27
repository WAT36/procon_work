class Solution:
    def maximumTime(self, time: str) -> str:
        ans=""
        for i in range(1,len(time)+1):
            j=-1*i
            if time[j] == "?":
                if j==-1:
                    ans="9"+ans
                elif j==-2:
                    ans="5"+ans
                elif j==-4:
                    if time[-5]=="?" or time[-5]=="2":
                        ans="23"+ans
                        return ans
                    else:
                        ans="9"+ans
                elif j==-5:
                    if time[-4]<="3":
                        ans="2"+ans
                    else:
                        ans="1"+ans
            else:
                ans=time[j]+ans
        return ans
