class Solution:
    def countPoints(self, rings: str) -> int:
        r=[set([]) for _ in range(10)]
        i=0
        while i<len(rings):
            j=int(rings[i+1])
            #print(i,j)
            r[j].add(rings[i])
            i+=2
        return len(list(filter(lambda x: len(list(x))==3,r)))