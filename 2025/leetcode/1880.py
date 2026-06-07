class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alphabet="abcdefghijklmnopqrstuvwxyz"
        ans1=""
        ans2=""
        anst=""
        for w in firstWord:
            ans1+=str(alphabet.index(w))
        for w in secondWord:
            ans2+=str(alphabet.index(w))
        for w in targetWord:
            anst+=str(alphabet.index(w))
        print(ans1,ans2,anst)
        return int(anst)==int(ans1)+int(ans2)
