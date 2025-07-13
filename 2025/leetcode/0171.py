class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        columnTitle = columnTitle[::-1]
        ans=0
        keta=0
        for i in range(len(columnTitle)):
            ind = ALPHABET.find(columnTitle[i])
            ans += (26 ** keta) * (ind+1)
            keta +=  1
        return ans