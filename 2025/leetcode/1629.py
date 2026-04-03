class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        keytime={}
        for i in range(len(keysPressed)):
            if i==0:
                keytime[keysPressed[i]]=releaseTimes[i]
            else:
                if keysPressed[i] in keytime:
                    keytime[keysPressed[i]]=max(keytime[keysPressed[i]],(releaseTimes[i]-releaseTimes[i-1]))
                else:
                    keytime[keysPressed[i]]=releaseTimes[i]-releaseTimes[i-1]
        ans=""
        val=-1
        for k,v in keytime.items():
            #print(k,v)
            if v>val:
                ans=k
                val=v
            elif v==val:
                ans=max(ans,k)
                val=v
        return ans