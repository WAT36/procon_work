class Solution:
    def countTime(self, time: str) -> int:
        ans1=1
        if time[0]=="?" and time[1]=="?":
            ans1=24
        elif time[0]=="?":
            ans1=0
            for i in range(3):
                t=str(i)+time[1]
                if "00"<=t and t<="23":
                    ans1+=1
        elif time[1]=="?":
            ans1=0
            for i in range(10):
                t=time[0]+str(i)
                if "00"<=t and t<="23":
                    ans1+=1

        ans2=1
        if time[3]=="?" and time[4]=="?":
            ans2=60
        elif time[3]=="?":
            ans2=0
            for i in range(6):
                t=str(i)+time[4]
                if "00"<=t and t<="59":
                    ans2+=1
        elif time[4]=="?":
            ans2=0
            for i in range(10):
                t=time[3]+str(i)
                if "00"<=t and t<="59":
                    ans2+=1
        return ans1*ans2