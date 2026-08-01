class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets[k]=-1*tickets[k]
        ans=0
        while True:
            ans+=1
            if tickets[0]<0:
                if tickets[0]==-1:
                    break
                else:
                    tickets=[*tickets[1:],tickets[0]+1]
            elif tickets[0]==1:
                tickets=tickets[1:]
            else:
                tickets=[*tickets[1:],tickets[0]-1]
            #print(ans,tickets)
        return ans