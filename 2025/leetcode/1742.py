class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box=[]
        for i in range(lowLimit,highLimit+1):
            stri=str(i)
            ansi=0
            for j in range(len(stri)):
                ansi+=int(stri[j])
            if len(box)<=ansi:
                while len(box)<=ansi:
                    box.append(0)
            box[ansi]+=1
        return max(box)
