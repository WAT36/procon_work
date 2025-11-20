class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fivebill=0
        tenbill=0
        twentybill=0
        for bill in bills:
            if bill == 5:
                fivebill+=1
            elif bill == 10:
                tenbill+=1
                if fivebill >= 1:
                    fivebill-=1
                else:
                    return False
            elif bill == 20:
                twentybill+=1
                if tenbill >= 1 and fivebill >= 1:
                    tenbill-=1
                    fivebill-=1
                elif fivebill >= 3:
                    fivebill-=3
                else:
                    return False
        return True