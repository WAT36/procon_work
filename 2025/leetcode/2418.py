class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        heights, names = zip(*sorted(zip(heights, names)))
        return names[::-1]