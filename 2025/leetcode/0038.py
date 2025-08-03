class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        subsay=self.countAndSay(n-1)
        maps={}
        list_subsay=list(subsay)
        ans=""
        nowValue=None
        nowCount=0
        for i in range(len(list_subsay)):
            if nowValue is None:
                nowValue=list_subsay[i]
                nowCount+=1
            elif nowValue == list_subsay[i]:
                nowCount+=1
            else:
                ans+=str(nowCount) + str(nowValue)
                nowValue=list_subsay[i]
                nowCount=1
        else:
            ans+=str(nowCount) + str(nowValue)
            nowValue=list_subsay[i]
            nowCount=1
        return ans