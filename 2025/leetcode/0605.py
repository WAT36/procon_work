class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans=0
        ad_flag=False
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                if ad_flag or (i<len(flowerbed)-1 and flowerbed[i+1] == 1):
                    ad_flag=False
                else:
                    ans+=1
                    ad_flag=True
            else:
                ad_flag=True
        return ans >= n