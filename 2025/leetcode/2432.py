class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        ans=9999999999
        start=0
        longest=-1
        for li in logs:
            time=li[1]-start
            if time>=longest:
                if time==longest and li[0]<=ans:
                    ans=li[0]
                elif time>longest:
                    ans=li[0]
                longest=time
            start=li[1]
            #print(ans,longest)
        return ans