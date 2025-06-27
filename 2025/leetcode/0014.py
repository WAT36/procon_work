class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        ans = ""
        min_len = len(min(strs))
        for i in range(min_len):
            ans_i = strs[0][i]
            for j in range(len(strs)):
                if(ans_i != strs[j][i]):
                    return ans
            ans += ans_i
        return ans
            
        