class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        ans=items1
        for i2i in items2:
            for i in range(len(ans)):
                if i2i[0]==ans[i][0]:
                    ans[i]=[ans[i][0],ans[i][1]+i2i[1]]
                    break
            else:
                ans.append(i2i)
        ans.sort()
        return ans