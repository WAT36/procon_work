class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans=0
        keyind={"type":0,"color":1,"name":2}
        for i in items:
            if(i[keyind[ruleKey]]==ruleValue):
                ans+=1
        return ans
