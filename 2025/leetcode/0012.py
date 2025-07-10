class Solution:
    def intToRoman(self, num: int) -> str:
        ans=""
        if(num // 1000 > 0):
            ans += "M" * (num  // 1000)
        num=num%1000
        hundred=num//100
        if(hundred == 9):
            ans+="CM"
        elif(4<hundred and hundred<9):
            ans+= ("D" + "C"*(hundred-5))
        elif(hundred == 4):
            ans+="CD"
        else:
            ans+= ("C"*hundred)
        num=num%100
        ten=num//10
        if(ten == 9):
            ans+="XC"
        elif(4<ten and ten<9):
            ans+= ("L" + "X"*(ten-5))
        elif(ten == 4):
            ans+="XL"
        else:
            ans+= ("X"*ten)
        num=num%10
        one=num//1
        if(one == 9):
            ans+="IX"
        elif(4<one and one<9):
            ans+= ("V" + "I"*(one-5))
        elif(one == 4):
            ans+="IV"
        else:
            ans+= ("I"*one)
        return ans
