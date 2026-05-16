class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        w=[]
        count=0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count+=1
                if len(w)==0:
                    w.append(s1[i])
                    w.append(s2[i])
                else:
                    if s1[i]==w[1] and s2[i]==w[0]:
                        pass
                    else:
                        return False
        return count==0 or count==2