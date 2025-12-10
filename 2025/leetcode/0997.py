class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people=[i+1 for i in range(n)]
        p=[]
        trustee={}
        for t in trust:
            p.append(t[0])
            if t[1] not in trustee.keys():
                trustee[t[1]]=1
            else:
                tc=trustee[t[1]]
                trustee[t[1]]=tc+1
        judge=list(set(people)-set(p))
        if len(judge) != 1:
            return -1
        if judge[0] in trustee.keys() and trustee[judge[0]] != len(people) - 1:
            return -1
        return judge[0]
