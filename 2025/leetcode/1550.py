class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        odds=0      
        for i in range(len(arr)):
            if arr[i]%2==1:
                odds+=1
            print(i,odds)
            if odds==3:
                return True
            if i>=2:
                if arr[i-2]%2==1:
                    odds-=1
        return False
        


