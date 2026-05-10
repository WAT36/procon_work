class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                ssub=s[i:j+1]
                ssubwords=list(set(list(ssub.lower())))
                for sw in ssubwords:
                    if sw.lower() not in ssub or sw.upper() not in ssub:
                        break
                else:
                    if len(ans) < len(ssub):
                        ans=ssub
                #print(i,j,ssub,ssubwords,ans)
        return ans            
