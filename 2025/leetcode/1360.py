class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        s_format = '%Y-%m-%d'
        d1dt = datetime.datetime.strptime(date1, s_format)
        d2dt = datetime.datetime.strptime(date2, s_format)
        td = d2dt - d1dt
        return abs(td.days)
