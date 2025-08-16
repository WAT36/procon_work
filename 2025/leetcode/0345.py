class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS=list('aeiouAEIOU')
        vlist = []
        for i in range(len(s)):
            if s[i] in VOWELS:
                vlist.append(s[i])
        reverse_vlist=vlist[::-1]
        ans=""
        j=0
        for i in range(len(s)):
            if j<len(vlist) and s[i] == vlist[j]:
                ans=ans+reverse_vlist[j]
                j+=1
            else:
                ans=ans+s[i]
        # print(vlist)
        # print(reverse_vlist)
        return ans
        