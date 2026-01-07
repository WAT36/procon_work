class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        left=min(start,destination)
        right=max(start,destination)
        cd=sum(distance[left:right])
        ccd=sum(distance)-cd
        return min(cd,ccd)