class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans=[0 for _ in range(num_people)]
        i=0
        while candies>0:
            ans[i%num_people]+=((i+1) if i+1<=candies else candies)
            candies-=(i+1)
            i+=1
            #print(i,ans)
        return ans