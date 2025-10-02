class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans=[]
        minind=99999999
        for l2i in list2:
            if l2i not in list1:
                continue
            ans.append([l2i,list1.index(l2i)+list2.index(l2i)])
            minind=min(minind,list1.index(l2i)+list2.index(l2i))
        return [ans[i][0] for i in range(len(ans)) if ans[i][1] == minind]