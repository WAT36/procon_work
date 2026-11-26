class Solution:
    def minMaxDifference(self, num: int) -> int:
        strnum=str(num)

        maxnum=num
        for i in range(len(strnum)):
            if strnum[i]!="9":
                maxnum=int(strnum.replace(strnum[i],"9"))
                break

        minnum=num
        for i in range(len(strnum)):
            if strnum[i]!="0":
                minnum=int(strnum.replace(strnum[i],"0"))
                break

        return maxnum-minnum
