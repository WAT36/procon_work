class Solution:
    def minOperations(self, logs: List[str]) -> int:
        nowstack=[]
        for l in logs:
            path=l.split('/')
            for p in path:
                if p == '' or p == '.':
                    continue
                elif p == '..':
                    if len(nowstack)>0:
                        nowstack.pop()
                else:
                    nowstack.append(p)
        return len(nowstack)