class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        bits=bin((2**10)-1)[2:]
        ans=[]
        for i in range(2**10):
            bini=bin(i)[2:].zfill(10)
            if(bini.count('1') != turnedOn):
                continue
            hour=bini[:4]
            minute=bini[4:]

            h=0
            for j in range(4):
                if hour[3-j]=='1':
                    h+=(2**j)

            m=0
            for j in range(6):
                if minute[5-j]=='1':
                    m+=(2**j)
            
            if h<=11 and m<=59:
                ans.append(str(h)+':'+str(m).zfill(2))
        return ans