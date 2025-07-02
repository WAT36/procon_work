class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        for i in range(len(s)):
            ans_i=s[i]
            j=i
            k=i
            while True:
                j=j-1
                k=k+1
                if j<0 or len(s)<=k:
                    break
                else:
                    if s[j] == s[k]:
                        ans_i = s[j] + ans_i + s[k]
                    else:
                        break
            if len(ans_i) > len(ans):
                ans = ans_i

            if(i ==  len(s)-1):
                break
            elif s[i] == s[i+1]:
                ans_i = s[i] + s[i+1]
                j=i
                k=i+1
                while True:
                    j=j-1
                    k=k+1
                    if j<0 or len(s)<=k:
                        break
                    else:
                        if s[j] == s[k]:
                            ans_i = s[j] + ans_i + s[k]
                        else:
                            break
                if len(ans_i) > len(ans):
                    ans = ans_i
        return ans

