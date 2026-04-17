class Solution:
    def reformatNumber(self, number: str) -> str:
        number=number.replace(' ','')
        number=number.replace('-','')
        ans=""
        while True:
            if len(number)>4:
                ans=ans+number[:3]+"-"
                number=number[3:]
            elif len(number)==4:
                ans=ans+number[:2]+"-"
                number=number[2:]
            elif len(number)<=3:
                ans=ans+number
                break
        return ans
