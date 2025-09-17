class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        ans_a=-1
        for i in range(len(a)):
            for j in range(i+1):
                #print(i,j,a[j:j+(len(a)-i)])
                if a[j:j+(len(a)-i)] not in b:
                    ans_a=len(a)-i
                    break
            if ans_a!=-1:
                break
        
        ans_b=-1
        for i in range(len(b)):
            for j in range(i+1):
                if b[j:j+(len(b)-i)] not in a:
                    ans_b=len(b)-i
                    break
            if ans_b!=-1:
                break
        
        return max(ans_a,ans_b)