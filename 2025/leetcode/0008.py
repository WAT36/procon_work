class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX,INT_MIN=(2**31)-1,-2**31
        NUMBERS=list("0123456789")
        signed=1
        signDecided=False
        strdigit=""
        ans=0
        for i in range(len(s)):
            #print(strdigit,NUMBERS)
            if s[i] == ' ':
                if signDecided or strdigit != "":
                    break
            elif s[i]=='+':
                if signDecided or strdigit != "":
                    break
                signDecided=True
            elif s[i] == '-':
                if signDecided:
                    break 
                elif strdigit == "":
                    signed=-1
                    signDecided=True
                else:
                    break
            elif s[i] in NUMBERS:
                strdigit += s[i]
            else:
                break

        if(strdigit == '0'*len(strdigit)):
            ans=0
        else:
            ans=signed*int(strdigit)
        #print(ans)

        if ans < INT_MIN:
            return INT_MIN
        elif ans > INT_MAX:
            return INT_MAX
        return ans