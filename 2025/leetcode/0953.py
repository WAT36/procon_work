class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        sorted_words= sorted(words,key=lambda x: [[order.index(x[i][j]) for j in range(len(x[i]))] for i in range(len(x))])
        # for i in range(len(words)):
        #     w=[]
        #     for j in range(len(words[i])):
        #         w.append(order.index(words[i][j]))
        #     print(words[i],w)
        return sorted_words == words