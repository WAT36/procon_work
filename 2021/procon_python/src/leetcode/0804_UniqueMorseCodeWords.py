class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

        ans=[]
        for w in words:
            sign=""
            for i in range(len(w)):
                sign+=morse[alpha.index(w[i])]
            ans.append(sign)
        return len(list(set(ans)))