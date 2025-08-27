class Solution:
    def generateseq(self, seq:List[str], n: int):
        if n==1:
            return seq
        newseq=["0"+seq[i] for i in range(len(seq))] + ["1"+seq[len(seq)-1-i] for i in range(len(seq))]
        return self.generateseq(newseq,n-1)

    def grayCode(self, n: int) -> List[int]:
        seq=self.generateseq(["0","1"],n)
        print(seq)
        return [int(seq[i],2) for i in range(len(seq))]