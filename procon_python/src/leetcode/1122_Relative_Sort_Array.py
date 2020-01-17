class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        set_arr=set()
        count=[0 for _ in range(1001)]
        for arri in arr1:
            count[arri]+=1
            set_arr.add(arri)

        ans=[]
        for arri in arr2:
            set_arr.remove(arri)
            count_arri=count[arri]
            for _ in range(count_arri):
                ans.append(arri)

        rest=sorted(list(set_arr))
        for resti in rest:
            count_resti=count[resti]
            for _ in range(count_resti):
                ans.append(resti)
        return ans