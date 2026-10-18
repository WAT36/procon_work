class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        s_format = '%m-%d'
        aadt = datetime.datetime.strptime(arriveAlice, s_format)
        ladt = datetime.datetime.strptime(leaveAlice, s_format)
        abdt = datetime.datetime.strptime(arriveBob, s_format)
        lbdt = datetime.datetime.strptime(leaveBob, s_format)
        if ladt<abdt or lbdt<aadt:
            return 0
        elif aadt<=abdt and lbdt<=ladt:
            return (lbdt-abdt).days +1
        elif abdt<=aadt and ladt<=lbdt:
            return (ladt-aadt).days +1
        elif aadt<=lbdt and lbdt<=ladt:
            return (lbdt-aadt).days +1
        elif abdt<=ladt and ladt<=lbdt:
            return (ladt-abdt).days +1
        return -1